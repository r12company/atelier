"""Proposta de SEO da R12: modelo para qualquer empresa. 23 slides, viram o PDF.

Código de consulta: foi montado num motor irmão deste (o do PDF de venda, que não vem no pacote) e as imagens não vêm
junto, então ele não remonta aqui. Copie as peças (barras, busca, fluxo, linha no tempo, torre de preço, equação).
Na versão pública, o caso real (s14) e o site de cliente (s15) viraram exemplo genérico e os preços viraram 0.000.

DIREÇÃO DE ARTE
- Capa: título embaixo, a dona da empresa de camisa verde no meio, lupa 3D grande atrás à direita e pino à esquerda.
- Final: a mesma pessoa apontando para cima, rosto à esquerda, pino 3D do outro lado.
- Fundos: claro nos pares, escuro nos ímpares.
- Moldes no meio: clássico, peça em cima, número de impacto, dividido, pílulas, foto na peça, resumo com ícones.
- Ordem do texto muda: em uns slides o título vem antes; em outros, a peça ou o número.
"""
import os

from comum import (ATE, AZUL, BRANCO, IMPACTO, MARGEM, PASTA, PECA_Y, PROFUNDO, SOMBRA, abrir, abrir_foto, chamada, corpo,
                   fechar, fio, foto_de_pessoa, foto_na_peca, manchete, objeto, palavra_de_impacto, pc, svg_png, tarja_da_capa,
                   titulo_de_foto, topo)

VERDE = AZUL                 # #95db30, o verde da R12 (no motor o nome ficou AZUL)
ESCURO = PROFUNDO            # #161616
CLARO = '#e7ffef'
VERDE_ESC = '#3f7a0f'        # verde que dá leitura em cima do claro
APAGADO = '#8fa596'
LINHA = '#2f3d33'
CINZA_G = '#5f6368'

# ── ícones próprios (traço único) ──
I = {
    'lupa': '<circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.3 15.3 21 21"/>',
    'pin': '<path d="M12 21s-6.5-6.1-6.5-11a6.5 6.5 0 0 1 13 0c0 4.9-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.3"/>',
    'alvo': '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r=".9"/>',
    'grafico': '<path d="M3 20.5h18"/><path d="M6 17v-4M10.5 17V9.5M15 17v-6M19.5 17V5"/>',
    'engrenagem': '<circle cx="12" cy="12" r="3"/><path d="M12 2.5v3M12 18.5v3M2.5 12h3M18.5 12h3M5.3 5.3l2.1 2.1M16.6 16.6l2.1 2.1M5.3 18.7l2.1-2.1M16.6 7.4l2.1-2.1"/><circle cx="12" cy="12" r="6.5"/>',
    'pagina': '<path d="M6 2.5h8.5L19 7v14.5H6z"/><path d="M14.5 2.5V7H19"/><path d="M9 11.5h7M9 15h7M9 18.5h4"/>',
    'estrela': '<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
    'ia': '<rect x="4.5" y="7" width="15" height="12" rx="3"/><path d="M12 7V3.5"/><circle cx="9" cy="12.5" r="1.1"/><circle cx="15" cy="12.5" r="1.1"/><path d="M9.5 16h5"/>',
    'predio': '<path d="M4 21V5.5L13 3v18M13 8.5h7V21M2.5 21h19"/><path d="M7 8h3M7 11.5h3M7 15h3M16 12h1.5M16 15.5h1.5"/>',
    'moeda': '<circle cx="12" cy="12" r="8.5"/><path d="M14.8 8.8c-.6-.9-1.6-1.3-2.8-1.3-1.7 0-2.8.9-2.8 2.1 0 2.9 5.8 1.5 5.8 4.6 0 1.3-1.2 2.3-3 2.3-1.3 0-2.4-.5-3-1.4M12 5.5v2M12 16.5v2"/>',
    'check': '<path d="m5 12.5 4.5 4.5L19 7.5"/>',
    'x': '<path d="M6.5 6.5l11 11M17.5 6.5l-11 11"/>',
    'olho': '<path d="M2 12s3.6-6.5 10-6.5S22 12 22 12s-3.6 6.5-10 6.5S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
    'conversa': '<path d="M4 5h16v11H9.5L5.5 19.5V16H4z"/><path d="M8 9.5h8M8 12.5h5"/>',
    'celular': '<rect x="6.5" y="2.5" width="11" height="19" rx="2.5"/><path d="M10.5 18.5h3"/>',
    'casa': '<path d="M3 11 12 3.5 21 11"/><path d="M5.5 9v11.5h13V9"/><path d="M10 20.5v-6h4v6"/>',
    'saude': '<path d="M12 20.5s-8-4.6-8-10.4A4.3 4.3 0 0 1 12 7.6a4.3 4.3 0 0 1 8 2.5c0 5.8-8 10.4-8 10.4z"/>',
    'balanca': '<path d="M12 3v17.5M7 20.5h10M4.5 7h15"/><path d="m4.5 7-2.5 6a2.8 2.8 0 0 0 5 0z"/><path d="m19.5 7-2.5 6a2.8 2.8 0 0 0 5 0z"/>',
    'carro': '<path d="M3.5 16.5V12l2.2-5h12.6l2.2 5v4.5z"/><path d="M3.5 12h17"/><circle cx="7.5" cy="16.5" r="1.8"/><circle cx="16.5" cy="16.5" r="1.8"/>',
    'relogio': '<circle cx="12" cy="12" r="8.5"/><path d="M12 7v5l3.5 2"/>',
    'escudo': '<path d="M12 2.5 19.5 5.5v6c0 4.6-3.2 8.3-7.5 10-4.3-1.7-7.5-5.4-7.5-10v-6z"/><path d="m8.5 12 2.4 2.4 4.6-4.8"/>',
    'calendario': '<rect x="3.5" y="5" width="17" height="15.5" rx="2"/><path d="M3.5 9.5h17M8 2.5V6M16 2.5V6"/>',
}
os.makedirs(os.path.join(PASTA, 'icones'), exist_ok=True)


