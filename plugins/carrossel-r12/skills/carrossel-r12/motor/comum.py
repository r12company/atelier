"""Peças fixas do carrossel do Convello, montado no PhotoCraft. Não se roda sozinho: quem chama é o montar.py.

Slide de foto (capa e final):   abrir_foto(n) -> foto_de_pessoa(...) -> topo('branco', arroba=False)
                                -> titulo_de_foto(linha, PALAVRA, tam) -> tarja_da_capa(...) ou chamada(...) -> fechar(n)
Slide de conteúdo (os do meio): abrir(n) -> manchete([...]) -> corpo([...]) -> A PEÇA (de PECA_Y a ATE) -> fio(pergunta) -> fechar(n)

Os fundos se intercalam (capa, branco, azul, branco, azul...) e as peças invertem junto:

  fundo branco -> texto escuro, destaque azul (ou vermelho), tarja colorida com letra branca, PEÇAS ESCURAS
  fundo azul   -> texto branco, destaque em tarja branca com letra azul, PEÇAS CLARAS
  (print do sistema leva moldura branca fina nos dois: é ela que separa a tela escura do fundo)

O que este arquivo já garante sozinho (dá erro e explica, em vez de deixar passar):
  fundo par branco e ímpar azul; todo slide de conteúdo com o fio; todo slide com a logo; capa e final de foto;
  linha de título, de texto e do fio dentro das margens; palavra sozinha numa linha do texto; e, no pc.py,
  travessão, emoji, fonte fora do padrão e letra menor que 24 px.

O que continua sendo julgamento de quem monta está em referencias/ (arquitetura-visual.md e reprovado.md).
A planta (onde fica cada coisa) está no planta.py. Para conferir o resultado com a régua por cima: regua.py.
"""
import json
import os
import subprocess
import time

from pc import AZUL, CACHE, CINZA, IMPACTO, PC, PROFUNDO, RAIZ, SKILL, recorte, svg_png, tamanho  # noqa: F401 (svg_png: para quem monta usar)
from planta import (ALTURA, ATE, CARD_ATE, STORIES, CABELO_Y, ESCURECE_DE, FIO_Y, LOGO_Y, MARGEM, MIOLO, MOLDURA, PALAVRA_BASE, PECA_Y, ROSTO, TARJA_FIM, TARJA_H,
                    TARJA_Y, TEXTO_Y, TITULO_PASSO, TITULO_Y, T_CORPO, T_FIO, T_TITULO)
from silhueta import recortar_pessoa

if 'CARROSSEL' not in os.environ:
    raise SystemExit('Rode pelo montar.py: python3 motor/montar.py <pasta-do-carrossel> [slides]')
PASTA = os.environ['CARROSSEL']
SAIDA = os.path.join(PASTA, 'previa') if os.environ.get('PREVIA') else PASTA
MARCA = os.path.join(SKILL, 'marca')
REC = os.path.join(PASTA, 'recortes')
DIREITA = 1080 - MARGEM
ARROBA = '@r12_company'  # Instagram da R12 (no PDF de venda é r12company.com)
BRANCO = '#ffffff'
VERMELHO = '#D92D34'
TEXTO = '#2f3d33'
ESCURO = '#1C1C1F'   # cor de fundo das telas do Convello no tema escuro
SOMBRA = {'color': '#0b120d', 'opacity': 30, 'angle': 90, 'distance': 20, 'size': 50}

import shutil
LOGO = shutil.copy(f'{MARCA}/r12-logo-64.png', CACHE)
LOGO_BRANCA = shutil.copy(f'{MARCA}/r12-logo-branca-64.png', CACHE)

TEMAS = {
    'branco': dict(nome='branco', tit=PROFUNDO, texto=TEXTO, dest='#3f7a0f', tarja=PROFUNDO, tarja_texto=AZUL, fio=PROFUNDO, fio_seta=AZUL),
    'azul': dict(nome='azul', tit='#e7ffef', texto='#cfe3d4', dest=AZUL, tarja=AZUL, tarja_texto=PROFUNDO, fio=AZUL, fio_seta=PROFUNDO),
    # Fundo marinho (Azul Profundo): letra branca, destaque azul claro, tarja azul Convello. Peça clara ou print com moldura.
    'escuro': dict(nome='escuro', tit=BRANCO, texto='#C9D3E3', dest='#5AA2FF', tarja=AZUL, tarja_texto=BRANCO, fio='#5AA2FF', fio_seta=BRANCO),
    # Foto no slide todo, escurecida onde vai o texto: mesmas cores do escuro.
    'foto': dict(nome='foto', tit=BRANCO, texto='#E3E8F0', dest='#5AA2FF', tarja=AZUL, tarja_texto=BRANCO, fio=BRANCO, fio_seta=AZUL),
}

pc = PC()
T = dict(TEMAS['branco'])  # tema do slide aberto
FICHA = {}                 # o que o slide aberto já tem; o fechar() confere
FEITOS = {}                # ficha de cada slide montado nesta rodada
AVISOS = []


def tema():
    return T


def _de_pe(caminho):
    """Foto de celular guarda a rotação à parte (EXIF): sem desvirar, o PhotoCraft a põe deitada. Devolve uma cópia já
    desvirada quando precisa; foto sem rotação volta como está."""
    giro = subprocess.run(['magick', 'identify', '-format', '%[orientation]', caminho + '[0]'], capture_output=True, text=True).stdout.strip()
    if giro in ('', 'Undefined', 'TopLeft'):
        return caminho
    destino = os.path.join(CACHE, 'de-pe-' + os.path.basename(caminho))
    if not (os.path.exists(destino) and os.path.getmtime(destino) >= os.path.getmtime(caminho)):
        subprocess.run(['magick', caminho, '-auto-orient', destino], check=True)
    return destino


