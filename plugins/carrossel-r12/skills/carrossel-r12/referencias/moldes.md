# Moldes: cada carrossel com a sua cara, no estilo da R12

Duas falas do dono da marca, que valem juntas:

1. "Tá muito lindo e perfeito, mas tá tudo igual o design, o layout e a ordem do texto. As capas também têm que diferenciar."
2. Sobre um teste com fundo de cor forte, frase centralizada e foto com texto por cima: "Isso tá poluído, nem parece slide, parece site. Mas aplique novas combinações."

Então: **o estilo é o da proposta de SEO** (`exemplo/folha-pdf-seo.jpg`): fundo claro ou escuro com degradê e grão, título grande em Oswald à esquerda, UMA imagem limpa, o fio no rodapé, a logo. O que muda de um carrossel para o outro são as **combinações**: molde de cada slide, ritmo de fundos, ordem do texto e a capa.
Peças prontas para copiar: `exemplo/slides-pdf-seo.py` (`s3` barras, `s4` busca com o lugar vazio, `s5` fluxo com setas, `s6` anúncio x SEO no tempo, `s19` torre de preço, `s21` equação "10 meses = 1 venda").

## O que a proposta de SEO faz bem

| O que ela faz | Como |
| --- | --- |
| Capa limpa | Pessoa de verdade de camisa verde, lupa 3D verde grande atrás, pino de mapa do outro lado; título embaixo e tarja verde. Nada mais |
| Mais visual por estratégia, não por imagem gerada | Barras, busca desenhada, fluxo com setas, linha no tempo, torre, equação. Uma peça só, que se entende sem ler |
| Pouco texto | Título grande de 2 linhas, a peça, o fio. O apoio de 2 linhas só quando indispensável (régua em `copy.md`, seção 3) |
| Ritmo variado | Moldes diferentes nos slides do meio; em uns o título vem antes, em outros a peça ou o número |
| Final que fecha a história | A mesma pessoa, agora apontando para cima, com o pino 3D do outro lado e `chamada('Fale com a', 'R12')` |

## O que outras agências fazem e a gente copia o jeito (não a cara)

- **A imagem é do assunto**: a pessoa da notícia (foto real), a logo da plataforma (Google, Instagram) em objeto 3D ou plana, nas cores dela. O fundo continua o nosso.
- **Composição muda a cada slide**: título em cima com a peça embaixo; foto ocupando a metade de cima e o texto embaixo; pessoa recortada saindo pela borda com o texto do outro lado; um número enorme; um recorte de notícia.
- **A capa muda a cada carrossel só na posição**: título embaixo, em cima ou no meio; pessoa no centro, à esquerda ou à direita; foto real do assunto. Os elementos e as cores são sempre os da R12.
- **Pouca coisa por slide**: um título, uma imagem forte. Nada de painel de site. Limite medido em `copy.md`, seção 3.

## O que não fazer (reprovado)

- Fundo de cor forte e frase grande centralizada: o motor só aceita claro e escuro.
- Foto ocupando o slide de conteúdo com texto por cima (`abrir(n, 'foto')`): o motor recusa. Foto no conteúdo é em faixa (metade de cima), dentro da peça ou pessoa recortada ao lado do texto.
- Vários cartões, selos, rótulos, notas e setas disputando o olho.
- Repetir a composição de outro carrossel (capa, ordem dos slides, peças).

## Regras de variação

- Escreva no topo do `slides.py` a **direção de arte** do carrossel: molde da capa, ritmo de fundos, moldes principais, ordem do texto (como no topo do `exemplo/slides-pdf-seo.py`).
- Nos 7 slides do meio, **pelo menos 4 moldes diferentes**, e nunca o mesmo molde em dois slides seguidos.
- **A ordem muda**: em uns slides o título vem primeiro; em outros a foto, a pessoa, o número ou a notícia vêm antes e o título explica.
- **Ritmo de fundos** só com claro e escuro, mas não precisa intercalar sempre: começar pelo escuro, ou dois claros seguidos, já muda.
- Título sempre à esquerda, em Oswald 82 a 92. Texto 34 (nada abaixo de 24).

## Moldes de conteúdo

