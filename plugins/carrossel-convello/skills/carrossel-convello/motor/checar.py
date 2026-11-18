"""Confere, antes de começar, se este computador consegue montar um carrossel no Atelier. Rodar sempre primeiro.

  python3 motor/checar.py

Diz o que falta e como resolver, em português simples. Sai com erro quando falta algo sem o qual não dá para montar.
Sem montagem automática ainda dá para fazer roteiro, legenda, pedidos de imagem e montar à mão (referencias/caminho-b.md).
"""
import glob
import os
import shutil
import subprocess
import sys

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.abspath(os.path.expanduser(os.environ.get('CARROSSEIS', '~/carrosseis')))
faltas = []


def linha(ok, nome, detalhe='', grave=True):
    print(f'  {"ok   " if ok else ("FALTA" if grave else "aviso")}  {nome}' + (f': {detalhe}' if detalhe else ''))
    if not ok and grave:
        faltas.append(nome)


def saida(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=20).stdout.strip()
    except Exception:
        return ''


print('Para montar (Atelier)')
pc = shutil.which('photocraft-cli')
linha(bool(pc), 'PhotoCraft (photocraft-cli)', saida(['photocraft-cli', '--version']).split(' (')[0] if pc else
      'não instalado. Baixe em https://github.com/storytold/photocraft/releases (Linux: o .tar.gz; Mac: o photocraft-cli-...-macos-universal.zip; '
      'Windows: o ...-windows-x64-portable.zip) e deixe o photocraft-cli no PATH. O instalador do repositório faz isso no Linux')
linha(bool(shutil.which('magick') and shutil.which('montage')), 'ImageMagick 7 (magick e montage)',
      '' if shutil.which('magick') else 'instale: Linux "sudo apt install imagemagick" (ou o pacote da sua distro), Mac "brew install imagemagick"')
try:
    import numpy  # noqa: F401
    import PIL  # noqa: F401
    linha(True, 'numpy e Pillow (recorte de pessoa)')
except ImportError as e:
    linha(False, 'numpy e Pillow (recorte de pessoa)', f'{e}. Instale com: python3 -m pip install --user numpy pillow')
fontes = saida(['fc-list', ':', 'family'])
for f in ('IBM Plex Sans', 'Oswald'):
    linha(f in fontes, f'fonte {f}', '' if f in fontes else
          f'instale os arquivos de {os.path.join(SKILL, "fontes")} (Linux: copie para ~/.local/share/fonts e rode fc-cache -f; '
          'Mac: copie para ~/Library/Fonts)')
os.makedirs(RAIZ, exist_ok=True)
linha(os.path.isdir(RAIZ), f'pasta de trabalho {RAIZ}', '' if 'CARROSSEIS' in os.environ else 'para usar outra pasta, defina a variável CARROSSEIS')
linha(bool(glob.glob(os.path.join(SKILL, 'marca', '*-64.png'))), 'logo da marca (marca/ da skill)')
try:
    livre = int(next(l for l in open('/proc/meminfo') if l.startswith('MemAvailable')).split()[1]) // 1024
    linha(livre >= 2500, 'memória livre', f'{livre} MB' + ('' if livre >= 2500 else ': feche programas antes de montar, senão o PhotoCraft cai'), grave=False)
except Exception:
    pass

print('Imagens (foto, objeto 3D): a skill escreve o pedido e você gera no Gemini ou no ChatGPT (modelos-de-prompt/)')

print()
if faltas:
    print('O ATELIER AINDA NÃO MONTA AQUI. Falta: ' + ', '.join(faltas) + '.')
    print('Enquanto isso dá para fazer roteiro, legenda e pedidos de imagem, e montar à mão no Photoshop ou no Figma (referencias/caminho-b.md).')
    sys.exit(1)
print('ATELIER PRONTO PARA MONTAR.')