def achar(arquivo):
    """Foto, ícone ou objeto 3D: procura na pasta do carrossel (geradas/) e depois no acervo aprovado
    (~/carrosseis/geradas)."""
    nome = os.path.basename(arquivo)
    pastas = [os.path.join(PASTA, p) for p in ('geradas', 'fotos', 'recortes')] + [os.path.join(RAIZ, 'geradas')]
    for p in pastas:
        if os.path.exists(os.path.join(p, nome)):
            return _de_pe(os.path.join(p, nome))
    raise FileNotFoundError(f'{nome} não está em {", ".join(pastas)}. Gere com o gerar_imagem.py ou baixe a foto para fotos/.')


def cabe(nome, x1, limite=DIREITA):
    """Nada de texto passa da margem direita."""
    if x1 > limite + 4:
        raise ValueError(f'{nome} passa da margem direita em {round(x1 - limite)} px: encurte a linha ou quebre em outro ponto.')


def grao(nome, quanto, preso=True):
    """Textura de grão por cima da última camada (presa a ela) ou do slide todo."""
    pc.ex('layer.new.layer', name=nome, clipToPrevious=preso, mode='Overlay', fillNeutral=True)
    pc.ex('filter.noise.addNoise', amount=quanto, distribution='gaussian', monochromatic=True)


def abrir(n, qual=None, destaque=None, foto=None, foco_x=0.5, foco_y=0.4, zoom=1.0, escurecer='baixo', logo=None,
          foto_no_topo=None, foto_ate=620, card=False):
    """Abre um slide de conteúdo com o fundo, a logo e o arroba.
    `qual`: 'claro' (o mesmo que 'branco': quase branco) ou 'escuro' (o mesmo que 'azul': o #161616 com toque de verde;
    o nome 'azul' ficou do motor do Convello). Sem `qual`, o padrão: par claro, ímpar escuro. O contraste continua
    valendo: peça escura no claro, peça clara no escuro.
    `logo`: 'escura' ou 'branca' (padrão: escura no claro, branca no escuro).
    `destaque=VERMELHO` troca o verde de destaque nos slides do problema (só faz efeito no claro).
    `foto_no_topo=arquivo`: a foto ocupa a faixa de cima, de ponta a ponta, até `foto_ate`; a logo vai branca por cima
    dela e o texto começa embaixo (molde "metade foto"). `foco_x`, `foco_y` e `zoom` escolhem o pedaço da foto.
    `card=True`: post único (uma imagem só, SLIDES = {1: s1}). Sem fio; a peça pode descer até CARD_ATE."""
    global T, FICHA
    if card and n != 1:
        raise ValueError('card é uma imagem só: abrir(1, card=True) e SLIDES = {1: s1}.')
    if n < 2 and not card:
        raise ValueError('o slide 1 é a capa: use abrir_foto (ou abrir(1, card=True) para um card).')
    qual = qual or ('branco' if card or n % 2 == 0 else 'azul')
    qual = {'claro': 'branco', 'escuro': 'azul'}.get(qual, qual)
    if qual == 'foto':
        raise ValueError(f'fundo "{qual}" reprovado pelo dono da marca em 15/11 ("poluído, parece site"): slide de conteúdo é claro ou escuro.')
    if qual not in TEMAS:
        raise ValueError(f'fundo "{qual}" não existe: use claro (ou branco) ou escuro (ou azul).')
    if qual == 'foto' and not foto:
        raise ValueError("abrir(n, 'foto') precisa de foto=arquivo.")
    T = dict(TEMAS[qual])
    if destaque and qual == 'branco':
        T['dest'] = T['tarja'] = destaque
    FICHA = dict(n=n, tipo='card' if card else 'conteudo', tema=qual, logo=False, corpo=False, altura=ALTURA)
    if not card:
        FICHA['fio'] = False
    pc.novo(BRANCO, f'slide-{n:02d}')
    if qual == 'foto':
        foto_inteira(foto, foco_x, foco_y, zoom, escurecer=escurecer)
    elif qual == 'escuro':
        pc.forma('FUNDO', 'rect', 0, 0, 1080, ALTURA, {'gradient': {
            'stops': [[0, '#16294A'], [0.45, '#0F1D36'], [1, '#070E1B']], 'style': 'radial', 'scale': 150, 'offset': [0, 0.1]}})
        grao('FUNDO-GRAO', 7, preso=False)
    elif qual == 'branco':
        pc.forma('FUNDO', 'rect', 0, 0, 1080, ALTURA, {'gradient': {'stops': [[0, '#FBFCFB'], [0.45, '#F2F5F2'], [1, '#E0E6E1']], 'angle': -62}})
        grao('FUNDO-GRAO', 3)
    else:
        # azul um pouco mais fraco perto do meio (atrás da peça) e mais firme nas bordas, sem chegar no marinho.
        # Calibrado em duas reprovações do dono da marca: chapado com canto marinho ficou "muito azul";
        # com o meio em #62A8FF ficou "muito branco". O texto fica na parte mais firme, onde o branco contrasta.
        pc.forma('FUNDO', 'rect', 0, 0, 1080, ALTURA, {'gradient': {
            'stops': [[0, '#1F2A1F'], [0.3, '#1B201B'], [0.6, '#171917'], [1, '#131313']],
            'style': 'radial', 'scale': 140, 'offset': [0, 0.15]}})
        grao('FUNDO-GRAO', 8, preso=False)
    if foto_no_topo:
        faixa_de_foto(foto_no_topo, foto_ate, foco_x, foco_y, zoom)
        logo = logo or 'branca'
    topo('branco' if (logo or ('escura' if qual == 'branco' else 'branca')) == 'escura' else 'azul')


def abrir_foto(n):
    """Abre um slide de foto (a capa e o final). Depois vêm foto_de_pessoa, topo, titulo_de_foto e a tarja ou a chamada."""
    global T, FICHA
    T = dict(TEMAS['branco'])
    FICHA = dict(n=n, tipo='foto', logo=False, titulo=False, fecho=False, altura=ALTURA)
    pc.novo('#E9EAEC', f'slide-{n:02d}')


