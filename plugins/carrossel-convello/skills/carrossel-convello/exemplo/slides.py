"""Carrossel 02: "Seu cliente está no meio da família". 10 slides, aprovado pelo dono da marca em 15/11/2026.

Código de consulta: as fotos, os ícones e os prints deste carrossel não vêm no pacote, então ele não remonta aqui.
Copie as peças (conversa, etiqueta, balão, lista, cartões, rótulos com linha fina, painel de resumo).

A moldura de todo slide (fundo, logo, título, texto, fio, foto) vem do comum.py. Aqui fica só o que é deste
carrossel: os textos e a PEÇA de cada slide, que mora entre PECA_Y e ATE.
"""
from comum import (ATE, AZUL, BRANCO, CINZA, ESCURO, IMPACTO, MARGEM, MIOLO, PECA_Y, SOMBRA, TEXTO_Y, VERMELHO, abrir, abrir_foto,
                   chamada, corpo, fechar, fio, foto_de_pessoa, icone, linha_fina, manchete, objeto, pc, print_do_sistema,
                   tarja_da_capa, titulo_de_foto, topo)

# Emenda entre a capa e o slide 2: um ícone 3D do WhatsApp fica metade em cada slide (cx=1080 na capa, cx=0 no 2).
# No slide 2 ele entra POR CIMA da lista (atrás dela ficava tapado, o dono da marca reprovou). A altura é a divisa entre
# a 2ª e a 3ª conversa (o slide 2 confere esse número) e o tamanho deixa 19 px até os círculos das iniciais.
EMENDA_Y = 864
EMENDA_LADO = 220

# Emenda entre os slides 7 e 8: o print do funil em colunas (kanban) começa na beirada direita do 7 e continua no 8.
# Os dois slides usam os mesmos números, senão a imagem não casa na hora de arrastar. Vai de PECA_Y a ATE nos dois.
FUNIL_W = round((ATE - PECA_Y) * 1004 / 897)   # largura do cartão do funil no slide 7 (ele aparece inteiro)
PAN_X7 = MARGEM + FUNIL_W + 48                 # onde o kanban começa no slide 7: 48 px depois do funil
PAN_W = (1080 - MARGEM) - (PAN_X7 - 1080)      # largura total do print: no slide 8 ele entra em PAN_X7 - 1080 e vai até a margem

# Cores das peças desenhadas (lista e conversa no estilo de aplicativo de mensagem)
CLARO = '#C9D1DE'    # mensagem dentro da peça escura
APAGADO = '#B4BAC5'  # nome das conversas pessoais (apagado, mas dá para ler)
SUMIDO = '#8A919E'   # mensagem e hora das conversas pessoais
FOTO = '#4A4C56'     # círculo de quem não tem foto, como no WhatsApp escuro
RISCO = '#2F3036'    # divisória entre as conversas
VERDE = '#00A884'    # bolinha de não lidas do WhatsApp escuro
BEGE = '#EBE4D8'     # fundo de aplicativo de mensagem


# ── capa ──
def s1():
    abrir_foto(1)

    def icones():
        # Jeito certo de pôr ícone em foto: grande, atrás da pessoa e meio escondido por ela, um de cada lado,
        # os dois virados para o meio. O da esquerda some atrás do ombro e o da direita atrás da cabeça.
        objeto('WHATSAPP-ESQUERDA', 'zap-3d.png', 190, 590, 340, -12)
        objeto('WHATSAPP-DIREITA', 'zap-3d-b.png', 880, 400, 420, 10)

    # cabelo, queixo e centro do rosto medidos na foto: o enquadramento sai igual ao do slide final.
    # Com o rosto nesse tamanho o celular aparece inteiro logo acima do título, e é para ele que o homem olha.
    foto_de_pessoa('homem-capa.png', cabelo=375, queixo=672, centro=430, atras=icones)
    objeto('EMENDA-WHATSAPP', 'zap-3d.png', 1080, EMENDA_Y, EMENDA_LADO)  # metade aqui, metade no slide 2
    topo('branco', arroba=False)
    titulo_de_foto('Seu cliente está', 'NO MEIO', 256)
    tarja_da_capa('da família')
    fechar(1)


