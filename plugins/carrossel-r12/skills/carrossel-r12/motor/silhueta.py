"""Recorta a pessoa de uma foto de estúdio (parede lisa em degradê) e salva em PNG com fundo transparente.

Serve para pôr um objeto ATRÁS da pessoa no PhotoCraft: a foto inteira fica embaixo, o objeto no meio e
o recorte da pessoa por cima, no mesmo lugar. Onde não há objeto, nada muda na imagem.

Como funciona: a parede é lisa, então dá para "adivinhar" a cor dela em cada ponto a partir das faixas
onde só existe parede (as duas laterais e o topo). Tudo que foge dessa cor é a pessoa.
Quando existe <foto>-mascara.png ao lado da foto (o alisar.py grava), o recorte vai pela máscara. Quando o cabelo
entra na faixa de cima (o topo não é só parede), a máscara é feita na hora, pelo mesmo método do alisar.py.

Uso: python3 photocraft/silhueta.py <foto> <saida.png> <x_do_rosto> <y_do_rosto>
"""
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

from alisar import e_parede, mascara

MAX_PESSOA = 0.70  # acima disso o recorte levou a parede junto


def _conferir_tamanho(alfa):
    cobre = float((alfa > 0.5).mean())
    if cobre > MAX_PESSOA:
        raise ValueError(f'o recorte da pessoa cobre {cobre:.0%} da foto (o limite é {MAX_PESSOA:.0%}): levou a parede junto. '
                         'Rode python3 motor/alisar.py <foto> e use a foto -lisa.png; se continuar, gere a foto com mais parede em volta.')


def recortar_pessoa(origem, destino, rosto, lado=0.10, topo=0.24, t0=14, t1=36):
    """`rosto` é um ponto (x, y) dentro do rosto, em px da foto. `lado` e `topo` dizem que fatia das bordas
    é só parede. `t0` e `t1`: diferença de cor em que um ponto começa a ser pessoa e em que é pessoa por inteiro."""
    img = np.asarray(Image.open(origem).convert('RGB')).astype(np.float64)
    h, w, _ = img.shape
    arq = os.path.splitext(origem)[0] + '-mascara.png'
    if os.path.exists(arq) or e_parede(img)[:int(topo * h)].mean() < 0.97:  # máscara pronta, ou cabelo na faixa de cima
        m = Image.open(arq).convert('L') if os.path.exists(arq) else mascara(img, rosto)
        if m.size != (w, h):
            raise ValueError(f'{os.path.basename(arq)} tem {m.size[0]}x{m.size[1]} e a foto {w}x{h}: rode o alisar.py de novo nesta foto.')
        alfa = np.asarray(m) / 255
        _conferir_tamanho(alfa)
        Image.fromarray(np.dstack([img.round(), alfa * 255]).round().astype(np.uint8), 'RGBA').save(destino)
        return None
    yy, xx = np.mgrid[0:h, 0:w]
    x, y = xx / w - 0.5, yy / h - 0.5
    parede = (xx < lado * w) | (xx >= (1 - lado) * w) | (yy < topo * h)

    def base(x, y):  # superfície lisa de grau 3: dá conta da luz mais forte no meio e do canto escuro
        return np.stack([np.ones_like(x), x, y, x * x, x * y, y * y, x ** 3, x * x * y, x * y * y, y ** 3], -1)

    amostra, tudo = base(x[parede], y[parede])[::5], base(x, y).reshape(-1, 10)
    placa = np.empty_like(img)
    for c in range(3):
        coef, *_ = np.linalg.lstsq(amostra, img[..., c][parede][::5], rcond=None)
        placa[..., c] = (tudo @ coef).reshape(h, w)

    dif = np.sqrt(((img - placa) ** 2).sum(-1))
    alfa = np.clip((dif - t0) / (t1 - t0), 0, 1)

    # Fecha buracos (branco do olho, brilho do celular) e joga fora sujeira solta: fica só o que está ligado ao rosto.
    duro = Image.fromarray(((alfa >= 0.5) * 255).astype(np.uint8)).copy()  # sem o copy o Pillow não deixa pintar e não avisa
    assert duro.getpixel(rosto) == 255, 'o ponto do rosto caiu fora da pessoa'
    ImageDraw.floodfill(duro, rosto, 128)                      # 128 = pessoa
    solto = np.asarray(duro) == 255                            # passou do corte, mas não encosta na pessoa
    moldura = Image.new('L', (w + 2, h + 2), 0)
    moldura.paste(Image.fromarray(((np.asarray(duro) == 128) * 255).astype(np.uint8)), (1, 1))
    ImageDraw.floodfill(moldura, (0, 0), 64)                   # 64 = parede ligada à borda
    buraco = np.asarray(moldura)[1:-1, 1:-1] == 0              # parede cercada de pessoa
    # A transparência suave só vale numa faixa fina em volta da silhueta: por dentro a pessoa é inteira
    # (senão a pele clara fica furada) e longe dela não sobra nada (senão a sombra da parede vem junto).
    pessoa = Image.fromarray((((np.asarray(duro) == 128) | buraco) * 255).astype(np.uint8))
    miolo = np.asarray(pessoa.filter(ImageFilter.MinFilter(7))) == 255
    perto = np.asarray(pessoa.filter(ImageFilter.MaxFilter(5))) == 255
    # Na beirada cada ponto mistura pessoa e parede. Quanto dele é pessoa: a distância dele até a cor da parede
    # dividida pela distância da pessoa "cheia" ali ao lado (o maior valor na vizinhança). Com um corte fixo,
    # a beirada da camisa escura saía inteira e clara, e ficava um fio branco em volta do ombro.
    cheio = np.asarray(Image.fromarray(np.clip(dif / 2, 0, 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(9))).astype(np.float64) * 2
    borda = np.clip((dif - t0) / np.maximum(cheio * 0.85 - t0, t1 - t0), 0, 1)
    alfa = np.where(miolo, 1.0, np.where(perto, borda, 0.0))
    alfa[alfa < 0.08] = 0
    alfa = np.asarray(Image.fromarray((alfa * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))) / 255
    alfa = np.where(miolo, 1.0, alfa)

    # Tira a cor da parede da beirada: sem isso sobra um fio claro em volta do cabelo quando ele passa na frente do objeto.
    a = alfa[..., None]
    frente = np.where(a > 0, (img - (1 - a) * placa) / np.maximum(a, 0.25), img)
    rgba = np.dstack([np.clip(frente, 0, 255), alfa * 255]).round().astype(np.uint8)
    # Recorte que levou parede junto falhava calado (parede branca com camisa branca): a faixa das laterais é parede.
    sobra = float((alfa[parede & (yy > topo * h)] > 0.5).mean()) if (parede & (yy > topo * h)).any() else 0.0
    if sobra > 0.25:
        raise ValueError(f'o recorte da pessoa levou parede junto ({sobra:.0%} das laterais): gere a foto com parede cinza clara '
                         'e roupa que contraste, ou monte sem objeto atrás (sem atras=).')
    _conferir_tamanho(alfa)
    Image.fromarray(rgba, 'RGBA').save(destino)
    return dif[parede].max(), np.percentile(dif[parede], 99.5)


if __name__ == '__main__':
    erro = recortar_pessoa(sys.argv[1], sys.argv[2], (int(sys.argv[3]), int(sys.argv[4])))
    if erro is None:
        print('recortado pela máscara (cabelo no topo ou -mascara.png ao lado da foto)')
    else:
        pior, quase = erro
        print(f'erro da parede adivinhada: pior ponto {pior:.0f}, 99,5% abaixo de {quase:.0f} (o corte começa em 14)')
