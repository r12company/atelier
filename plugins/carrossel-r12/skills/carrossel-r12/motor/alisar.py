"""Troca a parede da foto do Gemini por uma parede lisa e grava a máscara da pessoa.
A parede que o Gemini entrega tem vinheta forte e, quando o cabelo chega perto da borda de cima, o recorte
automático leva a parede junto. A máscara resolve os dois casos.
  python3 alisar.py <pasta>/geradas/foto.png          -> foto-lisa.png e foto-lisa-mascara.png
Depois use foto-lisa.png no slides.py: o motor acha a foto-lisa-mascara.png ao lado e recorta por ela."""
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter


def e_parede(im):
    """Cinza claro e sem cor = parede (im: matriz RGB em float)."""
    mx, mn = im.max(-1), im.min(-1)
    return ((mx - mn) / np.maximum(mx, 1) < 0.07) & (im.mean(-1) > 120)


def mascara(im, ponto=None):
    """Máscara da pessoa (PIL 'L', 255 = pessoa). `ponto` (x, y) cai dentro da pessoa; sem ele, um pouco acima do meio."""
    h, w, _ = im.shape
    duro = Image.fromarray(((~e_parede(im)) * 255).astype(np.uint8)).filter(ImageFilter.MedianFilter(5))
    d = duro.copy()
    ponto = ponto or (w // 2 - 40, h // 3)
    if d.getpixel(ponto) != 255:
        raise ValueError(f'o ponto {ponto} caiu na parede, não na pessoa: confira o centro do rosto com a régua de foto.')
    ImageDraw.floodfill(d, ponto, 128)
    m = Image.new('L', (w + 2, h + 2), 0)
    m.paste(Image.fromarray(((np.asarray(d) == 128) * 255).astype(np.uint8)), (1, 1))
    ImageDraw.floodfill(m, (0, 0), 64)
    pessoa = (np.asarray(d) == 128) | (np.asarray(m)[1:-1, 1:-1] == 0)
    return Image.fromarray((pessoa * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    origem = sys.argv[1]
    base = origem.rsplit('.', 1)[0]
    im = np.asarray(Image.open(origem).convert('RGB')).astype(float)
    h, w, _ = im.shape
    masc = mascara(im)
    a = np.asarray(masc)[..., None] / 255
    yy, xx = np.linspace(0, 1, h)[:, None, None], np.linspace(-1, 1, w)[None, :, None]
    fundo = np.array([232, 235, 234]) - yy * 26 - np.abs(xx) * 10
    Image.fromarray((im * a + fundo * (1 - a)).clip(0, 255).astype(np.uint8)).save(base + '-lisa.png')
    masc.save(base + '-lisa-mascara.png')
    print('pessoa ocupa', round((a > 0.5).mean() * 100), '% da foto:', base + '-lisa.png')