# ── peças desenhadas ──
def conversa(pref, x, cy, inicial, nome, msg, foto=AZUL, cor_inicial=BRANCO, cor_nome=BRANCO, cor_msg=CLARO, d=84,
             nome_tam=35, msg_tam=29, vao=28):
    """Círculo com a inicial, nome e mensagem: o miolo de uma conversa. `x` é a borda esquerda do círculo."""
    pc.bola(f'{pref}-FOTO', x + d / 2, cy, d, foto)
    pc.texto(f'{pref}-INICIAL', inicial, x + d / 2, cy + 12, 34, 700, cor_inicial, alinhar='center')
    pc.texto(f'{pref}-NOME', nome, x + d + vao, cy - 8, nome_tam, 700, cor_nome)
    pc.texto(f'{pref}-MENSAGEM', msg, x + d + vao, cy + 34, msg_tam, 400, cor_msg)


def etiqueta(nome, txt, y, h, tam=28, peso=500, cor=CINZA, fundo=BRANCO, raio=12, folga=22):
    """Texto no meio do slide com um fundo do tamanho dele (etiqueta de dia e aviso)."""
    t, x0, _, x1, _ = pc.texto(f'{nome}-TEXTO', txt, 540, y + h / 2 + tam * 0.35, tam, peso, cor, alinhar='center')
    f = pc.forma(f'{nome}-FUNDO', 'roundedRect', x0 - folga, y, (x1 - x0) + 2 * folga, h, fundo, raio)
    pc.abaixo_de(f, t)
    pc.ex('layer.select', layer=t)


def balao(nome, y, h, txt, hora, peso=400, borda=None, hora_peso=400, hora_cor=CINZA):
    """Balão de mensagem recebida, da largura do texto, com a hora no canto de baixo à direita."""
    base = y + h / 2 + 14
    x = MARGEM + MIOLO
    t = pc.texto(f'{nome}-TEXTO', txt, x + 30, base, 44, peso)
    hr = pc.texto(f'{nome}-HORA', hora, t[3] + 30, base + 14, 28, hora_peso, hora_cor)
    f = pc.forma(nome, 'roundedRect', x, y, hr[3] + 30 - x, h, BRANCO, [8, 28, 28, 28], borda)
    pc.abaixo_de(f, t[0])
    pc.ex('layer.select', layer=hr[0])


# ── o problema ──
def s2():
    abrir(2, 'branco')
    y = manchete(['No meio disso,', '!alguém quer comprar.'])
    corpo(['Um cliente pede preço. Outro quer agendar uma visita.', 'Enquanto isso, chegam mensagens pessoais e', '!a conversa importante desce na lista.'], y)
    x, w, yc = MARGEM, 920, PECA_Y
    h = ATE - yc
    pc.forma('LISTA-FUNDO', 'roundedRect', x, yc, w, h, ESCURO, 30, sombra=SOMBRA)
    linhas = [('G', 'Grupo dos amigos', 'Lucas: Bora hoje?', '10:02', 17),
              ('M', 'Mãe', 'Filho, vai almoçar em casa?', '09:58', 3),
              ('F', 'Família', 'Tia Ana: Bom dia, pessoal.', '09:51', 12),
              ('C', 'Cliente apartamento', 'Consegue agendar a visita?', '09:12', 1),
              ('A', 'Amor', 'Não esquece de passar no mercado.', '08:55', 1)]
    cliente = 3
    rh = (h - 32) // len(linhas)
    y0 = yc + (h - rh * len(linhas)) // 2
    assert y0 + 2 * rh == EMENDA_Y, 'o ícone que vem da capa tem de cair na divisa entre a 2ª e a 3ª conversa'
    for i, (ini, nome, msg, hora, n) in enumerate(linhas):
        pref, ly = f'CONVERSA-{i + 1}', y0 + i * rh
        cy = ly + rh / 2
        if i == cliente:  # a única linha acesa: faixa azul de ponta a ponta, com tudo em branco
            pc.forma(f'{pref}-DESTAQUE', 'rect', x, ly, w, rh, AZUL)
            conversa(pref, x + MIOLO, cy, ini, nome, msg, foto=BRANCO, cor_inicial=AZUL, cor_msg=BRANCO)
            cor_hora, bolinha, cor_n = BRANCO, BRANCO, AZUL
        else:
            conversa(pref, x + MIOLO, cy, ini, nome, msg, foto=FOTO, cor_inicial=APAGADO, cor_nome=APAGADO, cor_msg=SUMIDO)
            cor_hora, bolinha, cor_n = SUMIDO, VERDE, ESCURO
            if i + 1 not in (cliente, len(linhas)):  # divisória entre as conversas, menos encostado na faixa azul
                pc.forma(f'{pref}-FIO', 'rect', x + MIOLO + 112, ly + rh - 1, w - 112 - 2 * MIOLO, 2, RISCO)
        pc.texto(f'{pref}-HORA', hora, x + w - MIOLO, cy - 8, 25, 400, cor_hora, alinhar='right')
        pc.bola(f'{pref}-BOLINHA', x + w - MIOLO - 22, cy + 25, 44, bolinha)
        pc.texto(f'{pref}-NAO-LIDAS', str(n), x + w - MIOLO - 22, cy + 34, 24, 700, cor_n, alinhar='center')
    objeto('EMENDA-WHATSAPP', 'zap-3d.png', 0, EMENDA_Y, EMENDA_LADO)  # a outra metade do ícone da capa, por cima da lista
    fio('O problema começa aqui', primeiro=True)
    fechar(2)


