"""Régua do carrossel: desenha a planta por cima dos slides prontos, para conferir no olho se tudo está
no lugar, mostra a rota do olho de cada tipo de slide e emenda todos lado a lado. Os números vêm do planta.py.

  python3 motor/regua.py <pasta-do-carrossel>           sai em <pasta>/planta/: folha-com-regua.jpg, rota-*.jpg e panorama.jpg
  PREVIA=1 python3 motor/regua.py <pasta>               o mesmo, lendo de <pasta>/previa
  python3 motor/regua.py foto <arquivo>                 régua de 50 em 50 px por cima de uma foto, para medir cabelo, queixo e centro
"""
import json
import os
import subprocess
import sys

RAIZ = os.path.abspath(os.path.expanduser(os.environ.get('CARROSSEIS', '~/carrosseis')))


def _altura_do_carrossel():
    """O formato fica gravado em planta.json pelo montar.py: a régua usa a mesma planta."""
    if len(sys.argv) < 2 or sys.argv[1] == 'foto':
        return None
    pasta = sys.argv[1] if os.path.isdir(sys.argv[1]) else os.path.join(RAIZ, sys.argv[1])
    arq = os.path.join(pasta, 'previa' if os.environ.get('PREVIA') else '', 'planta.json')
    if os.path.exists(arq):
        alturas = {f.get('altura', 1440) for f in json.load(open(arq)).values()}
        return str(alturas.pop()) if len(alturas) == 1 else None
    return None


os.environ.setdefault('ALTURA', _altura_do_carrossel() or '1440')

from planta import ALTURA, ATE, CARD_ATE, CABELO_Y, FIO_Y, MARGEM, PALAVRA_BASE, PECA_Y, TARJA_FIM, TARJA_H, TARJA_Y, TEXTO_Y, TITULO_Y

_plex = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'fontes', 'IBMPlexSans[wdth,wght].ttf')
FONTE = ['-font', _plex] if os.path.exists(_plex) else []  # só para os rótulos da régua
ROSA = '#FF2BD6'
CALHA = 400  # faixa à esquerda do slide, onde vai a legenda da rota do olho