def topo(qual='branco', arroba=True):
    """Logo e arroba. `qual` é a cor do que está atrás do topo: 'branco' (ou foto clara) para a logo escura;
    'azul', 'escuro' ou 'foto' (foto escura) para a logo branca."""
    azul = qual in ('azul', 'escuro', 'foto')
    pc.imagem('LOGO', LOGO_BRANCA if azul else LOGO, MARGEM + 335 / 2, LOGO_Y)
    if arroba:
        pc.texto('ARROBA', ARROBA, DIREITA, LOGO_Y + 9, 27, 500, '#e7ffef' if azul else CINZA, alinhar='right')
    FICHA['logo'] = True


def _centralizar(tt, w, centro, recuo=0):
    """Linha centralizada: move a tinta para o meio e devolve o x0 da caixa de largura w (com recuo por dentro)."""
    x0 = round(centro - w / 2)
    pc.ex('type.edit', layer=tt[0], move=[x0 + recuo - tt[1], 0])
    return x0


def manchete(linhas, y=TITULO_Y, tam=82, x=MARGEM, alinhar='left', centro=540, limite=DIREITA):
    """Título, uma camada por linha (a quebra é escolhida à mão). Uma, duas ou três linhas.
    Linha começando com '!' é o destaque: cor de destaque no branco e no escuro, tarja branca com letra azul no azul.
    `[trecho]` destaca só o trecho. `tam` 64 é a manchete de sempre; 88 a 120 vira frase de impacto (slide tipográfico).
    `alinhar='center'` centraliza em `centro`; `x` e `limite` estreitam a coluna (layout dividido).
    Devolve onde o título acaba (TEXTO_Y para o título de sempre, de duas linhas)."""
    passo = round(tam * 1.12)  # título em Oswald (a letra da capa): mais alto e mais junto
    for i, t in enumerate(linhas):
        base = y + i * passo
        if t.startswith('!') and T['nome'] == 'azul':
            pad, alto = round(tam * 0.3125), round(tam * 1.1875)
            tt = pc.texto(f'TITULO-{i + 1}', t[1:], x + pad, base, tam, 600, PROFUNDO, fonte=IMPACTO, dentro=False)
            w = (tt[3] - tt[1]) + 2 * pad
            x0 = _centralizar(tt, w, centro, pad) if alinhar == 'center' else x
            f = pc.forma(f'TITULO-{i + 1}-TARJA', 'roundedRect', x0, base - round(tam * 0.9375), w, alto, AZUL, round(tam * 0.16))
            pc.abaixo_de(f, tt[0])
            pc.ex('layer.select', layer=tt[0])
            fim_x, ini_x = x0 + w, x0
        else:
            cor = T['dest'] if t.startswith('!') else T['tit']
            tt = pc.texto(f'TITULO-{i + 1}', t.lstrip('!'), x, base, tam, 600, cor, destaque=T['dest'], fonte=IMPACTO, dentro=False)
            x0 = _centralizar(tt, tt[3] - tt[1], centro) if alinhar == 'center' else tt[1]
            fim_x, ini_x = x0 + (tt[3] - tt[1]), x0
        cabe(f'a linha {i + 1} do título ("{t.lstrip("!")}")', fim_x, limite)
        if ini_x < MARGEM - 4:
            raise ValueError(f'a linha {i + 1} do título ("{t.lstrip("!")}") passa da margem esquerda: encurte.')
    return y + round(tam * 0.3) + passo * (len(linhas) - 1)


def corpo(linhas, y=TEXTO_Y, tam=T_CORPO, passo=48, x=MARGEM, alinhar='left', centro=540, limite=DIREITA):
    """Texto de apoio, uma camada por linha. Linha começando com '!' vira a frase em tarja.
    Com duas linhas e a tarja, a tarja termina em TARJA_FIM e a peça começa em PECA_Y (64 px depois).
    `alinhar`, `centro`, `x` e `limite` como na manchete. Devolve onde o texto acaba."""
    base, fim = y + 52, y
    for i, t in enumerate(linhas):
        if len(t.lstrip('!').split()) < 2:
            raise ValueError(f'palavra sozinha na linha {i + 1} do texto ("{t}"): quebre de outro jeito.')
        if t.startswith('!'):
            cima = base - passo + 24 if i else base - 40
            tt = pc.texto(f'TEXTO-{i + 1}', t[1:], x + 16, cima + 40, tam, 700, T['tarja_texto'], dentro=False)
            w = (tt[3] - tt[1]) + 32
            x0 = _centralizar(tt, w, centro, 16) if alinhar == 'center' else x
            f = pc.forma(f'TEXTO-{i + 1}-TARJA', 'roundedRect', x0, cima, w, 56, T['tarja'], 8)
            pc.abaixo_de(f, tt[0])
            pc.ex('layer.select', layer=tt[0])
            cabe(f'a frase em tarja ("{t[1:]}")', x0 + w, limite)
            base, fim = cima + 40 + passo, cima + 56
        else:
            tt = pc.texto(f'TEXTO-{i + 1}', t, x, base, tam, 400, T['texto'], dentro=False)
            x0 = _centralizar(tt, tt[3] - tt[1], centro) if alinhar == 'center' else tt[1]
            cabe(f'a linha {i + 1} do texto ("{t}")', x0 + (tt[3] - tt[1]), limite)
            base, fim = base + passo, base + 12
    FICHA['corpo'] = True
    return fim


def seta(nome, cx, cy, cor, para='direita', tam=14):
    """Seta fina desenhada (não é letra): haste e ponta com as pontas arredondadas."""
    if para == 'direita':
        haste, ponta = [[cx - tam, cy], [cx + tam, cy]], [[cx + tam - 10, cy - 10], [cx + tam, cy], [cx + tam - 10, cy + 10]]
    else:
        haste, ponta = [[cx, cy - tam], [cx, cy + tam]], [[cx - 10, cy + tam - 10], [cx, cy + tam], [cx + 10, cy + tam - 10]]
    pc.ex('shape.create', kind='path', name=nome, fill=None,
          path={'subpaths': [{'closed': False, 'knots': haste}, {'closed': False, 'knots': ponta}]},
          stroke={'width': 4, 'color': cor, 'align': 'center', 'cap': 'round', 'join': 'round'})


