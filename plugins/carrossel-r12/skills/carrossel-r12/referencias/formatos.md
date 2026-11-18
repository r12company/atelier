# Formatos: carrossel, card e stories

Os três usam a mesma identidade (logo, fontes, cores, margens de 80, régua de 8) e o mesmo motor. Muda a planta e o molde.
O formato sai do `slides.py`: a linha `ALTURA = ...` e quantos slides existem em `SLIDES`.

| Formato | Tamanho | Linha no `slides.py` | Slides | Fio | Legenda |
| --- | --- | --- | --- | --- | --- |
| Carrossel | 1080 x 1440 (3:4) ou 1080 x 1350 (4:5) | nenhuma, ou `ALTURA = 1350` | 6 a 10 | sim | sim |
| Card (post único) | 1080 x 1350 ou 1080 x 1440 | `ALTURA = 1350` (ou nenhuma) | 1: `SLIDES = {1: s1}` | não | sim |
| Stories | 1080 x 1920 (9:16) | `ALTURA = 1920` | 3 a 6 telas | sim, nas telas do meio | não (vai o texto de cada tela e o adesivo) |

Provas que montam sem imagem nenhuma: `exemplo/prova-card/` e `exemplo/prova-stories/`.
A régua e a conferência (`regua.py`, `conferir.py`) valem para os três. No card e nos stories a régua de texto é mais curta: até 50 palavras e 10 blocos por tela (mire em 30).

## Card: uma imagem, uma ideia

Monte com `abrir(1, card=True)` (fundo claro por padrão; `abrir(1, 'escuro', card=True)` para o outro fundo) ou com `abrir_foto(1)` para card de foto.
Sem fio e sem pergunta: o card não continua. A peça pode descer até `CARD_ATE` (80 px da borda de baixo).

| Molde | Como montar | Bom para |
| --- | --- | --- |
| **Frase + peça** | `manchete` de 2 linhas, `corpo` curto com tarja, uma peça de `PECA_Y` a `CARD_ATE` | uma ideia com prova visual |
| **Número que choca** | `manchete` curta, tarja, `palavra_de_impacto('614', base=CARD_ATE - 40, tam=240 a 320, cor=tema()['dest'])` | o dado é a notícia (só número real, com fonte) |
| **Print com uma frase** | `manchete` de 1 ou 2 linhas sem `corpo`, `print_do_sistema(..., y=TEXTO_Y + 48, ate=CARD_ATE)` | mostrar trabalho real da R12 (site de cliente, campanha), com autorização do cliente |
| **Dado em peça** | `manchete` curta e uma peça de dado (barras, linha no tempo, antes x depois), como `s3` e `s6` de `exemplo/slides-pdf-seo.py` | comparar sem texto: anúncio x SEO, antes x depois |
| **Citação** | aspas grandes em Oswald, a frase em IBM Plex 54 a 64 (até 20 palavras), quem disse em 30 e a fonte em 24 | fala de alguém, sempre com nome e fonte |
| **Card de foto** | `abrir_foto(1)`, `foto_de_pessoa` ou `foto_inteira`, `titulo_de_foto`, `tarja_da_capa` | a frase que para o dedo, com rosto |

O card leva legenda como o carrossel (`copy.md`, seção 5) e entra no mesmo feed: a capa de foto do card não repete a pose nem a pessoa da última capa.

## Stories: 3 a 6 telas

Área segura: o Instagram cobre o alto da tela (até 250 px: nome e barra de progresso) e o pé (de 1500 px para baixo: resposta e figurinhas). Nada importante fora de 250 a 1500. O motor já põe a planta nisso:

| Guia | Stories (1920) |
| --- | --- |
| Logo | de 250 a 314 (meio em 282) |
| Título, linhas de base | 438 e 518 |
| Texto de apoio | 594 e 642; tarja até 722 |
| Peça | 786 a 1360 (sem texto de apoio, sobe para 590) |
| Fio | 1440 (faixa de 1392 a 1488) |
| Foto: cabelo começa | 250, rosto com 600 de altura |
| Foto: palavra gigante assenta | 1368; tarja ou chamada de 1392 a 1488 |
| Foto: escurece a partir de | 1000 |

Moldes de stories:

| Tela | Molde |
| --- | --- |
| 1, capa com gancho | `abrir_foto(1)`, foto 9:16 (peça a foto em 9:16, `modelos-de-prompt/pessoa.md`), linha pequena e palavra gigante, tarja. O gancho é a frase mais forte do roteiro (`copy.md`, seção 6) |
| meio, conteúdo | `abrir(n)`, `manchete` de 2 linhas e a peça GRANDE (gráfico, desenho ou print de trabalho real) subindo para `TEXTO_Y + 48`, sem texto de apoio. Uma ideia por tela |
| última, chamada | `abrir_foto(n)` com a chamada (`chamada('Fale com a', 'R12')`, `chamada('Comente', 'R12')`, `chamada('Responda', 'SIM')`). A chamada combina com o adesivo sugerido |

Proibido nos stories: contador de página ("1/5"), "toque para ver", "arraste para o lado", seta pedindo toque. O fio já mostra que continua.
Adesivo (enquete, caixa de pergunta, link) quem põe é quem posta, no app: sugira no `copy.md` qual e onde (sempre entre 250 e 1500, onde não cobre a peça).