| Molde | Como montar | Bom para |
| --- | --- | --- |
| **Clássico** | `manchete`, peça logo abaixo até `ATE`, `fio` (apoio com `corpo` só se indispensável) | explicar com prova |
| **Peça de dado** | `manchete` e uma peça de barras, linha no tempo ou antes x depois (`s3`, `s6` do exemplo) | comparar sem texto |
| **Fluxo** | pílulas com ícone de traço e setas finas verdes entre elas (`s5` do exemplo) | o caminho do clique até a venda |
| **Busca desenhada** | um cartão de busca genérico com o lugar vazio onde a empresa deveria estar (`s4` do exemplo) | aparecer no Google |
| **Equação** | dois blocos e o sinal de igual em Oswald (`s21` do exemplo) | custo x retorno, sem número inventado |
| **Metade foto** | `abrir(n, 'claro', foto_no_topo='foto.jpg', foto_ate=600, foco_y=...)`, `manchete(y=720)` | foto real do fato, do lugar, do produto |
| **Pessoa saindo da borda** | `pessoa_solta(arquivo, cabelo, queixo, centro, cx=820, cabelo_y=430, rosto=420)`, `manchete(..., limite=600)` | gente da notícia, personagem do post |
| **Peça em cima** | peça de 152 a ~700, `manchete(y=~820)` | quando a imagem é a notícia |
| **Número de impacto** | `palavra_de_impacto('3 de 10', base=..., tam=180 a 240, fundo=AZUL ou None)` com título curto (`AZUL` no motor é o verde `#95db30`) | quando o dado é a notícia (só número real, com fonte) |
| **Recorte de notícia** | `recorte_de_noticia('Veículo', 'manchete real da matéria', '13/11/2026', y=PECA_Y)` (a manchete é a do veículo, curta; nunca inventada) | mostrar que saiu na imprensa |
| **Dividido** | `manchete(..., limite=520)` numa coluna, peça em `x=560, w=440` | comparar, explicar um print de trabalho real |
| **Lista em pílulas** | 3 ou 4 linhas curtas, cada uma numa pílula sólida (`pc.forma` roundedRect + `pc.texto` 30 a 34), ícone de traço à esquerda | os três passos, os três serviços |
| **Foto na peça** | `foto_na_peca(arquivo, ...)` no lugar da peça, crédito embaixo | foto real sem ocupar a faixa |

`manchete` aceita 1 a 3 linhas, `y`, `x`, `tam` e `limite`. Peça, foto e pessoa nunca ficam por cima de texto.

## Capa e final: limpos, só muda ONDE as coisas ficam

Regra do dono da marca: "A capa, independente de tudo, tem que ser limpa igual tava antes, apenas mudar aonde fica."
Os elementos e as cores da capa são sempre os mesmos: foto (pessoa ou foto real do assunto), a logo, a linha pequena
branca com o risco verde, a palavra gigante branca em Oswald e a tarja verde (na capa) ou a chamada (no final). Objeto 3D
verde grande atrás da pessoa quando houver. Nada de palavra em tarja, palavra escura atrás da pessoa, selo, cartão ou texto a mais.

O que muda de um carrossel para o outro é só a posição:

| Posição | Como montar |
| --- | --- |
| **Título embaixo** (o da proposta de SEO) | `foto_de_pessoa(..., escurecer='baixo')`, `titulo_de_foto(...)`, `tarja_da_capa(...)` |
| **Título em cima** | `foto_de_pessoa(..., escurecer='cima')` (a pessoa embaixo), `titulo_de_foto(..., base=~430)`, `tarja_da_capa(..., y=~460)` logo abaixo da palavra |
| **Título no meio** | `escurecer='baixo'` (degradê único e liso, nunca `'tudo'`), `titulo_de_foto(..., base=~760)`, tarja logo abaixo, pessoa no alto |
| **Pessoa à esquerda ou à direita** | `rosto_x=330` a `440` ou `680` a `750` (foto com parede sobrando), objeto 3D grande do outro lado, título embaixo ou em cima |
| **Foto real do assunto** | `foto_inteira(arquivo, foco_x, foco_y, zoom, escurecer=...)` (fachada, evento) com o mesmo bloco de título, `credito(...)` |

Pessoa real da notícia só em foto real (`material.md`). Pose sempre do assunto e diferente das outras capas: notebook, balcão da loja, apontando para cima, braços cruzados.
A capa e o final do mesmo carrossel combinam entre si. A capa de um carrossel não repete a posição, a pessoa e os objetos da capa de outro.