def s3():
    abrir(3, 'azul')
    y = manchete(['Você viu.', '!Mas esqueceu de responder.'])
    corpo(['Não foi falta de interesse. A mensagem ficou', 'para depois. Quando você lembra,', '!o cliente pode já ter procurado outra empresa.'], y)
    yc, topo_h = PECA_Y, 124
    h = ATE - yc
    pc.forma('CHAT-FUNDO', 'roundedRect', 80, yc, 920, h, BEGE, 30, sombra=SOMBRA)
    pc.forma('CHAT-TOPO', 'roundedRect', 80, yc, 920, topo_h, BRANCO, [30, 30, 0, 0])
    pc.forma('CHAT-TOPO-FIO', 'rect', 80, yc + topo_h, 920, 2, '#DAD2C4')
    cy = yc + topo_h / 2
    xf = MARGEM + MIOLO + 42  # centro do círculo da foto
    pc.bola('CHAT-FOTO', xf, cy, 84, AZUL)
    pc.texto('CHAT-INICIAL', 'C', xf, cy + 12, 34, 700, BRANCO, alinhar='center')
    pc.texto('CHAT-NOME', 'Cliente apartamento', xf + 70, cy - 8, 35, 700)
    pc.texto('CHAT-STATUS', 'visto por último hoje', xf + 70, cy + 31, 28, 400, CINZA)
    # A conversa ocupa o resto do cartão. O que sobra de altura vira respiro, repartido pelos pesos:
    # os dois balões ficam juntos e o vão maior, antes de "Hoje", é o tempo que passou sem resposta.
    alturas, pesos = [48, 100, 116, 48, 72], [1.2, 0.9, 0.5, 1.5, 0.9, 1.2]
    u = (h - topo_h - sum(alturas)) / sum(pesos)
    dia, b1, b2, hoje, aviso = [(yc + topo_h + u * sum(pesos[:i + 1]) + sum(alturas[:i]), a) for i, a in enumerate(alturas)]
    etiqueta('DIA', 'Terça-feira', *dia)
    balao('BALAO-1', *b1, 'Vi o apartamento no anúncio.', '09:10')
    balao('BALAO-2', *b2, 'Consegue agendar a visita?', 'Terça, 09:12', 600, (5, VERMELHO), 700, VERMELHO)
    etiqueta('HOJE', 'Hoje', *hoje)
    etiqueta('AVISO', 'Visto. Sem resposta desde terça.', *aviso, 36, 700, BRANCO, VERMELHO, 36, 40)
    fio('E se tiver uma equipe?')
    fechar(3)


