"""Troca a parede da foto do Gemini por uma parede lisa e grava a máscara da pessoa.
A parede que o Gemini entrega tem vinheta forte e o recorte automático do motor leva a parede junto.
  python3 alisar.py <pasta>/geradas/foto.png          -> foto-lisa.png e foto-lisa-mascara.png
O slides.py usa a máscara no lugar do recorte automático (ver exemplo/slides.py, _recorte_pela_mascara)."""
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

origem = sys.argv[1]
base = origem.rsplit('.', 1)[0]
im = np.asarray(Image.open(origem).convert('RGB')).astype(float)
h, w, _ = im.shape
mx, mn = im.max(-1), im.min(-1)
parede = ((mx - mn) / np.maximum(mx, 1) < 0.07) & (im.mean(-1) > 120)  # cinza claro e sem cor = parede
duro = Image.fromarray(((~parede) * 255).astype(np.uint8)).filter(ImageFilter.MedianFilter(5))
d = duro.copy()
ImageDraw.floodfill(d, (w // 2 - 40, h // 3), 128)
m = Image.new('L', (w + 2, h + 2), 0)
m.paste(Image.fromarray(((np.asarray(d) == 128) * 255).astype(np.uint8)), (1, 1))
ImageDraw.floodfill(m, (0, 0), 64)
pessoa = (np.asarray(d) == 128) | (np.asarray(m)[1:-1, 1:-1] == 0)
mascara = Image.fromarray((pessoa * 255).astype(np.uint8)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
a = np.asarray(mascara)[..., None] / 255
yy, xx = np.linspace(0, 1, h)[:, None, None], np.linspace(-1, 1, w)[None, :, None]
fundo = np.array([232, 235, 234]) - yy * 26 - np.abs(xx) * 10
Image.fromarray((im * a + fundo * (1 - a)).clip(0, 255).astype(np.uint8)).save(base + '-lisa.png')
mascara.save(base + '-lisa-mascara.png')
print('pessoa ocupa', round(pessoa.mean() * 100), '% da foto:', base + '-lisa.png')