# Rota do olho: (altura no slide, rótulo).
ROTAS = {'conteudo': [(TITULO_Y + 22, 'título'), (TARJA_FIM - 28, 'frase em tarja'), ((PECA_Y + ATE) // 2, 'a peça'), (FIO_Y, 'o fio')],
         'sem-texto': [(TITULO_Y + 22, 'título'), ((TEXTO_Y + 48 + ATE) // 2, 'a peça'), (FIO_Y, 'o fio')],
         'card': [(TITULO_Y + 22, 'título'), (TARJA_FIM - 28, 'frase em tarja'), ((PECA_Y + CARD_ATE) // 2, 'a peça')],
         'capa': [(CABELO_Y + 272, 'o rosto'), (PALAVRA_BASE - 370, 'para onde ele olha'), (PALAVRA_BASE - 107, 'a palavra'), (FIO_Y, 'a tarja')],
         'final': [(CABELO_Y + 272, 'o rosto'), (PALAVRA_BASE - 87, 'a palavra'), (FIO_Y, 'a chamada')]}


def tipo(n, fichas, ultimo):
    f = fichas.get(str(n), {})
    if f.get('tipo') == 'card':
        return 'card'
    if f.get('tipo') == 'foto' or (not f and n in (1, ultimo)):
        return 'capa' if n == 1 else 'final'
    return 'conteudo' if f.get('corpo', True) else 'sem-texto'


def guias(t):
    """Linhas-guia do slide: as duas margens e as alturas que se repetem."""
    alturas = ([CABELO_Y, PALAVRA_BASE, TARJA_Y, TARJA_Y + TARJA_H] if t in ('capa', 'final')
               else [TEXTO_Y, PECA_Y, CARD_ATE] if t == 'card'
               else [TEXTO_Y, TEXTO_Y + 48 if t == 'sem-texto' else PECA_Y, ATE, FIO_Y])  # sem texto de apoio a peça sobe
    d = [f'line {x},0 {x},{ALTURA}' for x in (MARGEM, 1080 - MARGEM)] + [f'line 0,{y} 1080,{y}' for y in alturas]
    return ['-fill', 'none', '-stroke', ROSA, '-strokewidth', '2'] + [a for l in d for a in ('-draw', l)]


def cota(x, y0, y1):
    """Marca de medida na margem direita: um traço de y0 a y1 com o tamanho escrito ao lado."""
    return ['-stroke', ROSA, '-strokewidth', '4', '-draw', f'line {x},{y0} {x},{y1}', '-draw', f'line {x - 9},{y0} {x + 9},{y0}',
            '-draw', f'line {x - 9},{y1} {x + 9},{y1}', '-stroke', 'none', '-fill', ROSA] + FONTE + ['-pointsize', '26',
            '-gravity', 'NorthWest', '-annotate', f'+{x + 14}+{(y0 + y1) // 2 - 15}', str(y1 - y0)]


def planta(origem, destino, t):
    """Slide com as linhas-guia e, nos de conteúdo, as medidas dos respiros que se repetem."""
    cmd = ['magick', origem] + guias(t)
    if t not in ('capa', 'final', 'card'):
        cmd += cota(1026, TEXTO_Y, TEXTO_Y + 48) if t == 'sem-texto' else cota(1026, TARJA_FIM, PECA_Y)
        cmd += cota(1026, ATE, FIO_Y)
    subprocess.run(cmd + [destino], check=True)


def rota(origem, destino, t, titulo):
    """Slide com a legenda da rota do olho numa calha à esquerda: por onde o olho entra e por onde sai."""
    passos = ROTAS[t]
    cmd = ['magick', '-size', f'{CALHA + 1080}x{ALTURA}', 'xc:#101216', origem, '-geometry', f'+{CALHA}+0', '-composite']
    cmd += ['-stroke', ROSA, '-strokewidth', '5', '-draw', f'line {CALHA - 60},{passos[0][0]} {CALHA - 60},{passos[-1][0]}']
    cmd += FONTE + ['-gravity', 'NorthWest', '-stroke', 'none', '-fill', '#9AA6B8', '-pointsize', '30', '-annotate', '+36+56', 'Rota do olho',
                    '-fill', '#FFFFFF', '-pointsize', '44', '-annotate', '+36+96', titulo]
    for i, (y, nome) in enumerate(passos, 1):
        cmd += ['-fill', ROSA, '-stroke', '#101216', '-strokewidth', '6', '-draw', f'circle {CALHA - 60},{y} {CALHA - 60},{y - 46}',
                '-stroke', 'none', '-fill', '#FFFFFF', '-pointsize', '44', '-annotate', f'+{CALHA - 84}+{y - 26}', f'{i}º',
                '-pointsize', '38', '-annotate', f'+36+{y - 24}', nome,
                # o mesmo ponto marcado no slide, na margem esquerda
                '-fill', ROSA, '-stroke', '#FFFFFF', '-strokewidth', '4', '-draw', f'circle {CALHA + 40},{y} {CALHA + 40},{y - 26}',
                '-stroke', 'none', '-fill', '#FFFFFF', '-pointsize', '28', '-annotate', f'+{CALHA + 24}+{y - 17}', f'{i}º']
    subprocess.run(cmd + ['-quality', '90', destino], check=True)


def regua_de_foto(arquivo):
    """Foto com uma linha a cada 50 px e o número ao lado: é com isso que se mede cabelo, queixo e centro do rosto."""
    w, h = (int(v) for v in subprocess.run(['magick', 'identify', '-format', '%w %h', arquivo], check=True, capture_output=True, text=True).stdout.split())
    cmd = ['magick', arquivo] + FONTE + ['-pointsize', '18']
    for y in range(50, h, 50):
        cmd += ['-stroke', ROSA, '-strokewidth', '1', '-draw', f'line 0,{y} {w},{y}', '-stroke', 'none', '-fill', ROSA, '-annotate', f'+4+{y - 4}', str(y)]
    for x in range(100, w, 100):
        cmd += ['-stroke', ROSA, '-strokewidth', '1', '-draw', f'line {x},0 {x},{h}', '-stroke', 'none', '-fill', ROSA, '-annotate', f'+{x + 4}+18', str(x)]
    destino = os.path.join(RAIZ, '.cache', os.path.splitext(os.path.basename(arquivo))[0] + '-regua.png')
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    subprocess.run(cmd + [destino], check=True)
    print(destino)


def main():
    if sys.argv[1:2] == ['foto']:
        return regua_de_foto(sys.argv[2])
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    pasta = sys.argv[1] if os.path.isdir(sys.argv[1]) else os.path.join(RAIZ, sys.argv[1])
    base = os.path.join(pasta, 'previa') if os.environ.get('PREVIA') else pasta
    saida = os.path.join(base, 'planta')
    os.makedirs(saida, exist_ok=True)
    nums = sorted(int(f[:2]) for f in os.listdir(os.path.join(base, 'png')) if f.endswith('.png'))
    arq = os.path.join(base, 'planta.json')
    fichas = json.load(open(arq)) if os.path.exists(arq) else {}
    tipos = {n: tipo(n, fichas, nums[-1]) for n in nums}
    for n in nums:
        planta(os.path.join(base, 'png', f'{n:02d}.png'), os.path.join(saida, f'{n:02d}.png'), tipos[n])
    subprocess.run(['montage'] + [os.path.join(saida, f'{n:02d}.png') for n in nums] + ['-resize', '540x', '-tile', f'{min(len(nums), 5)}x', '-geometry', '+10+10',
                   '-background', '#111', '-quality', '90', os.path.join(saida, 'folha-com-regua.jpg')], check=True)
    # Todos os slides emendados, como quem arrasta: é aqui que se vê se o fio e as peças que atravessam casam.
    subprocess.run(['magick'] + [os.path.join(base, 'png', f'{n:02d}.png') for n in nums] + ['+append', '-resize', 'x720', '-quality', '90',
                   os.path.join(saida, 'panorama.jpg')], check=True)
    feitas = set()
    for n in nums:  # uma rota por tipo de slide: capa, o primeiro branco, o primeiro azul e o final
        chave = tipos[n] if tipos[n] in ('capa', 'final', 'card') else ('branco' if n % 2 == 0 else 'azul')
        if chave not in feitas:
            feitas.add(chave)
            titulo = {'capa': 'Capa', 'final': 'Final', 'card': 'Card', 'branco': 'Fundo branco', 'azul': 'Fundo azul'}[chave]
            rota(os.path.join(saida, f'{n:02d}.png'), os.path.join(saida, f'rota-{chave}.jpg'), tipos[n], titulo)
    # as rotas numa imagem só, para mandar de uma vez
    subprocess.run(['montage'] + [os.path.join(saida, f'rota-{c}.jpg') for c in ('capa', 'card', 'branco', 'azul', 'final') if c in feitas]
                   + ['-resize', 'x720', '-tile', 'x1', '-geometry', '+8+8', '-background', '#111', '-quality', '90', os.path.join(saida, 'rotas.jpg')], check=True)
    print(saida)


if __name__ == '__main__':
    main()
