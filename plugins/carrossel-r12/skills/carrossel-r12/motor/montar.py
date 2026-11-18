"""Monta um carrossel no PhotoCraft: psd/ com camadas, png/ para postar e folha.jpg com todos os slides.

  python3 motor/montar.py <pasta-do-carrossel>              todos os slides
  python3 motor/montar.py <pasta> 1 5                       só a capa e o slide 5
  PREVIA=1 python3 motor/montar.py <pasta> [slides]         grava em <pasta>/previa, sem mexer no que está pronto

<pasta> é a pasta do carrossel (ou o caminho dela dentro de ~/carrosseis) e tem de ter um slides.py
com SLIDES = {1: s1, 2: s2, ...}. A linha `ALTURA = 1350` no slides.py monta em 4:5 (1080x1350); sem ela, 3:4 (1080x1440). As peças e as regras estão no comum.py; o modelo está em exemplo/slides.py.
"""
import os
import re
import sys

if len(sys.argv) < 2:
    raise SystemExit(__doc__)
RAIZ = os.path.abspath(os.path.expanduser(os.environ.get('CARROSSEIS', '~/carrosseis')))
pasta = os.path.abspath(sys.argv[1] if os.path.isdir(sys.argv[1]) else os.path.join(RAIZ, sys.argv[1]))
if not pasta.startswith(RAIZ + os.sep):
    raise SystemExit(f'a pasta do carrossel tem de ficar dentro de {RAIZ} (o PhotoCraft só lê e grava lá): {pasta}')
if not os.path.exists(os.path.join(pasta, 'slides.py')):
    raise SystemExit(f'não achei {pasta}/slides.py')
os.environ['CARROSSEL'] = pasta
# Formato: a linha `ALTURA = 1350` no slides.py escolhe o 4:5; sem ela, 1440 (3:4).
_altura = re.search(r'^ALTURA\s*=\s*(\d+)', open(os.path.join(pasta, 'slides.py'), encoding='utf-8').read(), re.M)
os.environ['ALTURA'] = _altura.group(1) if _altura else '1440'
sys.path.insert(1, pasta)

import comum  # noqa: E402  (só depois de dizer qual é o carrossel)
import slides  # noqa: E402

comum.rodar(slides.SLIDES, sys.argv[2:])
