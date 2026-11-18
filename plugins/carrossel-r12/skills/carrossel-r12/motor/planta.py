"""ARQUITETURA VISUAL do carrossel Convello: a planta que todo slide segue (1080x1440).

O que se repete fica no MESMO lugar em todos os slides: o olho aprende onde procurar e só o conteúdo muda.
Os respiros saem de uma régua só, em múltiplos de 8 (8, 16, 24, 40, 48, 64, 80).

Rota do olho no slide de conteúdo: desce pela margem esquerda e sai pelo canto de baixo à direita.
  1º título          a maior letra, no canto de cima à esquerda, onde a leitura começa
  2º frase em tarja  bloco de cor chapada: é lida até por quem pula o texto
  3º a peça          a prova (print ou desenho), no centro, sempre começando na mesma altura
  4º o fio           a pergunta que puxa o próximo slide e o botão redondo, no canto onde a leitura termina

Rota do olho no slide de foto (capa e final):
  1º o rosto (rosto segura o olhar)               2º para onde a pessoa olha (o celular, logo acima do título)
  3º a palavra gigante                            4º a tarja (capa) ou a chamada (final)

Em cada slide uma coisa só chama mais que as outras. De onde isso saiu: referencias/arquitetura-visual.md.
Este arquivo só tem números: o comum.py monta os slides com eles e o regua.py confere.

Dois formatos, escolhidos pela linha `ALTURA = ...` do slides.py do carrossel (o montar.py lê):
  1440 (3:4)  o padrão, o do carrossel 02
  1350 (4:5)  o topo é igual; tudo que fica embaixo (peça, fio, palavra gigante, tarja) sobe 90 px
  1920 (9:16) stories: o topo desce 194 px (área segura de 250 a 1500) e o rodapé fica em 1440
"""
import os

ALTURA = int(os.environ.get('ALTURA', '1440'))
assert ALTURA in (1440, 1350, 1920), f'ALTURA {ALTURA}: o motor monta 1440 (3:4), 1350 (4:5) ou 1920 (stories, 9:16)'
STORIES = ALTURA == 1920
# Stories: o Instagram cobre o alto (0 a 250, nome e barra de progresso) e o pé (1500 em diante, resposta e figurinhas).
# O topo desce 194 px para a logo começar em 250, e o rodapé fica acima de 1500.
_DESCE = 194 if STORIES else 0
_SOBE = 0 if STORIES else 1440 - ALTURA  # o que o 4:5 tira de baixo
MARGEM = 80          # tudo começa em x=80 e termina em x=1000
LOGO_Y = 88 + _DESCE          # meio da logo (ela vai de 56 a 120; nos stories, de 250 a 314)
TITULO_Y = 244 + _DESCE       # linha de base da 1ª linha do título (o topo das letras fica 80 px abaixo da logo)
TITULO_PASSO = 80    # distância entre as duas linhas do título
TEXTO_Y = 348 + _DESCE        # onde o título acaba; a 1ª linha do texto assenta 52 px depois
TARJA_FIM = 528 + _DESCE      # onde termina a frase em tarja do texto (duas linhas + tarja)
PECA_Y = 592 + _DESCE         # topo da peça em TODO slide: 64 px abaixo da tarja do texto
FIO_Y = 1440 if STORIES else 1344 - _SOBE  # altura do fio do rodapé (faixa de FIO_Y - 48 a FIO_Y + 48)
ATE = FIO_Y - 80     # fim da peça: 80 px acima do fio. Nenhuma peça passa daqui
CARD_ATE = ALTURA - 80  # card (post único, sem fio): a peça pode descer até a margem de baixo
MIOLO = 40           # respiro por dentro de cartão e de lista
MOLDURA = 8          # moldura branca em volta de todo print; conta como parte da peça

# Tamanho de letra (px). Nada abaixo de 24.
T_TITULO = 64
T_CORPO = 34
T_FIO = 34

# Slides de foto
CABELO_Y = 250 if STORIES else 48  # onde começa o cabelo da pessoa (nos stories, abaixo da faixa coberta)
ROSTO = 600 if STORIES else (540 if not _SOBE else 500)  # altura do rosto, do cabelo ao queixo
ESCURECE_DE = 1000 if STORIES else 800 - _SOBE  # a foto escurece daqui para baixo, para o título aparecer
TARJA_Y, TARJA_H = FIO_Y - 48, 96   # a tarja da capa e a chamada do final ocupam a faixa do rodapé
PALAVRA_BASE = TARJA_Y - 24  # linha de base da palavra gigante