def linha_fina(nome, *tracos, cor=BRANCO):
    """Linha fina (3 px) numa camada só, para apontar de um rótulo até um ponto do print. Cada traço é uma lista
    de pontos: reta, cotovelo ou chave. Linha em pé com x terminado em .5 (e deitada com y em .5) sai nítida."""
    pc.ex('shape.create', kind='path', name=nome, fill=None,
          path={'subpaths': [{'closed': False, 'knots': [list(p) for p in t]} for t in tracos]},
          stroke={'width': 3, 'color': cor, 'align': 'center', 'cap': 'butt', 'join': 'miter'})


def fio(pergunta, primeiro=False):
    """Rodapé do Convello: o FIO. Uma linha fina corre de ponta a ponta na mesma altura em todos os slides,
    como o fio de uma conversa. A pergunta que puxa o próximo slide assenta no fio, à esquerda, e ele termina
    num botão redondo no canto de baixo à direita, que é onde a leitura acaba e o dedo começa a arrastar.
    O fio sai pela beirada direita e entra pela esquerda do slide seguinte.
    `primeiro=True` no slide logo depois da capa: lá o fio começa, não vem de trás."""
    y, cor = FIO_Y, T['fio']
    t = pc.texto('FIO-PERGUNTA', pergunta, MARGEM, y + 12, T_FIO, 600, T['tit'])
    bx = DIREITA - 36  # meio do botão: ele encosta na margem direita
    if (bx - 36) - (t[3] + 24) < 120:
        raise ValueError(f'a pergunta do fio ("{pergunta}") é comprida demais: tem de sobrar linha até o botão. Até uns 30 caracteres.')
    if not primeiro:
        pc.forma('FIO-ENTRADA', 'rect', 0, y - 1, MARGEM - 24, 3, cor)
    pc.forma('FIO-LINHA', 'rect', t[3] + 24, y - 1, (bx - 36) - (t[3] + 24), 3, cor)
    pc.forma('FIO-SAIDA', 'rect', bx + 36, y - 1, 1080 - (bx + 36), 3, cor)
    pc.bola('FIO-BOTAO', bx, y, 72, cor)
    seta('FIO-SETA', bx, y, T['fio_seta'])
    FICHA['fio'] = True


def print_do_sistema(origem, nome, y=PECA_Y, ate=ATE, x=MARGEM, w=920, gravidade=None, prefixo='PRINT'):
    """Print real do Convello (tela escura), com moldura branca fina nos dois temas.
    `origem` é o recorte já no formato da caixa (nome solto = arquivo em recortes/ do carrossel).
    A caixa (x, y, w, ate) é a borda DE FORA da moldura: é ela que assenta nas guias da planta.
    A imagem ocupa a caixa inteira e a moldura cobre a beirada dela, então o print fica no mesmo lugar
    com ou sem moldura (é o que faz ele casar quando continua no slide vizinho).
    `x` negativo ou `x + w` acima de 1080 faz o print sair pela lateral."""
    if not os.path.isabs(origem):
        origem = os.path.join(REC, origem)
    dias = (time.time() - os.path.getmtime(origem)) / 86400
    if dias > 30:
        AVISOS.append(f'{os.path.basename(origem)} é um print de {round(dias)} dias atrás: confira se a tela ainda é assim (senão, tire de novo).')
    h = ate - y
    pc.forma(f'{prefixo}-MOLDURA', 'roundedRect', x, y, w, h, BRANCO, 30, sombra=SOMBRA)
    pc.forma(f'{prefixo}-FUNDO', 'roundedRect', x + MOLDURA, y + MOLDURA, w - 2 * MOLDURA, h - 2 * MOLDURA, ESCURO, 22)
    pc.imagem(prefixo, recorte(origem, w, h, nome, gravidade=gravidade), x + w / 2, y + h / 2, prender=True)


def objeto(nome, arquivo, cx, cy, lado, giro=0):
    """Objeto 3D solto (gerado sobre fundo branco): tira o fundo, deixa transparente e põe com sombra.
    Serve para a emenda entre slides (o mesmo objeto com cx=1080 num slide e cx=0 no seguinte) e para pôr
    atrás da pessoa numa foto."""
    origem = achar(arquivo)
    destino = os.path.join(CACHE, f'{os.path.splitext(os.path.basename(arquivo))[0]}-{lado}-{giro}.png')
    if not (os.path.exists(destino) and os.path.getmtime(destino) >= os.path.getmtime(origem)):
        # Tira o branco de fora para dentro, come 3 px da borda (a franja clara) e SÓ DEPOIS apara a sobra.
        # Aparando antes, os pontos que encostavam na borda do recorte não eram comidos e sobrava um
        # tracinho claro de cada lado do objeto (o dono da marca viu a falha no ícone do WhatsApp).
        # Margem de 20 px antes de tirar o fundo: objeto rente à borda da imagem deixava pontinhos brancos.
        subprocess.run(['magick', origem, '-alpha', 'set', '-bordercolor', 'white', '-border', '20',
                        '-fuzz', '7%', '-fill', 'none', '-draw', 'alpha 0,0 floodfill', '-shave', '20x20',
                        '(', '+clone', '-alpha', 'extract', '-morphology', 'Erode', 'Disk:3', '-blur', '0x1', ')',
                        '-compose', 'CopyOpacity', '-composite', '-trim', '+repage', '-background', 'none', '-rotate', str(giro),
                        '-filter', 'Lanczos', '-resize', f'{lado}x{lado}', destino], check=True)
    c = pc.imagem(nome, destino, cx, cy)
    pc.ex('layer.layerStyle.dropShadow', color='#0b120d', opacity=38, angle=90, distance=14, size=26)
    return c


