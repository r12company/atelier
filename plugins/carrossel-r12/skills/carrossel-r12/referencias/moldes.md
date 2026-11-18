# Moldes: cada carrossel com a sua cara, no estilo do Convello

Duas falas do dono da marca em 15/11/2026, que valem juntas:

1. "Tá muito lindo e perfeito, mas tá tudo igual o design, o layout e a ordem do texto. As capas também têm que diferenciar."
2. Sobre um teste com fundo marinho, frase centralizada e foto com texto por cima: "Mantenha nosso estilo, isso tá poluído, nem parece slide, parece site. Mas aplique novas combinações. Se inspire na V4."

Então: **o estilo é o do carrossel 02 e do 03** (fundo branco ou azul com degradê e grão, título à esquerda, tarja, uma peça limpa,
o fio no rodapé, a logo). O que muda de um carrossel para o outro são as **combinações**, do jeito que a V4 varia os dela.
Referências que ele mandou: os carrosséis da V4 Company no Instagram (as imagens não vêm no pacote, são de terceiros: se quiser, peça à produtora prints de uns 9 carrosséis recentes deles e olhe antes de desenhar). Exemplo montado: `exemplo/moldes.jpg` (código em `exemplo/moldes.py`).

## O exemplo do bom: o carrossel do TikTok

dono da marca, 15/11: "o do TikTok ficou muito bom". Folha em `exemplo/tiktok-folha.jpg` (7 dos 9 slides: os dois que citavam pessoas da notícia saíram da versão pública; o código não vem no pacote). Olhe antes de desenhar.

| O que ele faz | Como |
| --- | --- |
| Capa limpa | Pessoa real de foto, sorrindo, com sacolas (pose do assunto); a logo 3D da marca grande atrás dela; título embaixo e tarja. Nada mais |
| Uma imagem forte por slide | Cupom, lupa, escada de pílulas, caixa registradora, etiquetas, recorte com clipe, barra quente e frio. Uma peça só, simples, que se entende sem ler |
| Pouco texto | Título de 2 linhas, apoio de 2 linhas, tarja, fio. Média de 59 palavras por slide (régua em `copy.md`, seção 3) |
| Logo real nas peças | A logo plana do TikTok onde a marca é rótulo ("Nota do TikTok", a 1ª pílula) |
| Ritmo variado | 4 moldes nos 7 do meio: peça em cima, clássico, pílulas, recorte; a ordem do texto muda de slide para slide |
| Final que fecha a história | A mesma pessoa, agora do outro lado e como quem vende; a mesma logo, girada para o outro lado |

## O que a V4 faz e a gente copia o jeito (não a cara)

- **A imagem é do assunto**: a pessoa da notícia (foto real), o produto, a logo da marca em objeto 3D ou plana, nas cores da marca do assunto. O fundo continua o nosso.
- **Composição muda a cada slide**: título em cima com a peça embaixo; foto ocupando a metade de cima e o texto embaixo; pessoa recortada saindo pela borda com o texto do outro lado; um número enorme; um recorte de notícia.
- **A capa muda a cada carrossel só na posição**: título embaixo, em cima ou no meio; pessoa no centro, à esquerda ou à direita; foto real do assunto. Os elementos e as cores são sempre os do 02.
- **Pouca coisa por slide**: um título, um texto curto, uma imagem forte. Nada de painel de site. Limite medido em `copy.md`, seção 3.

## O que não fazer (reprovado)

- Fundo marinho e frase grande centralizada (`abrir(n, 'escuro')`): o motor recusa.
- Foto ocupando o slide de conteúdo com texto por cima (`abrir(n, 'foto')`): o motor recusa. Foto no conteúdo é em faixa (metade de cima), dentro da peça ou pessoa recortada ao lado do texto.
- Vários cartões, selos, rótulos, notas e setas disputando o olho.
- Repetir a composição de outro carrossel (capa, ordem dos slides, peças).

## Regras de variação

- Escreva no topo do `slides.py` a **direção de arte** do carrossel: molde da capa, ritmo de fundos, moldes principais, ordem do texto.
- Nos 7 slides do meio, **pelo menos 4 moldes diferentes**, e nunca o mesmo molde em dois slides seguidos.
- **A ordem muda**: em uns slides o título vem primeiro; em outros a foto, a pessoa, o número ou a notícia vêm antes e o título explica.
- **Ritmo de fundos** só com branco e azul, mas não precisa intercalar sempre: começar pelo azul, ou dois brancos seguidos, já muda.
- Título sempre à esquerda. Tamanhos: título 64, texto 34 (nada abaixo de 24).