def s4():
    abrir(4, 'branco', destaque=VERMELHO)
    y = manchete(['Com uma equipe,', 'fica [ainda pior.]'])
    corpo(['Quem respondeu? Quem ficou de retornar?', 'Quem está negociando? Sem organização,', '!ninguém sabe onde cada cliente parou.'], y)
    linhas = [('Cliente interessado', 'Qual o valor final do imóvel?', 'Quem\nrespondeu?'),
              ('Cliente apartamento', 'Consegue agendar a visita?', 'Quem ficou\nde retornar?'),
              ('Cliente da proposta', 'Vocês aceitam uma proposta?', 'Quem está\nnegociando?')]
    y0, vao, cw = PECA_Y, 48, 560  # 560 de cartão + 48 de respiro: a pergunta começa em 688
    ch = (ATE - y0 - 2 * vao) // 3  # altura inteira, para a borda do cartão sair nítida
    for i, (nome, msg, duvida) in enumerate(linhas):
        cy = y0 + i * (ch + vao) + ch / 2
        pc.forma(f'CLIENTE-{i + 1}-FUNDO', 'roundedRect', MARGEM, cy - ch / 2, cw, ch, ESCURO, 30, sombra=SOMBRA)
        conversa(f'CLIENTE-{i + 1}', MARGEM + MIOLO, cy, 'C', nome, msg, d=80, nome_tam=34, msg_tam=28, vao=24)
        # a pergunta é a palavra de impacto do slide: Oswald em caixa alta, como na capa.
        # Começa em 688 para a linha mais larga ("DE RETORNAR?") terminar na margem direita (1000).
        pc.texto(f'DUVIDA-{i + 1}', duvida.upper(), MARGEM + cw + vao, cy - 6, 50, 700, VERMELHO, entrelinha=58, fonte=IMPACTO)
    fio('Existe outro jeito')
    fechar(4)


# ── a solução, com print real ──
def s5():
    abrir(5, 'azul')
    y = manchete(['Seu atendimento precisa', '!de um lugar próprio.'])
    corpo(['No Convello, sua equipe acompanha os clientes', 'em uma lista organizada, com', '!responsável, origem e tempo de espera.'], y)
    # A peça aqui é o conjunto rótulo + print + rótulos: o rótulo de cima começa em PECA_Y, os de baixo terminam
    # em ATE e o print fica no meio, com o mesmo respiro (136 px) dos dois lados.
    # Só duas conversas do print (400 de altura): sobra respiro de verdade para os rótulos em cima e embaixo.
    yp, hp = PECA_Y + 136, 400
    print_do_sistema('lista-dono.png', 'p5-lista', yp, yp + hp)
    # Ponto exato em que cada linha encosta, medido no recorte já em 920 de largura.
    quem, espera = (734.5, yp + 38), (867.5, yp + 42)     # 1ª conversa, por cima: foto de quem atende e pílula de espera
    selo, origem = (192.5, yp + 357), (828.5, yp + 343)   # 2ª conversa, por baixo: selo do número e etiqueta de origem
    # Em cima vai um rótulo só, com chave: dois rótulos lado a lado ficavam grudados.
    yl = PECA_Y + 22
    barra, meio = yl + 47.5, (quem[0] + espera[0]) / 2 + 0.5
    pc.texto('APONTA-1-TEXTO', 'Quem atende e tempo de espera', 1000, yl, 30, 600, BRANCO, alinhar='right')
    linha_fina('APONTA-1-LINHA', [quem, (quem[0], barra), (espera[0], barra), espera], [(meio, yl + 20), (meio, barra)])
    yb = ATE - 8
    pc.texto('APONTA-2-TEXTO', 'Por qual número chegou', 80, yb, 30, 600, BRANCO)
    linha_fina('APONTA-2-LINHA', [selo, (selo[0], yb - 37)])
    pc.texto('APONTA-3-TEXTO', 'De onde o cliente veio', 1000, yb, 30, 600, BRANCO, alinhar='right')
    linha_fina('APONTA-3-LINHA', [origem, (origem[0], yb - 37)])
    fio('E o histórico do cliente?')
    fechar(5)


def s6():
    abrir(6, 'branco')
    manchete(['Ninguém precisa', '!começar do zero.'])
    corpo(['O Convello reúne resumo da conversa, notas e', 'informações importantes. Quem assume o atendimento', '!entende o que o cliente já pediu.'])
    # Recorte da ficha do tamanho exato da peça (do rosto do cliente até "Veio por qual WhatsApp"):
    #   magick telas-novas/ficha-completa-recorte.png -crop 980x686+106+118 +repage -background '#1C1C1F' -gravity North -extent 980x716 recortes/ficha-peca.png
    print_do_sistema('ficha-peca.png', 'p-ficha-peca', gravidade='North')
    fio('Mas e quem não comprou?')
    fechar(6)