def icone(nome, arquivo, cx, cy, lado):
    """Ícone 3D da marca (gerado sobre branco). Entra em modo multiplicar: só usar em cima de fundo branco
    (o fundo branco do slide ou um painel branco)."""
    destino = os.path.join(CACHE, f'{FICHA.get("n", 0):02d}-{nome.lower()}.png')
    # O Gemini entrega o fundo em 254 com ruído, não 255: em modo multiplicar aparecia um quadrado cinza fraco.
    # Pinta de branco puro só o fundo ligado à borda (o branco de dentro do ícone fica).
    subprocess.run(['magick', achar(arquivo), '-bordercolor', 'white', '-border', '20', '-fuzz', '4%', '-fill', 'white',
                    '-draw', 'color 0,0 floodfill', '-shave', '20x20', '-filter', 'Lanczos', '-resize', f'{lado}x{lado}', destino], check=True)
    c = pc.imagem(nome, destino, cx, cy)
    pc.ex('layer.setProps', layer=c, blend='Multiply')


def escurecer_foto(onde='baixo'):
    """Escurece a foto onde vai o texto: 'baixo' (padrão da capa), 'cima', 'tudo' ou 'nenhum'."""
    if onde == 'nenhum':
        return
    if onde == 'tudo':
        c = pc.forma('ESCURECER', 'rect', 0, 0, 1080, ALTURA, '#0b120d')
        pc.opacidade([c], 0.58)
    elif onde == 'cima':
        pc.forma('ESCURECER', 'rect', 0, 0, 1080, ALTURA - ESCURECE_DE + 120,
                 {'gradient': {'stops': [[0, '#0b120d'], [1, '#0b120d']], 'opacityStops': [[0, 0], [0.42, 0.82], [1, 0.97]], 'angle': 90}})
    else:
        pc.forma('ESCURECER', 'rect', 0, ESCURECE_DE, 1080, ALTURA - ESCURECE_DE,
                 {'gradient': {'stops': [[0, '#0b120d'], [1, '#0b120d']], 'opacityStops': [[0, 0], [0.42, 0.82], [1, 0.97]], 'angle': -90}})


def _logo_fora_do_cabelo(pessoa, arquivo):
    """Logo em cima do cabelo é proibido (referencias/material.md): a caixa da logo não pode tocar a pessoa."""
    x0, x1, y0, y1 = MARGEM, MARGEM + 335, LOGO_Y - 32, LOGO_Y + 32  # a logo da R12 tem 335 de largura
    alfa = subprocess.run(['magick', pessoa, '-alpha', 'extract', '-crop', f'{x1 - x0}x{y1 - y0}+{x0}+{y0}', '+repage', '-threshold', '50%',
                           '-format', '%[fx:mean]', 'info:'], capture_output=True, text=True, check=True).stdout
    if float(alfa) > 0.002:
        raise ValueError(f'{os.path.basename(arquivo)}: a pessoa encosta na logo (caixa x {x0} a {x1}, y {y0} a {y1}) e a logo ficaria em cima '
                         'do cabelo. Meça de novo o alto do cabelo com a régua de foto, diminua o rosto ou leve o rosto para a direita (rosto_x).')


