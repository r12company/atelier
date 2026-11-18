"""Ponte fina com o PhotoCraft (photocraft-cli serve): monta slides como PSD com camadas.

Cada função cria UMA camada com nome, como no painel do Photoshop. Quem usa é o comum.py.
A pasta de trabalho é ~/carrosseis (a variável CARROSSEIS troca): o PhotoCraft só lê e grava dentro dela.
"""
import json
import os
import re
import subprocess

from planta import ALTURA

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.abspath(os.path.expanduser(os.environ.get('CARROSSEIS', '~/carrosseis')))
# Um cache por carrossel: com dois sendo montados ao mesmo tempo, um não pega a imagem do outro.
_CARROSSEL = os.path.relpath(os.environ['CARROSSEL'], RAIZ).replace(os.sep, '__') if os.environ.get('CARROSSEL') else 'geral'
CACHE = os.path.join(RAIZ, '.cache', _CARROSSEL)
os.makedirs(CACHE, exist_ok=True)
AZUL, PROFUNDO, GELO, CINZA = '#005DE1', '#0B1423', '#F5F7FB', '#5B6474'
# Tipografia limpa, pedida pelo dono da marca em 15/11/2026 com as capas da V4 como referência:
# IBM Plex Sans em tudo e Oswald (condensada) só na palavra de impacto. Fira Sans, Anton e Sora ficaram para trás.
FONTE = 'IBM Plex Sans'
IMPACTO = 'Oswald'
MENOR_LETRA = 24  # o slide aparece no celular com um terço do tamanho


ESPACO_MAXIMO = 5  # espaçamento entre letras: o dono da marca pediu para tirar o exagerado (15/11/2026)


def conferir_texto(txt, tam, fonte, espaco=0):
    """Regras de texto que não dependem de gosto. O motor recusa na hora, em vez de confiar em quem monta."""
    if espaco > ESPACO_MAXIMO:
        raise ValueError(f'espaçamento entre letras {espaco} em "{txt[:30]}": o dono da marca pediu para tirar o espaçamento exagerado. '
                         f'Use espaco entre -15 e {ESPACO_MAXIMO} (o normal é 0).')
    if re.search('[\u2012-\u2015]', txt):
        raise ValueError(f'travessão em "{txt}": o dono da marca não aceita em lugar nenhum. Use dois-pontos, vírgula ou ponto.')
    if any(ord(c) >= 0x1F000 or 0x2600 <= ord(c) <= 0x27BF for c in txt):
        raise ValueError(f'emoji em "{txt}": slide do Convello não leva emoji.')
    if fonte not in (FONTE, IMPACTO):
        raise ValueError(f'fonte "{fonte}" fora do padrão: só {FONTE} e, na palavra de impacto, {IMPACTO}.')
    if tam < MENOR_LETRA:
        raise ValueError(f'letra de {tam} px em "{txt}": nada abaixo de {MENOR_LETRA} px, senão não se lê no celular.')