## Moldes de conteúdo

| Molde | Como montar | Bom para |
| --- | --- | --- |
| **Clássico** | `manchete` em 244, `corpo`, peça de `PECA_Y` a `ATE`, `fio` | explicar com prova |
| **Metade foto** | `abrir(n, 'branco', foto_no_topo='foto.jpg', foto_ate=600, foco_y=...)`, `manchete(y=720)`, `corpo(y=...)` | foto real do fato, do lugar, do produto |
| **Pessoa saindo da borda** | `pessoa_solta(arquivo, cabelo, queixo, centro, cx=820, cabelo_y=430, rosto=420)`, `manchete(..., limite=600)`, `corpo(..., limite=600)` | gente da notícia, personagem do post |
| **Peça em cima** | peça de 152 a ~700, `manchete(y=~820)`, `corpo(y=...)` | quando a imagem é a notícia |
| **Número de impacto** | `palavra_de_impacto('R$ 7 BI', base=..., tam=180 a 240, fundo=AZUL ou None)` com título e texto curtos | quando o dado é a notícia |
| **Recorte de notícia** | `recorte_de_noticia('Reuters', 'manchete real da matéria', '13/11/2026', y=PECA_Y)` (a manchete é a do veículo, curta; nunca inventada) | mostrar que saiu na imprensa |
| **Dividido** | `manchete(..., limite=520)` e `corpo(..., limite=520)` numa coluna, peça em `x=560, w=440` | comparar, explicar um print |
| **Lista em pílulas** | 3 ou 4 linhas curtas, cada uma numa pílula sólida (`pc.forma` roundedRect + `pc.texto` 30 a 34) | as três perguntas, os três papéis |
| **Foto na peça** | `foto_na_peca(arquivo, ...)` no lugar da peça, crédito embaixo | foto real sem ocupar a faixa |

`manchete` aceita 1 a 3 linhas, `y`, `x` e `limite`. Peça, foto e pessoa nunca ficam por cima de texto.

## Capa e final: limpos como antes, só muda ONDE as coisas ficam

Regra do dono da marca (15/11): "A capa, independente de tudo, tem que ser limpa igual tava antes, apenas mudar aonde fica."
Os elementos e as cores da capa são sempre os do carrossel 02: foto (pessoa ou foto real do assunto), a logo, a linha pequena
branca com o risco azul, a palavra gigante branca em Oswald e a tarja azul (na capa) ou a chamada (no final). Objeto 3D
grande atrás da pessoa quando houver. Nada de palavra em tarja, palavra escura atrás da pessoa, selo, cartão ou texto a mais.

O que muda de um carrossel para o outro é só a posição:

| Posição | Como montar |
| --- | --- |
| **Título embaixo** (o do 02) | `foto_de_pessoa(..., escurecer='baixo')`, `titulo_de_foto(...)`, `tarja_da_capa(...)` |
| **Título em cima** | `foto_de_pessoa(..., escurecer='cima')` (a pessoa embaixo), `titulo_de_foto(..., base=~430)`, `tarja_da_capa(..., y=~460)` logo abaixo da palavra |
| **Título no meio** | `escurecer='baixo'` (degradê único e liso, nunca `'tudo'`), `titulo_de_foto(..., base=~760)`, tarja logo abaixo, pessoa no alto |
| **Pessoa à esquerda ou à direita** | `rosto_x=330` a `400` ou `680` a `750` (foto com parede sobrando), objeto 3D grande do outro lado, título embaixo ou em cima |
| **Foto real do assunto** | `foto_inteira(arquivo, foco_x, foco_y, zoom, escurecer=...)` (avião, prédio, executivo em evento) com o mesmo bloco de título, `credito(...)` |

Pessoa real da notícia (ex.: o dono da empresa citada) só em foto real (`material.md`). Pose sempre do assunto e diferente das outras capas: notebook, café, caixa, sacolas.
A capa e o final do mesmo carrossel combinam entre si. A capa de um carrossel não repete a posição, a pessoa e os objetos da capa de outro.