def foto_de_pessoa(arquivo, cabelo, queixo, centro, atras=None, rosto_x=540, rosto=ROSTO, escurecer='baixo'):
    """Foto de pessoa ocupando o slide todo: rosto com ROSTO de altura, cabelo começando em CABELO_Y e rosto
    no meio do slide. `cabelo`, `queixo` (alturas) e `centro` (posição do rosto na largura) são medidos na
    foto original, em px: `python3 motor/regua.py foto <arquivo>`.

    Cada carrossel muda a composição: `rosto_x` põe o rosto mais para a esquerda ou para a direita (de 330 a 750),
    abrindo espaço para um objeto grande do outro lado, e `rosto` muda o tamanho da pessoa (de 400 a 600).
    O que não muda: o rosto fica na metade de cima e o título embaixo.

    `atras` é uma função que desenha objetos (ícone, logo) ATRÁS da pessoa: a foto fica embaixo, os objetos no
    meio e o recorte da pessoa por cima, no mesmo lugar. É o jeito certo de pôr ícone em foto: grande e meio
    escondido pela pessoa, com profundidade, e não boiando na frente. Precisa de foto em parede lisa."""
    origem = achar(arquivo)
    nome = f'{FICHA.get("n", 0):02d}-{os.path.splitext(os.path.basename(arquivo))[0]}'
    w0, h0 = tamanho(origem)
    if not (330 <= rosto_x <= 750 and 400 <= rosto <= 600):
        raise ValueError(f'rosto_x={rosto_x} ou rosto={rosto} fora da faixa: o rosto fica entre 330 e 750 na largura e tem de 400 a 600 de altura.')
    s = rosto / (queixo - cabelo)
    largura, dx, dy = round(w0 * s), round(centro * s - rosto_x), round(cabelo * s - CABELO_Y)
    assert 0 <= dx and dx + 1080 <= w0 * s and 0 <= dy and dy + ALTURA <= h0 * s, \
        f'{arquivo}: a foto não cobre o slide nesse enquadramento (confira as medidas com a régua de foto; se a pessoa está muito para um lado, aproxime rosto_x do meio ou gere a foto com mais parede em volta)'
    enquadrar = ['-filter', 'Lanczos', '-resize', f'{largura}x', '-crop', f'1080x{ALTURA}+{dx}+{dy}', '+repage']
    nitidez = ['-channel', 'RGB', '-unsharp', '0x0.8+0.6+0.02', '+channel']
    destino = os.path.join(CACHE, nome + '.png')
    subprocess.run(['magick', origem] + enquadrar + nitidez + [destino], check=True)
    pc.imagem('FOTO', destino, 540, ALTURA / 2)
    solta, pessoa = os.path.join(CACHE, nome + '-solta.png'), os.path.join(CACHE, nome + '-pessoa.png')
    try:
        recortar_pessoa(origem, solta, (centro, (cabelo + queixo) // 2))
        subprocess.run(['magick', solta] + enquadrar + nitidez + [pessoa], check=True)
    except ValueError:
        if atras:
            raise
        AVISOS.append(f'{os.path.basename(arquivo)}: não deu para recortar a pessoa, então ninguém conferiu se a logo encosta no cabelo. Olhe o slide.')
    else:
        _logo_fora_do_cabelo(pessoa, arquivo)
    if atras:
        atras()
        pc.imagem('PESSOA', pessoa, 540, ALTURA / 2)
    escurecer_foto(escurecer)
    grao('GRAO', 9, preso=False)


def foto_inteira(arquivo, foco_x=0.5, foco_y=0.4, zoom=1.0, escurecer='baixo'):
    """Foto que ocupa o slide todo sem ser retrato de estúdio: prédio, produto, evento, foto de agência.
    Preenche 1080 x ALTURA e corta em volta do ponto de foco (`foco_x`, `foco_y`: frações da foto, 0 a 1).
    `zoom` acima de 1 aproxima. Escurece embaixo como a foto de pessoa, para o título aparecer."""
    origem = achar(arquivo)
    w0, h0 = tamanho(origem)
    s = max(1080 / w0, ALTURA / h0) * zoom
    if s > 1.6:
        AVISOS.append(f'{os.path.basename(arquivo)} foi ampliada {s:.1f} vezes: confira se não ficou borrada.')
    largura, altura = round(w0 * s), round(h0 * s)
    dx = min(max(round(foco_x * largura - 540), 0), largura - 1080)
    dy = min(max(round(foco_y * altura - ALTURA / 2), 0), altura - ALTURA)
    destino = os.path.join(CACHE, f'{FICHA.get("n", 0):02d}-inteira-{os.path.splitext(os.path.basename(arquivo))[0]}.png')
    subprocess.run(['magick', origem, '-filter', 'Lanczos', '-resize', f'{largura}x{altura}!', '-crop', f'1080x{ALTURA}+{dx}+{dy}', '+repage',
                    '-channel', 'RGB', '-unsharp', '0x0.8+0.6+0.02', '+channel', destino], check=True)
    pc.imagem('FOTO', destino, 540, ALTURA / 2)
    escurecer_foto(escurecer)
    grao('GRAO', 9, preso=False)


def faixa_de_foto(arquivo, ate=620, foco_x=0.5, foco_y=0.4, zoom=1.0):
    """Foto de ponta a ponta no alto do slide (de 0 até `ate`), com um véu escuro só no topo para a logo branca aparecer."""
    origem = achar(arquivo)
    w0, h0 = tamanho(origem)
    s = max(1080 / w0, ate / h0) * zoom
    largura, altura = round(w0 * s), round(h0 * s)
    dx = min(max(round(foco_x * largura - 540), 0), largura - 1080)
    dy = min(max(round(foco_y * altura - ate / 2), 0), altura - ate)
    destino = os.path.join(CACHE, f'{FICHA.get("n", 0):02d}-faixa-{os.path.splitext(os.path.basename(arquivo))[0]}.png')
    subprocess.run(['magick', origem, '-filter', 'Lanczos', '-resize', f'{largura}x{altura}!', '-crop', f'1080x{ate}+{dx}+{dy}', '+repage',
                    '-channel', 'RGB', '-unsharp', '0x0.8+0.6+0.02', '+channel', destino], check=True)
    pc.imagem('FOTO-TOPO', destino, 540, ate / 2)
    pc.forma('FOTO-TOPO-VEU', 'rect', 0, 0, 1080, 220,
             {'gradient': {'stops': [[0, '#0b120d'], [1, '#0b120d']], 'opacityStops': [[0, 0.55], [1, 0]], 'angle': -90}})
    if s > 1.6:
        AVISOS.append(f'{os.path.basename(arquivo)} foi ampliada {s:.1f} vezes na faixa: confira se não ficou borrada.')


def pessoa_solta(arquivo, cabelo, queixo, centro, cx, cabelo_y, rosto=440, nome='PESSOA-SOLTA'):
    """Pessoa recortada (foto de estúdio em parede lisa) posta em qualquer lugar do slide, podendo sair pela borda,
    como a V4 faz: rosto no ponto `cx` (largura) com o cabelo começando em `cabelo_y`, e `rosto` de altura.
    A foto tem de chegar até a borda de baixo do slide (senão a cintura fica cortada no ar). Texto ao lado, nunca por cima."""
    origem = achar(arquivo)
    base = os.path.join(CACHE, f'{FICHA.get("n", 0):02d}-{os.path.splitext(os.path.basename(arquivo))[0]}')
    solta = base + '-solta-inteira.png'
    recortar_pessoa(origem, solta, (centro, (cabelo + queixo) // 2))
    w0, h0 = tamanho(origem)
    s = rosto / (queixo - cabelo)
    destino = base + f'-solta-{rosto}.png'
    subprocess.run(['magick', solta, '-filter', 'Lanczos', '-resize', f'{round(w0 * s)}x', destino], check=True)
    w, h = tamanho(destino)
    x0, y0 = cx - centro * s, cabelo_y - cabelo * s
    if y0 + h < ALTURA - 2:
        AVISOS.append(f'{os.path.basename(arquivo)}: a pessoa termina em y={round(y0 + h)}, antes da borda de baixo ({ALTURA}). Desça ou aumente.')
    c = pc.imagem(nome, destino, x0 + w / 2, y0 + h / 2)
    pc.ex('layer.layerStyle.dropShadow', color='#0b120d', opacity=22, angle=90, distance=10, size=30)
    return c


def recorte_de_noticia(veiculo, titulo, data, x=MARGEM, y=PECA_Y, w=560, prefixo='NOTICIA'):
    """Cartão de notícia (como o recorte de jornal da V4, mas limpo): veículo e data em cima, a manchete REAL da
    matéria (curta, até 15 palavras) embaixo. Nunca invente manchete: se não for a do veículo, escreva "resumo".
    Devolve onde o cartão termina."""
    v = pc.texto(f'{prefixo}-VEICULO', veiculo.upper(), x + 32, y + 56, 24, 700, '#3f7a0f')  # verde de leitura no cartão branco
    pc.texto(f'{prefixo}-DATA', data, x + w - 32, y + 56, 24, 400, CINZA, alinhar='right')
    t = pc.texto(f'{prefixo}-TITULO', titulo, x + 32, y + 84, 36, 600, PROFUNDO, largura=w - 64, entrelinha=46)
    fim = t[4] + 32
    f = pc.forma(f'{prefixo}-CARTAO', 'roundedRect', x, y, w, fim - y, BRANCO, 18, sombra=SOMBRA)
    pc.abaixo_de(f, v[0])  # o veículo é a camada mais de baixo das três: o cartão fica atrás de todas
    pc.forma(f'{prefixo}-FILETE', 'rect', x + 32, y + 72, 56, 3, AZUL)
    return fim


def palavra_de_impacto(texto, x=MARGEM, base=PECA_Y + 200, tam=180, cor=AZUL, fundo=None, nome='IMPACTO'):
    """Palavra ou frase curta em Oswald, grande, dentro do slide de conteúdo ("SER FEITO AQUI", "R$ 205 MILHÕES").
    `fundo` (cor) põe uma tarja atrás, com a letra branca. Devolve a caixa (x0, y0, x1, y1) da tinta."""
    t = pc.texto(nome, texto, x if not fundo else x + 24, base, tam, 700, (PROFUNDO if fundo == AZUL else BRANCO) if fundo else cor, fonte=IMPACTO)
    if fundo:
        f = pc.forma(f'{nome}-TARJA', 'roundedRect', x, t[2] - 20, (t[3] - t[1]) + 48, (t[4] - t[2]) + 40, fundo, 14)
        pc.abaixo_de(f, t[0])
        cabe(f'a palavra de impacto "{texto}"', x + (t[3] - t[1]) + 48)
    else:
        cabe(f'a palavra de impacto "{texto}"', t[3])
    return t[1:]


def credito(texto, cor='#5B6474'):
    """Crédito da foto (ou "Imagem ilustrativa") no canto de cima à direita, na altura da logo, em 24 px.
    Foto real com licença CC BY pede o autor; foto gerada por IA num post de notícia pede "Imagem ilustrativa".
    `cor`: escura em fundo claro, '#FFFFFF' quando o canto da foto é escuro."""
    t = pc.texto('CREDITO', texto, DIREITA, LOGO_Y + 9, 24, 500, cor, alinhar='right')
    if t[1] < MARGEM + 72 + 186 + 32:
        raise ValueError(f'o crédito "{texto}" é comprido demais e encosta na logo: encurte (ex.: "Foto: Nome / Wikimedia").')


def foto_na_peca(arquivo, nome, credito_da_foto=None, y=PECA_Y, ate=ATE, x=MARGEM, w=920, gravidade='Center', prefixo='FOTO-PECA'):
    """Foto real (de agência, de produto, de evento) no lugar da peça, com os cantos da peça e sombra.
    O crédito, quando há, vai em 24 px logo abaixo da foto, por fora: nada fica por cima dela."""
    h = ate - y - (40 if credito_da_foto else 0)
    pc.forma(f'{prefixo}-FUNDO', 'roundedRect', x, y, w, h, ESCURO, 30, sombra=SOMBRA)
    pc.imagem(prefixo, recorte(achar(arquivo), w, h, nome, gravidade=gravidade), x + w / 2, y + h / 2, prender=True)
    if credito_da_foto:
        pc.texto(f'{prefixo}-CREDITO', credito_da_foto, x, ate - 6, 24, 400, T['texto'])


def titulo_de_foto(linha, palavra, tam, base=PALAVRA_BASE, cor=BRANCO, risco='#95db30', fundo_da_palavra=None):
    """Título dos slides de foto, sempre no mesmo lugar: a palavra gigante assenta em PALAVRA_BASE e a linha
    pequena, com o risco azul, fica logo acima dela. `tam` é o tamanho da palavra, escolhido para ela
    ocupar a largura entre as margens (256 para "NO MEIO", 208 para "SER ASSIM"). O máximo é 256."""
    p = pc.texto('TITULO-2', palavra, 540, base, tam, 700, cor, alinhar='center', fonte=IMPACTO, dentro=False)  # a medida é logo abaixo, com o tam certo
    if fundo_da_palavra:  # a palavra dentro de uma tarja (como o "MAIS CARO?" da V4)
        f = pc.forma('TITULO-2-TARJA', 'roundedRect', p[1] - 28, p[2] - 24, (p[3] - p[1]) + 56, (p[4] - p[2]) + 48, fundo_da_palavra, 18)
        pc.abaixo_de(f, p[0])
        FICHA['fecho'] = True  # a tarja da palavra já fecha a capa
    larg, vao = p[3] - p[1], DIREITA - MARGEM
    cheio = min(256, int(tam * vao / larg))
    if larg > vao + 8 or tam > 256:
        raise ValueError(f'"{palavra}" com tam={tam} ocupa {round(larg)} px e não cabe entre as margens ({vao} px): use tam={cheio}.')
    if cheio < 160:
        raise ValueError(f'"{palavra}" é comprida demais para palavra gigante (só caberia com {cheio} px): use uma ou duas palavras, até 10 letras.')
    if cheio - tam > 8:
        AVISOS.append(f'slide {FICHA.get("n")}: a palavra "{palavra}" pode crescer para tam={cheio} e ocupar a largura toda.')
    base = p[2] - 40
    t = pc.texto('TITULO-1', linha, 540, base, T_TITULO, 600, cor, alinhar='center', espaco=-10, dentro=False)
    if t[3] - t[1] > vao:
        raise ValueError(f'a linha pequena do título ("{linha}") não cabe entre as margens: encurte (até uns 26 caracteres).')
    if risco:
        pc.forma('TITULO-1-RISCO', 'rect', t[1], base + 18, t[3] - t[1], 6, risco)
    FICHA['titulo'] = True


def tarja_da_capa(texto, y=TARJA_Y):
    """Fecha a frase da capa: tarja azul com letra branca na faixa do rodapé, no meio do slide."""
    t = pc.texto('TARJA-TEXTO', texto, 540, y + 67, 64, 700, PROFUNDO, alinhar='center', espaco=-5)
    if (t[3] - t[1]) + 80 > DIREITA - MARGEM:
        raise ValueError(f'a tarja da capa ("{texto}") não cabe entre as margens: encurte (até uns 22 caracteres).')
    f = pc.forma('TARJA-FUNDO', 'roundedRect', t[1] - 40, y, (t[3] - t[1]) + 80, TARJA_H, AZUL, 16)
    pc.abaixo_de(f, t[0])
    FICHA['fecho'] = True


def chamada(verbo='Comente', palavra='CONVELLO'):
    """Chamada do slide final, na faixa do rodapé: o verbo, a palavra em tarja azul e o botão redondo.
    O fio que vem dos outros slides entra pela esquerda e termina nela. Uma chamada só."""
    cy = TARJA_Y + TARJA_H / 2
    a = pc.texto('CHAMADA-1', verbo, 0, cy + 20, 60, 500, BRANCO, dentro=False)
    b = pc.texto('CHAMADA-2', palavra, 0, cy + 23, 64, 700, PROFUNDO, dentro=False)
    wa, wb = a[3] - a[1], b[3] - b[1]
    total = wa + 24 + 32 + wb + 32 + 24 + 72
    if total > DIREITA - MARGEM - 48:
        raise ValueError(f'a chamada "{verbo} {palavra}" não cabe na faixa do rodapé: encurte a palavra.')
    x = round(540 - total / 2)
    g = pc.forma('CHAMADA-TARJA', 'roundedRect', x + wa + 24, TARJA_Y, wb + 64, TARJA_H, AZUL, 16)
    pc.abaixo_de(g, a[0])
    pc.ex('type.edit', layer=a[0], move=[x - a[1], 0])
    pc.ex('type.edit', layer=b[0], move=[x + wa + 24 + 32 - b[1], 0])
    pc.ex('layer.select', layer=b[0])
    pc.forma('FIO-ENTRADA', 'rect', 0, cy - 1, x - 24, 3, BRANCO)
    bx = x + wa + 24 + wb + 64 + 24 + 36
    pc.bola('CHAMADA-BOTAO', bx, cy, 72, AZUL)
    seta('CHAMADA-SETA', bx, cy, PROFUNDO, para='baixo')
    FICHA['fecho'] = True


def fechar(n):
    """Confere se o slide tem o que todo slide tem e grava o PSD e o PNG."""
    assert FICHA.get('n') == n, f'fechar({n}) sem abrir o slide {n} antes'
    falta = [nome for chave, nome in (('logo', 'a logo (topo)'), ('fio', 'o fio (rodapé)'), ('titulo', 'o titulo_de_foto'),
                                      ('fecho', 'a tarja_da_capa ou a chamada')) if FICHA.get(chave) is False]
    if falta:
        raise ValueError(f'slide {n} sem ' + ' e sem '.join(falta) + '.')
    pc.salvar(SAIDA, f'{n:02d}')
    FEITOS[n] = dict(FICHA)


def gravar_fichas():
    """Guarda o tipo de cada slide em planta.json (a régua e a conferência leem de lá)."""
    arq = os.path.join(SAIDA, 'planta.json')
    tudo = json.load(open(arq)) if os.path.exists(arq) else {}
    tudo.update({str(n): f for n, f in FEITOS.items()})
    json.dump(tudo, open(arq, 'w'), ensure_ascii=False, indent=1)
    return tudo


def rodar(slides, args):
    """Monta os slides pedidos na linha de comando (ou todos) e, no fim, a folha com todos eles."""
    pedidos = [int(a) for a in args] or sorted(slides)
    nums = sorted(slides)
    try:
        if not args and nums != [1] and nums != list(range(1, len(nums) + 1)):
            raise SystemExit(f'Este slides.py tem só os slides {nums}, e a montagem completa precisa ir de 1 a {len(nums)} sem pular.\n'
                             f'Para montar só esses: python3 motor/montar.py <pasta> {" ".join(map(str, nums))}')
        for n in pedidos:
            if n not in slides:
                raise SystemExit(f'não existe o slide {n} em slides.py (existem: {sorted(slides)})')
            slides[n]()
            print('slide', n, 'ok', flush=True)
    finally:
        pc.fim()
        if FEITOS:
            gravar_fichas()
    if not args and sorted(slides) != [1]:  # um slide só é card: não tem capa nem final
        for n in nums:
            certo = 'foto' if n in (1, nums[-1]) else 'conteudo'
            assert FEITOS[n]['tipo'] == certo, f'slide {n}: a capa e o final são de foto e os do meio são de conteúdo'
    pngs = sorted(f for f in os.listdir(os.path.join(SAIDA, 'png')) if f.endswith('.png'))
    folha = os.path.join(SAIDA, 'folha.jpg')
    subprocess.run(['montage'] + [os.path.join(SAIDA, 'png', f) for f in pngs] + ['-resize', '540x720', '-tile', f'{min(len(pngs), 5)}x', '-geometry', '+10+10',
                   '-background', '#111', '-quality', '90', folha], check=True)
    seguidos = [n for n in sorted(FEITOS) if FEITOS[n].get('tema') and FEITOS.get(n + 1, {}).get('tema') == FEITOS[n]['tema']]
    for n in seguidos:
        AVISOS.append(f'slides {n} e {n + 1} com o mesmo fundo ({FEITOS[n]["tema"]}): confira se o ritmo ficou bom de arrastar.')
    for a in AVISOS:
        print('AVISO:', a)
    print('folha:', folha)