# A parede das fotos do Gemini tem vinheta forte e o cabelo encosta no topo: o recorte automático do motor levava a
# parede junto. Aqui o recorte usa a máscara feita na hora de alisar a parede (geradas/<foto>-mascara.png).
import comum  # noqa: E402
import numpy as _np  # noqa: E402
from PIL import Image as _Image  # noqa: E402


def _recorte_pela_mascara(origem, destino, rosto):
    nome = os.path.splitext(os.path.basename(origem))[0]
    rgb = _np.asarray(_Image.open(origem).convert('RGB'))
    alfa = _np.asarray(_Image.open(os.path.join(PASTA, 'geradas', nome + '-mascara.png')).convert('L'))
    _Image.fromarray(_np.dstack([rgb, alfa]), 'RGBA').save(destino)


comum.recortar_pessoa = _recorte_pela_mascara


def ic(nome, chave, cx, cy, lado, cor, traco=1.6):
    """Ícone de traço, desenhado aqui, em qualquer cor e tamanho."""
    arq = os.path.join(PASTA, 'icones', f'{chave}-{cor[1:]}-{traco}.svg')
    with open(arq, 'w') as f:
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="{cor}" stroke-width="{traco}" '
                f'stroke-linecap="round" stroke-linejoin="round">{I[chave]}</svg>')
    pc.imagem(nome, svg_png(arq, lado, f'ic-{chave}-{cor[1:]}-{traco}-{lado}'), cx, cy)


def cartao(nome, x, y, w, h, fundo, raio=24, borda=None):
    return pc.forma(nome, 'roundedRect', x, y, w, h, fundo, raio, borda=borda, sombra=SOMBRA)


def pilula(nome, txt, x, y, h, fundo, cor, tam=32, peso=600, folga=28):
    t = pc.texto(f'{nome}-TXT', txt, x + folga, y + h / 2 + tam * 0.35, tam, peso, cor)
    f = pc.forma(nome, 'roundedRect', x, y, (t[3] - t[1]) + 2 * folga, h, fundo, h / 2)
    pc.abaixo_de(f, t[0])
    pc.ex('layer.select', layer=t[0])
    return t[3] + folga


# ── 1 capa ──
def s1():
    abrir_foto(1)

    def atras():
        objeto('LUPA', 'lupa-3d.png', 940, 470, 480, 14)
        objeto('PINO', 'pino-3d.png', 130, 720, 220, -12)

    foto_de_pessoa('dona-capa-lisa.png', cabelo=165, queixo=495, centro=345, atras=atras, rosto_x=440, rosto=460)
    topo('branco', arroba=False)
    titulo_de_foto('Sua empresa em', 'PRIMEIRO', 229)
    tarja_da_capa('no Google')
    fechar(1)


# ── páginas do meio: limpas como a capa. Título grande em Oswald, uma imagem, o fio. Sem parágrafo. ──
T = 92            # tamanho do título das páginas
P0 = 560          # onde a imagem começa


def tit(linhas, y=316):  # 316: o título respira abaixo da logo (pedido do dono da marca)
    return manchete(linhas, y=y, tam=T)