class PC:
    def __init__(self):
        os.makedirs(CACHE, exist_ok=True)
        self.p = subprocess.Popen(
            ['photocraft-cli', 'serve', '--automation-read-root', RAIZ, '--automation-write-root', RAIZ],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        self.n = 0

    def chamar(self, metodo, params):
        self.n += 1
        self.p.stdin.write(json.dumps({'id': self.n, 'method': metodo, 'params': params}) + '\n')
        self.p.stdin.flush()
        linha = self.p.stdout.readline()
        if not linha:
            raise RuntimeError('o PhotoCraft fechou no meio da montagem. Quase sempre é falta de memória: rode `free -m`, '
                               'feche programas e monte de novo (um slide de cada vez, se precisar).')
        r = json.loads(linha)
        if not r.get('ok'):
            raise RuntimeError(f'{metodo} {json.dumps(params, ensure_ascii=False)[:300]} -> {r}')
        return r.get('result')

    def ex(self, comando, **params):
        return self.chamar('engine.execute', {'command': comando, 'params': params})

    # ── documento ──
    def novo(self, fundo='#ffffff', nome='slide'):
        self.chamar('doc.new', {'width': 1080, 'height': ALTURA, 'background': fundo, 'name': nome})

    def salvar(self, pasta, nome):
        psd = os.path.join(pasta, 'psd', nome + '.psd')
        png = os.path.join(pasta, 'png', nome + '.png')
        os.makedirs(os.path.dirname(psd), exist_ok=True)
        os.makedirs(os.path.dirname(png), exist_ok=True)
        self.chamar('doc.save', {'path': psd})
        self.chamar('doc.close', {})
        subprocess.run(['photocraft-cli', 'convert', psd, png], check=True, capture_output=True)
        assert tamanho(png) == (1080, ALTURA), f'{png} não saiu em 1080x{ALTURA}'

    def fim(self):
        self.p.stdin.close()
        self.p.wait()

    # ── camadas ──
    def texto(self, nome, txt, x, y, tam, peso=400, cor=PROFUNDO, largura=None, entrelinha=None,
              alinhar='left', destaque=AZUL, espaco=0, fonte=FONTE, negrito=PROFUNDO, dentro=True):
        """Texto. `[assim]` sai na cor de destaque e `**assim**` em negrito.
        Com `largura` vira parágrafo (quebra sozinho, y = topo). Sem, é uma linha (y = linha de base).
        Devolve (id, x0, y0, x1, y1) da tinta."""
        conferir_texto(txt, tam, fonte, espaco)
        limpo, trechos = '', []
        for parte in re.split(r'(\[[^\]]*\]|\*\*[^*]*\*\*)', txt):
            if parte.startswith('['):
                trechos.append((len(limpo), len(limpo) + len(parte) - 2, {'color': destaque}))
                limpo += parte[1:-1]
            elif parte.startswith('**'):
                trechos.append((len(limpo), len(limpo) + len(parte) - 4, {'weight': 700, 'color': negrito}))
                limpo += parte[2:-2]
            else:
                limpo += parte
        p = {'text': limpo, 'name': nome, 'font': fonte, 'size': tam, 'weight': peso, 'color': cor, 'align': alinhar, 'tracking': espaco}
        if entrelinha:
            p['leading'] = entrelinha
        if largura:
            p['box'] = [x, y, largura, 900]
        else:
            p['x'], p['y'] = x, y
        r = self.ex('type.create', **p)
        if trechos:
            r = self.ex('type.edit', layer=r['layer'], runs=[{'start': a, 'end': b, **e} for a, b, e in trechos])
        b = r['bounds']
        # Nenhum texto sai das margens (80 a 1000). `dentro=False` só para texto criado num lugar e movido depois.
        if dentro and (b[0] < 76 or b[2] > 1004):
            raise ValueError(f'o texto "{limpo[:40]}" ({nome}) vai de x={round(b[0])} a {round(b[2])} e sai da margem (80 a 1000): '
                             'encurte, quebre a linha ou diminua o tamanho só se for texto de peça (nunca abaixo de 24).')
        return (r['layer'], b[0], b[1], b[2], b[3])

    def forma(self, nome, tipo, x, y, w, h, cor, raio=0, borda=None, sombra=None):
        p = {'kind': tipo, 'rect': [x, y, w, h], 'fill': cor, 'name': nome}
        if tipo == 'roundedRect':
            p['radii'] = raio
        if borda:
            p['stroke'] = {'width': borda[0], 'color': borda[1], 'align': 'inside'}
        r = self.ex('shape.create', **p)
        if sombra:
            self.ex('layer.layerStyle.dropShadow', **sombra)
        return r['layer']

    def bola(self, nome, cx, cy, d, cor, borda=None, sombra=None):
        return self.forma(nome, 'ellipse', cx - d / 2, cy - d / 2, d, d, cor, borda=borda, sombra=sombra)

    def imagem(self, nome, caminho, cx, cy, prender=False):
        """Põe uma imagem (o arquivo tem de estar dentro da pasta de trabalho). `prender` recorta pela camada de baixo."""
        r = self.chamar('doc.place', {'path': caminho, 'scale': 100, 'center': [cx, cy]})
        self.ex('layer.renameLayer', name=nome)
        if prender:
            self.ex('layer.createClippingMask')
        return r['layer']

    def opacidade(self, ids, valor):
        self.ex('layer.setProps', layers=list(ids), opacity=valor)

    def abaixo_de(self, camada, alvo):
        self.ex('layer.moveTo', layer=camada, target=alvo, position='below')


def recorte(origem, w, h, nome, de_cima=True, gravidade=None):
    """Deixa a imagem com exatamente w x h (preenche e corta), em cache."""
    os.makedirs(CACHE, exist_ok=True)
    destino = os.path.join(CACHE, nome + '.png')
    subprocess.run(['magick', origem, '-resize', f'{int(w)}x{int(h)}^', '-gravity', gravidade or ('NorthWest' if de_cima else 'Center'),
                    '-extent', f'{int(w)}x{int(h)}', destino], check=True)
    return destino


def tamanho(png):
    w, h = subprocess.run(['magick', 'identify', '-format', '%w %h', png], check=True, capture_output=True, text=True).stdout.split()
    return int(w), int(h)


def svg_png(origem, altura, nome, branco=False):
    """SVG para PNG na altura pedida, em cache: só refaz se o SVG mudou.
    A densidade sai do tamanho do desenho (4x a altura final). Com densidade fixa de 600 a logo
    virava uma imagem de 200 megapixels, gastava 2 GB por montagem e travava o PhotoCraft."""
    os.makedirs(CACHE, exist_ok=True)
    destino = os.path.join(CACHE, nome + '.png')
    if os.path.exists(destino) and os.path.getmtime(destino) >= os.path.getmtime(origem):
        return destino
    vb = re.search(r'viewBox="[\d.\-]+[ ,]+[\d.\-]+[ ,]+[\d.]+[ ,]+([\d.]+)"', open(origem, encoding='utf-8', errors='ignore').read(20000))
    densidade = max(24, min(2400, round(96 * 4 * altura / float(vb.group(1))))) if vb else 300
    cmd = ['magick', '-background', 'none', '-density', str(densidade), origem, '-resize', f'x{altura}']
    if branco:
        cmd += ['-fill', 'white', '-colorize', '100']
    subprocess.run(cmd + [destino], check=True)
    return destino
