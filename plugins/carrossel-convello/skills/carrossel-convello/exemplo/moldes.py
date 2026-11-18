"""Exemplo das composições (exemplo/moldes.jpg). Atenção: a capa do slide 1 com a palavra em tarja foi REPROVADA depois;
vale a capa limpa do 02, só mudando a posição (referencias/moldes.md).
Foto do slide 2: "Amazon Spheres 2018", de Andy Li, Wikimedia Commons, domínio público (CC0). As imagens não vêm no pacote:
é código de consulta."""
from comum import (ATE, AZUL, BRANCO, PECA_Y, VERMELHO, abrir, abrir_foto, chamada, corpo, credito, fechar, fio, foto_de_pessoa, manchete,
                   palavra_de_impacto, pessoa_solta, recorte_de_noticia, tarja_da_capa, titulo_de_foto, topo)

ALTURA = 1350


def s1():
    abrir_foto(1)
    foto_de_pessoa('homem-capa.png', cabelo=375, queixo=672, centro=430)
    topo('branco', arroba=False)
    titulo_de_foto('O e-mail da Microsoft', 'CAIU', 230, fundo_da_palavra=AZUL)
    fechar(1)


def s2():  # metade foto, metade texto
    abrir(2, 'branco', foto_no_topo='amazon-spheres.jpg', foto_ate=600, foco_y=0.5)
    y = manchete(['A Amazon quer mostrar', '!até o que não vende.'], y=720)
    corpo(['Um documento interno descreve um catálogo de', 'produtos de toda a internet, não só da loja.', '!Segundo a Reuters, é um plano.'], y=y)
    fio('E o que isso muda?', primeiro=True)
    fechar(2)


def s3():  # pessoa saindo pela borda, texto na outra coluna
    abrir(3, 'azul')
    pessoa_solta('homem-final.png', cabelo=388, queixo=650, centro=443, cx=820, cabelo_y=430, rosto=420)
    y = manchete(['Texto de um', 'lado, pessoa', '!do outro.'], limite=600)
    corpo(['A pessoa sai pela borda', 'de baixo e da direita,', '!sem nada por cima dela.'], y=y, limite=600)
    fio('E a notícia?')
    fechar(3)


def s4():  # recorte de notícia + palavra de impacto
    abrir(4, 'branco')
    y = manchete(['Quando a notícia', '!vira a peça.'])
    corpo(['O cartão traz o veículo, a data e a manchete', 'de verdade. Embaixo, o dado em destaque.', '!Limpo, sem colagem.'], y=y)
    fim = recorte_de_noticia('Reuters', 'Amazon planeja catálogo com produtos de toda a internet', '13/11/2026', y=PECA_Y)
    palavra_de_impacto('R$ 7 BI', base=ATE - 20, tam=200, fundo=VERMELHO)
    fio('E no fim?')
    fechar(4)


def s5():
    abrir_foto(5)
    foto_de_pessoa('homem-final.png', cabelo=388, queixo=650, centro=443, escurecer='tudo')
    topo('azul', arroba=False)
    titulo_de_foto('O final pode ter', 'OUTRA CARA', 175, base=700)
    chamada('Comente', 'SIM')
    fechar(5)


SLIDES = {1: s1, 2: s2, 3: s3, 4: s4, 5: s5}