def s2():
    abrir(2)
    tit(['Antes de comprar,', '!o cliente pesquisa.'])
    cartao('BUSCA', MARGEM, P0, 920, 128, BRANCO, 64)
    ic('BUSCA-ICONE', 'lupa', MARGEM + 80, P0 + 64, 60, CINZA_G, 2)
    pc.texto('BUSCA-TXT', 'dentista perto de mim', MARGEM + 136, P0 + 80, 44, 400, '#202124')
    for i in range(3):
        yy = P0 + 200 + i * 150
        eu = i == 0
        cartao(f'RES-{i + 1}', MARGEM, yy, 920, 124, ESCURO if eu else BRANCO, 24, borda=(4, VERDE) if eu else None)
        if eu:
            pc.texto('RES-1-T', 'Sua Empresa', MARGEM + 48, yy + 78, 44, 700, VERDE)
        else:
            pc.forma(f'RES-{i + 1}-L1', 'roundedRect', MARGEM + 48, yy + 40, 420 - i * 80, 18, '#d5e6da', 9)
            pc.forma(f'RES-{i + 1}-L2', 'roundedRect', MARGEM + 48, yy + 72, 620 - i * 60, 14, '#e4efe7', 7)
    fio('E quem aparece hoje?', primeiro=True)
    fechar(2)


def s7():
    abrir(7)
    tit(['O ChatGPT também', '!indica empresas.'])
    cartao('PERGUNTA', 300, P0 + 20, 700, 130, CLARO, [32, 32, 8, 32])
    pc.texto('PERGUNTA-T', 'Onde faço implante?', 340, P0 + 100, 40, 500, ESCURO)
    cartao('RESPOSTA', MARGEM, P0 + 210, 760, 230, BRANCO, [8, 32, 32, 32])
    ic('RESPOSTA-IA', 'ia', MARGEM + 80, P0 + 290, 68, VERDE_ESC, 1.8)
    pc.texto('RESPOSTA-1', 'Na Sua Empresa.', MARGEM + 140, P0 + 310, 48, 700, VERDE_ESC)
    pc.texto('RESPOSTA-2', 'Ótimas avaliações no Google.', MARGEM + 48, P0 + 392, 34, 400, ESCURO)
    pilula('SIMULACAO', 'Simulação', MARGEM, ATE - 60, 56, VERDE, ESCURO, 28, 700)
    fio('Como a R12 faz isso?')
    fechar(7)


ETAPAS = [('lupa', 'Diagnóstico'), ('engrenagem', 'Fundação técnica'), ('pagina', 'Páginas que vendem'),
          ('estrela', 'Mapa e avaliações'), ('ia', 'Pronto para as IAs')]