def s7():
    abrir(7, 'azul')
    manchete(['A venda não termina', '!na conversa.'])
    corpo(['No funil de vendas, você vê quantos negócios', 'estão em cada etapa e quanto eles valem.', '!Dá para ver onde a venda trava.'])
    # o cartão do funil inteiro, encostado na esquerda: a largura sai da altura da peça
    print_do_sistema('funil-vendas.png', 'p-funil-vendas', w=FUNIL_W, gravidade='North', prefixo='FUNIL')
    # na beirada direita já aparece o começo do funil em colunas, que continua no slide 8
    print_do_sistema('kanban-pan.png', 'p-kanban-pan', x=PAN_X7, w=PAN_W, prefixo='KANBAN')
    fio('E pra mudar de etapa?')
    fechar(7)


def s8():
    abrir(8, 'branco')
    y = manchete(['Mudou de etapa?', '!É só arrastar.'])
    corpo(['Cada negócio é um cartão. O cliente avançou,', 'você arrasta para a próxima etapa.', '!O sistema avisa quem está parado há dias.'], y)
    # Recorte com as duas colunas inteiras e 24 px de respiro em volta, tirado do print inteiro:
    #   magick telas-novas/kanban-arrastando.png -crop 1325x1160+565+355 +repage recortes/kanban-janela.png
    # O print continua do slide 7: lá aparecem os primeiros 180 px na beirada direita, aqui ele entra pela esquerda
    # e vai até 1000. Mesmo topo, mesma altura e mesmo recorte nos dois (constantes PAN_*).
    print_do_sistema('kanban-pan.png', 'p-kanban-pan', x=PAN_X7 - 1080, w=PAN_W, prefixo='KANBAN')
    fio('Guarde isso')
    fechar(8)


# ── resumo para salvar (sem texto de apoio: o painel sobe) ──
def s9():
    abrir(9, 'azul')
    manchete(['Resumo para quem', '!vende pelo WhatsApp.'])
    itens = [('icone-conversas.png', 'Conversas [organizadas.]'), ('icone-responsavel.png', 'Cada cliente com [responsável.]'),
             ('icone-historico.png', 'Histórico sempre [acessível.]'), ('icone-funil.png', 'Negociações [acompanhadas.]')]
    yp, rh = TEXTO_Y + 48, 176  # o painel sobe e o fecho termina em ATE
    pc.forma('PAINEL', 'roundedRect', 80, yp, 920, 4 * rh, BRANCO, 30, sombra=SOMBRA)
    for i, (arq, txt) in enumerate(itens):
        ly = yp + i * rh
        if i:
            pc.forma(f'RESUMO-{i + 1}-FIO', 'rect', MARGEM + MIOLO, ly - 1, 920 - 2 * MIOLO, 2, '#DDE3EC')
        icone(f'RESUMO-{i + 1}-ICONE', arq, MARGEM + MIOLO + 60, ly + rh / 2, 120)  # ícone grande no lugar de número
        pc.texto(f'RESUMO-{i + 1}-TEXTO', txt, MARGEM + MIOLO + 120 + 32, ly + rh / 2 + 16, 44, 700)
    yf = ATE - 14 - 66  # a 2ª linha assenta em ATE; sobram uns 48 px entre o painel e o topo das letras
    pc.texto('FECHO-1', 'Cliente interessado não pode', MARGEM, yf, 54, 700, BRANCO, espaco=-10)
    pc.texto('FECHO-2', 'depender da sua memória.', MARGEM, yf + 66, 54, 700, BRANCO, espaco=-10)
    fio('Quer organizar suas vendas?')
    fechar(9)


# ── final: o mesmo desenho da capa, com a chamada no lugar da tarja ──
def s10():
    abrir_foto(10)
    foto_de_pessoa('homem-final.png', cabelo=388, queixo=650, centro=443)
    topo('branco', arroba=False)
    titulo_de_foto('Seu WhatsApp não precisa', 'SER ASSIM', 208)
    chamada('Comente', 'CONVELLO')
    fechar(10)


SLIDES = {1: s1, 2: s2, 3: s3, 4: s4, 5: s5, 6: s6, 7: s7, 8: s8, 9: s9, 10: s10}
