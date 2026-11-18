"""Prova dos stories (1080x1920): 3 telas, sem precisar de nenhuma imagem (o fundo das fotos é desenhado aqui).

  cp -r exemplo/prova-stories "${CARROSSEIS:-$HOME/carrosseis}/00-prova-stories"
  python3 motor/montar.py 00-prova-stories

Moldes: capa com gancho, tela de conteúdo com a peça grande (sem texto de apoio) e tela final com a chamada.
"""
import os
import subprocess

from comum import (ATE, MARGEM, PASTA, SOMBRA, TEXTO_Y, abrir, abrir_foto, chamada, fechar, fio, foto_inteira, manchete, pc,
                   tarja_da_capa, tema, titulo_de_foto, topo)

ALTURA = 1920

os.makedirs(os.path.join(PASTA, 'geradas'), exist_ok=True)
FUNDO = os.path.join(PASTA, 'geradas', 'fundo-prova.png')
if not os.path.exists(FUNDO):  # no story de verdade aqui entra a foto gerada (modelos-de-prompt/pessoa.md, formato 9:16)
    subprocess.run(['magick', '-size', '1080x1920', 'gradient:#9AA3AF-#1F2933', FUNDO], check=True)


def s1():
    abrir_foto(1)
    foto_inteira('fundo-prova.png')
    topo('branco', arroba=False)
    titulo_de_foto('Stories no Atelier', 'PRONTO', 250)
    tarja_da_capa('3 telas de prova')
    fechar(1)


def s2():
    abrir(2)
    manchete(['Print grande,', '!uma frase só.'])
    y, h = TEXTO_Y + 48, ATE - TEXTO_Y - 48  # sem texto de apoio, a peça sobe e ocupa a tela
    pc.forma('PECA', 'roundedRect', MARGEM, y, 920, h, tema()['tit'], 30, sombra=SOMBRA)
    for i in range(4):
        pc.forma(f'PECA-LINHA-{i + 1}', 'roundedRect', MARGEM + 48, y + 64 + i * 150, 824, 104, '#3A3F48', 20)
    fio('E no fim?', primeiro=True)
    fechar(2)


def s3():
    abrir_foto(3)
    foto_inteira('fundo-prova.png')
    topo('branco', arroba=False)
    titulo_de_foto('Uma chamada só', 'NO FIM', 250)
    chamada('Responda', 'SIM')
    fechar(3)


SLIDES = {1: s1, 2: s2, 3: s3}