def s8():
    abrir(8)
    tit(['Cinco etapas.', '!Nada de mágica.'])
    h = (ATE - P0 - 4 * 20) // 5
    for i, (chave, t) in enumerate(ETAPAS):
        yy = P0 + i * (h + 20)
        cartao(f'ETAPA-{i + 1}', MARGEM, yy, 920, h, ESCURO, h // 2)
        ic(f'ETAPA-{i + 1}-ICONE', chave, MARGEM + 84, yy + h / 2, 64, VERDE, 1.6)
        pc.texto(f'ETAPA-{i + 1}-T', t, MARGEM + 156, yy + h / 2 + 18, 48, 600, CLARO, fonte=IMPACTO)
    fio('Por onde começa?')
    fechar(8)


def s9():
    abrir(9)
    tit(['Primeiro,', '!a gente mede tudo.'])
    objeto('LUPA', 'lupa-3d.png', 540, 920, 600, 10)
    fio('E depois de medir?')
    fechar(9)


def s10():
    abrir(10)
    tit(['O Google precisa', '!ler sem tropeçar.'])
    itens = ['Título em cada página', 'Mapa do site limpo', 'Rápido no celular', 'Endereço e horário']
    cartao('LISTA', MARGEM, P0, 920, ATE - P0, ESCURO, 30)
    passo = (ATE - P0) // 4
    for i, t in enumerate(itens):
        cy = P0 + passo * i + passo / 2
        ic(f'ITEM-{i + 1}-CHECK', 'check', MARGEM + 90, cy, 64, VERDE, 2.4)
        pc.texto(f'ITEM-{i + 1}', t, MARGEM + 156, cy + 15, 42, 500, CLARO)
        if i:
            pc.forma(f'ITEM-{i + 1}-RISCO', 'rect', MARGEM + 48, P0 + passo * i, 824, 2, LINHA)
    fio('E o que ele vai ler?')
    fechar(10)


def s11():
    abrir(11)
    tit(['Uma página para', '!cada busca.'])
    cartao('RAIZ', 320, P0 + 20, 440, 104, VERDE, 52)
    pc.texto('RAIZ-T', 'seusite.com.br', 540, P0 + 86, 40, 700, ESCURO, alinhar='center')
    pc.forma('TRONCO', 'rect', 538, P0 + 124, 4, 70, VERDE)
    pc.forma('GALHO', 'rect', 238, P0 + 192, 604, 4, VERDE)
    folhas = [('/implante', '/clareamento', '/aparelho'), ('/centro', '/zona-sul', '/canoas')]
    for c, grupo in enumerate(folhas):
        cx = 238 + c * 604
        pc.forma(f'RAMO-{c + 1}', 'rect', cx - 2, P0 + 192, 4, 70, VERDE)
        for k, f in enumerate(grupo):
            yy = P0 + 262 + k * 136
            cartao(f'FOLHA-{c + 1}-{k + 1}', cx - 210, yy, 420, 108, CLARO, 24)
            ic(f'FOLHA-{c + 1}-{k + 1}-IC', 'pagina' if c == 0 else 'pin', cx - 146, yy + 54, 48, VERDE_ESC, 1.8)
            pc.texto(f'FOLHA-{c + 1}-{k + 1}-T', f, cx - 106, yy + 67, 34, 600, ESCURO)
    fio('E quem busca no mapa?')
    fechar(11)


def s12():
    abrir(12)
    tit(['Quem busca perto', '!vê o mapa primeiro.'])
    cartao('MAPA', MARGEM, P0, 920, ATE - P0, ESCURO, 30)
    lugares = [('Sua Empresa', '4,9', True), ('Auto Center Silva', '4,4', False), ('Oficina do Bairro', '4,1', False)]
    for i, (nm, nota, eu) in enumerate(lugares):
        yy = P0 + 48 + i * 190
        if eu:
            pc.forma('LOCAL-1-FUNDO', 'roundedRect', MARGEM + 32, yy - 10, 856, 160, '#1f2a1f', 20, borda=(3, VERDE))
        ic(f'LOCAL-{i + 1}-PIN', 'pin', MARGEM + 104, yy + 70, 72, VERDE if eu else APAGADO, 1.6)
        pc.texto(f'LOCAL-{i + 1}-NOME', nm, MARGEM + 176, yy + 66, 44, 700, CLARO if eu else APAGADO)
        ic(f'LOCAL-{i + 1}-ESTRELA', 'estrela', MARGEM + 194, yy + 110, 32, '#e8b400', 2)
        pc.texto(f'LOCAL-{i + 1}-NOTA', nota, MARGEM + 224, yy + 122, 32, 500, CLARO if eu else APAGADO)
    pilula('SIMULACAO', 'Simulação', MARGEM + 40, ATE - 90, 56, VERDE, ESCURO, 28, 700)
    fio('E no Google?')
    fechar(12)


def s13():
    abrir(13)
    tit(['É assim que', '!queremos aparecer.'])
    x, w, y0 = MARGEM, 920, P0
    cartao('SERP', x, y0, w, ATE - y0, BRANCO, 30)
    pc.forma('SERP-BARRA', 'roundedRect', x + 40, y0 + 44, w - 80, 96, BRANCO, 48, borda=(2, '#dfe1e5'))
    ic('SERP-LUPA', 'lupa', x + 100, y0 + 92, 44, CINZA_G, 2.2)
    pc.texto('SERP-BUSCA', 'advogado em canoas', x + 144, y0 + 106, 36, 400, '#202124')
    pc.forma('SERP-TOPO', 'roundedRect', x + 40, y0 + 180, w - 80, 220, '#f4fbe9', 20, borda=(3, VERDE))
    pc.texto('SERP-DOM', 'suaempresa.com.br', x + 76, y0 + 240, 28, 400, '#4d5156')
    pc.texto('SERP-TIT', 'Advogado em Canoas', x + 76, y0 + 306, 46, 500, '#1a0dab')
    pc.texto('SERP-DS', 'Sua Empresa', x + 76, y0 + 362, 30, 400, '#4d5156')
    for k in range(2):
        pc.forma(f'SERP-L{k}', 'roundedRect', x + 76, y0 + 460 + k * 50, 520 - k * 140, 18, '#e3e6e8', 9)
    pilula('SIMULACAO', 'Simulação', x + 40, ATE - 90, 56, VERDE, ESCURO, 28, 700)
    fio('Isso funciona de verdade?')
    fechar(13)


def s14():
    abrir(14)
    tit(['Caso real: um bloqueio', '!que ninguém via.'])  # nome do cliente só com autorização dele
    w, h = 448, ATE - P0
    for i, (rot, linha, chave, cor_ic) in enumerate([('Antes', 'Google bloqueado', 'x', '#d9805f'),
                                                    ('Depois', 'Site liberado', 'check', VERDE)]):
        x = MARGEM + i * (w + 24)
        cartao(f'CASO-{i + 1}', x, P0, w, h, ESCURO, 28)
        pc.texto(f'CASO-{i + 1}-ROT', rot, x + 48, P0 + 110, 64, 600, CLARO, fonte=IMPACTO)
        ic(f'CASO-{i + 1}-IC', chave, x + w / 2, P0 + 340, 200, cor_ic, 2)
        pc.texto(f'CASO-{i + 1}-NOTA', linha, x + w / 2, P0 + 580, 34, 600, cor_ic, alinhar='center')
    fio('E num negócio local?')
    fechar(14)


def s15():
    abrir(15)
    tit(['Uma página para', '!cada bairro.'])
    foto_na_peca('site-do-cliente.jpg', 'site', 'Cliente, cidade: N páginas no Google (dado real)', y=P0, gravidade='NorthWest')
    fio('Quanto tempo leva?')
    fechar(15)


def s16():
    abrir(16)
    tit(['Os primeiros', '!90 dias.'])
    marcos = ['Diagnóstico', 'Fundação técnica', 'Páginas e mapa', 'Primeiro relatório']
    quando = ['Semana 1', 'Semana 3', 'Mês 2', 'Mês 3']
    passo = (ATE - P0) // 4
    pc.forma('LINHA', 'rect', MARGEM + 26, P0 + 30, 4, passo * 3, ESCURO)
    for i, (m, q) in enumerate(zip(marcos, quando)):
        yy = P0 + i * passo
        pc.bola(f'MARCO-{i + 1}', MARGEM + 28, yy + 30, 52, VERDE if i == 3 else ESCURO)
        pc.texto(f'MARCO-{i + 1}-Q', q, MARGEM + 96, yy + 24, 30, 500, '#4c5e52')
        pc.texto(f'MARCO-{i + 1}-M', m, MARGEM + 96, yy + 84, 56, 600, ESCURO, fonte=IMPACTO)
    fio('E como eu acompanho?')
    fechar(16)


def s17():
    abrir(17)
    tit(['Todo mês, você', '!vê o resultado.'])
    itens = [('grafico', 'Posições'), ('olho', 'Visitas'), ('conversa', 'Contatos'), ('estrela', 'Avaliações')]
    w, h = 448, (ATE - P0 - 24) // 2
    for i, (chave, t) in enumerate(itens):
        x, yy = MARGEM + (i % 2) * (w + 24), P0 + (i // 2) * (h + 24)
        cartao(f'REL-{i + 1}', x, yy, w, h, CLARO, 28)
        ic(f'REL-{i + 1}-IC', chave, x + w / 2, yy + h / 2 - 40, 120, VERDE_ESC, 1.4)
        pc.texto(f'REL-{i + 1}-T', t, x + w / 2, yy + h / 2 + 100, 48, 600, ESCURO, alinhar='center', fonte=IMPACTO)
    fio('O que vocês prometem?')
    fechar(17)


def s18():
    abrir(18)
    tit(['Quem garante 1º', '!está mentindo.'])
    w, h = 448, ATE - P0
    for i, (t, itens, fundo, cor, chave, cor_ic) in enumerate([
            ('Prometemos', ['Método completo', 'Números reais', 'Português simples'], ESCURO, CLARO, 'check', VERDE),
            ('Não prometemos', ['1º lugar em 7 dias', 'Truque que o Google pune'], '#f6e6e1', ESCURO, 'x', '#b5543f')]):
        x = MARGEM + i * (w + 24)
        cartao(f'PROM-{i + 1}', x, P0, w, h, fundo, 28)
        ic(f'PROM-{i + 1}-IC', chave, x + 80, P0 + 100, 72, cor_ic, 2.4)
        pc.texto(f'PROM-{i + 1}-T', t, x + 48, P0 + 230, 52, 600, cor, fonte=IMPACTO)
        for k, it in enumerate(itens):
            pc.texto(f'PROM-{i + 1}-IT-{k + 1}', it, x + 48, P0 + 330 + k * 70, 30, 400, cor)
    fio('E quanto custa?')
    fechar(18)


def s20():
    abrir(20)
    tit(['Escolha o', '!seu plano.'])
    planos = [('Essencial', '0.000', ['10 páginas', 'Mapa do Google', 'Relatório mensal'], False),
              ('Profissional', '0.000', ['30 páginas', 'Avaliações', '4 conteúdos/mês', 'Pronto para IAs'], True),
              ('Dominante', '0.000', ['Sem limite', '8 conteúdos/mês', 'Olho no rival', 'Reunião mensal'], False)]
    gap = 20
    w = (920 - 2 * gap) // 3
    topo_y, fim = PECA_Y - 40, ATE
    for i, (nm, v, itens, rec) in enumerate(planos):
        x = MARGEM + i * (w + gap)
        y0 = topo_y - (24 if rec else 0)
        fundo, cor, sub = (ESCURO, CLARO, APAGADO) if rec else (BRANCO, ESCURO, '#4c5e52')
        cartao(f'PLANO-{i + 1}', x, y0, w, fim - y0, fundo, 28, borda=(4, VERDE) if rec else None)
        cx = x + w / 2
        pc.texto(f'PLANO-{i + 1}-NOME', nm, cx, y0 + 76, 34, 700, cor, alinhar='center')
        r = pc.texto(f'PLANO-{i + 1}-RS', 'R$', cx - 100, y0 + 186, 28, 600, sub)
        n = pc.texto(f'PLANO-{i + 1}-V', v, cx - 60, y0 + 186, 76, 700, VERDE if rec else ESCURO, fonte=IMPACTO)
        larg = (r[3] - r[1]) + 8 + (n[3] - n[1])
        x0 = cx - larg / 2
        pc.ex('type.edit', layer=r[0], move=[x0 - r[1], 0])
        pc.ex('type.edit', layer=n[0], move=[x0 + (r[3] - r[1]) + 8 - n[1], 0])
        pc.texto(f'PLANO-{i + 1}-MES', 'por mês', cx, y0 + 230, 26, 500, sub, alinhar='center')
        pc.forma(f'PLANO-{i + 1}-RISCO', 'rect', x + 28, y0 + 270, w - 56, 2, LINHA if rec else '#d5e6da')
        for k, it in enumerate(itens):
            yy = y0 + 330 + k * 64
            ic(f'PLANO-{i + 1}-CK-{k + 1}', 'check', x + 44, yy - 9, 30, VERDE if rec else VERDE_ESC, 2.6)
            t = pc.texto(f'PLANO-{i + 1}-IT-{k + 1}', it, x + 70, yy, 26, 500, cor)
            assert t[3] <= x + w - 16, f'item "{it}" passa da coluna {nm} em {t[3] - (x + w - 16)} px'
        bh = 64
        b = pc.forma(f'PLANO-{i + 1}-BOTAO', 'roundedRect', x + 24, fim - 24 - bh, w - 48, bh, VERDE if rec else ESCURO, bh / 2)
        pc.texto(f'PLANO-{i + 1}-BOTAO-T', 'Quero este', cx, fim - 24 - bh / 2 + 10, 28, 700, ESCURO if rec else CLARO, alinhar='center')
        if rec:
            pilula('PLANO-REC', 'Mais escolhido', cx - 128, y0 - 26, 52, VERDE, ESCURO, 26, 700)
    fio('Isso se paga?')
    fechar(20)


# ── 21 a conta: número de impacto ──
def s22():
    abrir(22)
    tit(['Perguntas que', '!sempre chegam.'])
    faq = [('Quando aparece?', 'A partir do 2º mês.'), ('E se eu parar?', 'O que foi feito fica.'),
           ('Vou ter trabalho?', 'Só aprovar os textos.')]
    h = (ATE - P0 - 2 * 24) // 3
    for i, (q, r) in enumerate(faq):
        yy = P0 + i * (h + 24)
        cartao(f'FAQ-{i + 1}', MARGEM, yy, 920, h, ESCURO, 28)
        pc.texto(f'FAQ-{i + 1}-Q', q, MARGEM + 48, yy + h / 2 - 6, 56, 600, VERDE, fonte=IMPACTO)
        pc.texto(f'FAQ-{i + 1}-R', r, MARGEM + 48, yy + h / 2 + 52, 34, 400, CLARO)
    fio('Vamos começar?')
    fechar(22)


def traco(nome, pontos, cor, largura=6):
    pc.ex('shape.create', kind='path', name=nome, fill=None,
          path={'subpaths': [{'closed': False, 'knots': [list(p) for p in pontos]}]},
          stroke={'width': largura, 'color': cor, 'align': 'center', 'cap': 'round', 'join': 'round'})


def s3():
    abrir(3)
    tit(['Quem está no topo', '!leva o cliente.'])
    alturas = [1.0, 0.6, 0.4, 0.27, 0.18, 0.05]
    rot = ['1º', '2º', '3º', '4º', '5º', 'Pág. 2']
    base, topo = ATE - 70, P0 + 90
    w, gap = 124, 35
    for i, (a, r) in enumerate(zip(alturas, rot)):
        x = MARGEM + i * (w + gap)
        h = max(12, round((base - topo) * a))
        pc.forma(f'BARRA-{i + 1}', 'roundedRect', x, base - h, w, h, VERDE if i < 3 else '#2a2f2a', [16, 16, 0, 0])
        pc.texto(f'BARRA-{i + 1}-R', r, x + w / 2, ATE - 14, 36 if i < 5 else 28, 600, CLARO if i < 3 else APAGADO, alinhar='center', fonte=IMPACTO)
    pc.forma('BASE', 'rect', MARGEM, base, 920, 3, LINHA)
    pc.texto('NOTA', 'Os 3 primeiros ficam com quase todos os cliques', MARGEM, topo - 40, 30, 500, VERDE)
    fio('E se não for você?')
    fechar(3)


def s4():
    abrir(4)
    tit(['Hoje, alguém está', '!no seu lugar.'])
    cartao('SERP', MARGEM, P0, 920, ATE - P0, ESCURO, 30)
    pc.forma('SERP-BARRA', 'roundedRect', MARGEM + 40, P0 + 40, 840, 84, '#2a2f2a', 42)
    ic('SERP-LUPA', 'lupa', MARGEM + 96, P0 + 82, 40, APAGADO, 2.2)
    pc.texto('SERP-BUSCA', 'o que você vende + sua cidade', MARGEM + 136, P0 + 94, 32, 400, APAGADO)
    linhas = [('moeda', 'Anúncio pago'), ('predio', 'Portal'), ('alvo', 'Concorrente')]
    for i, (chave, t) in enumerate(linhas):
        yy = P0 + 160 + i * 112
        pc.forma(f'RES-{i + 1}', 'roundedRect', MARGEM + 40, yy, 840, 92, '#222722', 18)
        ic(f'RES-{i + 1}-IC', chave, MARGEM + 96, yy + 46, 48, APAGADO, 1.6)
        pc.texto(f'RES-{i + 1}-T', t, MARGEM + 148, yy + 60, 40, 600, CLARO, fonte=IMPACTO)
    yy = P0 + 160 + 3 * 112 + 16
    pc.forma('VOCE', 'roundedRect', MARGEM + 40, yy, 840, ATE - 40 - yy, ESCURO, 18, borda=(3, VERDE))
    pc.texto('VOCE-T', 'Sua empresa?', MARGEM + 440, yy + (ATE - 40 - yy) / 2 + 18, 52, 600, VERDE, alinhar='center', fonte=IMPACTO)
    fio('Como virar esse jogo?')
    fechar(4)


def s5():
    abrir(5)
    tit(['SEO é o Google', '!entender você.'])
    nos = [('pagina', 'Seu site'), ('lupa', 'Google entende'), ('conversa', 'Cliente chama')]
    h = (ATE - P0 - 2 * 70) // 3
    for i, (chave, t) in enumerate(nos):
        yy = P0 + i * (h + 70)
        eu = i == 2
        cartao(f'NO-{i + 1}', MARGEM, yy, 920, h, VERDE if eu else CLARO, 28)
        ic(f'NO-{i + 1}-IC', chave, MARGEM + 110, yy + h / 2, 96, ESCURO, 1.5)
        pc.texto(f'NO-{i + 1}-T', t, MARGEM + 210, yy + h / 2 + 26, 72, 600, ESCURO, fonte=IMPACTO)
        if i < 2:
            seta_y = yy + h + 35
            traco(f'SETA-{i + 1}', [(540, seta_y - 22), (540, seta_y + 22)], VERDE, 5)
            traco(f'SETA-{i + 1}-P', [(526, seta_y + 8), (540, seta_y + 22), (554, seta_y + 8)], VERDE, 5)
    fio('E o anúncio pago?')
    fechar(5)


def s6():
    abrir(6)
    tit(['Anúncio é aluguel.', '!SEO é patrimônio.'])
    x0, y0, x1, y1 = MARGEM, P0, 1000, ATE
    cartao('GRAFICO', x0, y0, x1 - x0, y1 - y0, ESCURO, 30)
    gx0, gx1, gy0, gy1 = x0 + 60, x1 - 60, y0 + 120, y1 - 110
    pc.forma('EIXO-X', 'rect', gx0, gy1, gx1 - gx0, 3, LINHA)
    pc.texto('EIXO-T', 'tempo', gx1, gy1 + 50, 28, 500, APAGADO, alinhar='right')
    corte = gx0 + (gx1 - gx0) * 0.55
    alto = gy0 + 140
    traco('ANUNCIO', [(gx0, alto), (corte, alto), (corte, gy1 - 4), (gx1, gy1 - 4)], '#d9805f', 7)
    pc.texto('ANUNCIO-T', 'Anúncio', gx0, alto - 28, 34, 600, '#d9805f')
    pc.texto('PAROU', 'parou de pagar', corte + 18, gy1 - 30, 28, 500, '#d9805f')
    pts = [(gx0 + (gx1 - gx0) * t / 20, gy1 - 8 - (gy1 - gy0 - 30) * (t / 20) ** 1.8) for t in range(21)]
    traco('SEO', pts, VERDE, 8)
    pc.texto('SEO-T', 'SEO', gx1, gy0 - 20, 40, 600, VERDE, alinhar='right', fonte=IMPACTO)
    fio('E o ChatGPT?')
    fechar(6)


def s19():
    abrir(19)
    tit(['Implantação', '!completa.'])
    itens = [('Diagnóstico', 1200), ('Fundação técnica', 1800), ('Páginas', 2400), ('Mapa', 800), ('IAs', 900), ('Painel', 500)]
    total = sum(v for _, v in itens)
    base, alto = ATE - 60, P0 + 20
    escala = (base - alto) / total
    x, w = MARGEM, 470
    y = base
    tons = ['#2a2f2a', '#232823']
    for i, (t, v) in enumerate(itens):
        h = round(v * escala)
        y -= h
        pc.forma(f'TORRE-{i + 1}', 'rect', x, y, w, h - 4, tons[i % 2])
        pc.texto(f'TORRE-{i + 1}-T', t, x + 28, y + h / 2 + 10, 28 if h > 40 else 24, 500, CLARO)
    pc.texto('TORRE-TOTAL', 'R$ 0.000', x + w / 2, base + 50, 40, 600, APAGADO, alinhar='center', fonte=IMPACTO)
    pc.forma('TORRE-RISCO', 'rect', x + w / 2 - 80, base + 34, 160, 4, '#d9805f')
    xb, wb = x + w + 60, 1000 - (x + w + 60)
    hb = round(2900 * escala)
    pc.forma('PRECO', 'roundedRect', xb, base - hb, wb, hb, VERDE, [20, 20, 0, 0])
    pc.texto('PRECO-T', 'R$ 0.000', xb + wb / 2, base - hb - 30, 76, 600, VERDE, alinhar='center', fonte=IMPACTO)
    pc.texto('PRECO-S', 'você paga', xb + wb / 2, base - hb / 2 + 12, 34, 700, ESCURO, alinhar='center')
    fio('E por mês?')
    fechar(19)


def s21():
    abrir(21)
    tit(['Um cliente novo', '!paga meses de SEO.'])
    cartao('CONTA', MARGEM, P0, 920, 360, CLARO, 30)
    pc.texto('CONTA-A', '10 meses de SEO', MARGEM + 48, P0 + 80, 40, 600, ESCURO, fonte=IMPACTO)
    for k in range(10):
        xx = MARGEM + 48 + (k % 5) * 70
        yy = P0 + 120 + (k // 5) * 70
        pc.forma(f'MES-{k + 1}', 'roundedRect', xx, yy, 56, 56, VERDE_ESC, 10)
    pc.texto('IGUAL', '=', MARGEM + 470, P0 + 230, 96, 600, ESCURO, fonte=IMPACTO, alinhar='center')
    pc.forma('VENDA', 'roundedRect', MARGEM + 540, P0 + 110, 340, 156, ESCURO, 20)
    ic('VENDA-IC', 'casa', MARGEM + 620, P0 + 188, 72, VERDE, 1.6)
    pc.texto('VENDA-T', '1 venda', MARGEM + 680, P0 + 206, 52, 600, VERDE, fonte=IMPACTO)
    pc.texto('VENDA-S', 'de imóvel', MARGEM + 540 + 170, P0 + 310, 30, 500, ESCURO, alinhar='center')
    outros = [('saude', 'Clínica', '2 meses'), ('balanca', 'Advocacia', '2 meses'), ('carro', 'Oficina', '1 mês')]
    w = (920 - 2 * 20) // 3
    for i, (chave, t, m) in enumerate(outros):
        x = MARGEM + i * (w + 20)
        yy = P0 + 400
        cartao(f'OUTRO-{i + 1}', x, yy, w, ATE - yy, ESCURO, 24)
        ic(f'OUTRO-{i + 1}-IC', chave, x + w / 2, yy + 70, 60, VERDE, 1.6)
        pc.texto(f'OUTRO-{i + 1}-T', t, x + w / 2, yy + 150, 32, 500, CLARO, alinhar='center')
        pc.texto(f'OUTRO-{i + 1}-M', m, x + w / 2, yy + 230, 56, 600, VERDE, alinhar='center', fonte=IMPACTO)
    fio('Ficou alguma dúvida?')
    fechar(21)


# ── 23 final ──
def s23():
    abrir_foto(23)

    def atras():
        objeto('PINO', 'pino-3d.png', 310, 330, 250, -12)

    foto_de_pessoa('dona-final-larga.png', cabelo=160, queixo=490, centro=479, atras=atras, rosto_x=720, rosto=500)
    topo('branco', arroba=False)
    titulo_de_foto('Sua empresa', 'NA FRENTE', 217)
    chamada('Fale com a', 'R12')
    fechar(23)


SLIDES = {i: globals()[f's{i}'] for i in range(1, 24)}
