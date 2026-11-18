"""Prova do card (post único, 1080x1350): uma imagem só, sem fio.

  cp -r exemplo/prova-card "${CARROSSEIS:-$HOME/carrosseis}/00-prova-card"
  python3 motor/montar.py 00-prova-card

Molde "número que choca": título curto, frase em tarja e o número grande no lugar da peça.
"""
from comum import CARD_ATE, abrir, corpo, fechar, manchete, palavra_de_impacto, tema

ALTURA = 1350


def s1():
    abrir(1, card=True)
    y = manchete(['Um card, uma ideia,', '!uma imagem só.'])
    corpo(['O número vem grande e o resto fica curto.', '!Sem fio: o card não continua.'], y)
    palavra_de_impacto('1 POST', base=CARD_ATE - 40, tam=300, cor=tema()['dest'])  # destaque que dá leitura no fundo
    fechar(1)


SLIDES = {1: s1}
