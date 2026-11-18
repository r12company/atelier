# Design system da R12 Company (posts de Instagram)

A identidade que se repete em todo post: carrossel, card e stories. Dá para montar no Figma só com esta página; o motor (`motor/comum.py`, `motor/planta.py`) usa exatamente estes números. Quem é a marca e o tom: `referencias/marca.md`.
Prancha visual: `design-system/prancha.jpg`. Os recortes de exemplo estão em `design-system/` (tirados dos slides aprovados da proposta de SEO).

## 1. Cores

| Nome | Hex | Quando usar |
| --- | --- | --- |
| Verde Resultado | `#95db30` | destaque no fundo escuro, tarjas no escuro (letra escura), fio e botão no escuro, tarja da capa, chamada, objeto 3D e ícones |
| Verde de leitura | `#3f7a0f` | destaque de texto no fundo claro (o `#95db30` não dá leitura no claro) |
| Escuro | `#161616` | título no fundo claro, tarja no fundo claro (com letra verde), fio no claro. Base do manual: `#18211b` |
| Texto | `#2f3d33` | texto de apoio no fundo claro |
| Claro Confiança | `#e7ffef` | título no fundo escuro, cartão claro sobre o escuro |
| Texto no escuro | `#cfe3d4` | texto de apoio no fundo escuro |
| Cinza | `#5d7064` | arroba e crédito no fundo claro |
| Vermelho | `#D92D34` | só nos slides do problema e só no fundo claro |
| Escurecer foto | `#0b120d` | degradê que escurece a foto onde vai o título |

Fundos (nunca chapados: degradê leve e grão):

| Fundo | Degradê | Grão |
| --- | --- | --- |
| Claro | linear a -62°: `#FBFCFB` 0%, `#F2F5F2` 45%, `#E0E6E1` 100% (o verde-água foi achado "poluído") | ruído de 3% em camada Sobrepor |
| Escuro | radial, escala 140%, centro 15% abaixo do meio: `#1F2A1F` 0%, `#1B201B` 30%, `#171917` 60%, `#131313` 100% | ruído de 8% |
| Foto (capa e final) | a foto inteira, escurecida só onde vai o título | ruído de 9% |

Contraste: peça escura no fundo claro, peça clara (`#e7ffef`) ou verde no fundo escuro.

## 2. Tipografia

Duas fontes (arquivos em `fontes/`, licença OFL): **Oswald** no título e na palavra de impacto (aprovado em 16/11/2026: "mais limpo e bonito") e **IBM Plex Sans** no texto. A Ouma Devanagari do manual só aparece dentro da logo (já pronta em PNG).

| Papel | Fonte | Tamanho | Peso | Espaço entre letras | Entrelinha |
| --- | --- | --- | --- | --- | --- |
| Título (manchete) | Oswald | 82 | 600 | 0 | 92 entre linhas de base |
| Texto de apoio | IBM Plex Sans | 34 | 400 | 0 | 48 |
| Frase em tarja | IBM Plex Sans | 34 | 700 | 0 | |
| Pergunta do fio | IBM Plex Sans | 34 | 600 | 0 | |
| Arroba | IBM Plex Sans | 27 | 500 | 0 | |
| Palavra gigante (capa, final) | Oswald | até 256 (enche de 80 a 1000) | 700 | 0 | |
| Linha pequena da capa | IBM Plex Sans | 64 | 600 | -10 | |
| Tarja da capa | IBM Plex Sans | 64 | 700 | -5 | |
| Chamada do final | IBM Plex Sans | verbo 60/500, palavra 64/700 | | 0 | |
| Palavra de impacto na peça | Oswald | 180 a 320 | 700 | 0 | |
| Dentro da peça | IBM Plex Sans | nome 34 a 35/700, mensagem 28 a 29, hora 25, rótulo de print 30/600 | | 0 | |
| Crédito e fonte | IBM Plex Sans | 24 | 400 a 500 | 0 | |

**Menor letra: 24 px.** O post aparece no celular com um terço do tamanho. Espaçamento exagerado entre letras ("E S P A Ç O") foi reprovado: o máximo é 5.

## 3. Grade e margens

Margem de 80 dos dois lados (conteúdo de x = 80 a 1000). Respiros só da régua de 8: **8, 16, 24, 40, 48, 64, 80**.

| Guia (y, em px) | Carrossel 3:4 (1080 x 1440) | Carrossel e card 4:5 (1080 x 1350) | Stories 9:16 (1080 x 1920) |
| --- | --- | --- | --- |
| Logo (de / meio / até) | 56 / 88 / 120 | 56 / 88 / 120 | 250 / 282 / 314 |
| Título, linhas de base | 244 e 324 | 244 e 324 | 438 e 518 |
| Texto de apoio, linhas de base | 400 e 448 | 400 e 448 | 594 e 642 |
| Frase em tarja | 472 a 528 | 472 a 528 | 666 a 722 |
| Peça | 592 a 1264 | 592 a 1174 | 786 a 1360 |
| Peça sem texto de apoio começa em | 396 | 396 | 590 |
| Fio (faixa do rodapé) | 1344 (1296 a 1392) | 1254 (1206 a 1302) | 1440 (1392 a 1488) |
| Card: a peça desce até | 1360 | 1270 | (card não usa 9:16) |
| Foto: cabelo começa / rosto | 48 / 540 | 48 / 500 | 250 / 600 |
| Foto: escurece a partir de | 800 | 710 | 1000 |
| Foto: palavra gigante assenta | 1272 | 1182 | 1368 |
| Foto: tarja ou chamada | 1296 a 1392 | 1206 a 1302 | 1392 a 1488 |

Stories: nada importante acima de 250 nem abaixo de 1500 (o Instagram cobre).

Na R12 o título é mais alto (Oswald 82): as linhas de base ficam em 244 e 336, e o texto de apoio começa logo abaixo (o motor calcula).

## 4. Componentes

| Componente | Medidas | Exemplo |
| --- | --- | --- |
| **Logo e arroba** | logo completa (símbolo "R12" verde e "company") com 64 de altura, em x = 80, meio no y da guia: `marca/r12-logo-64.png` no claro, `marca/r12-logo-branca-64.png` no escuro. Arroba `@r12_company` (ou `r12company.com` em PDF) alinhada à direita em x = 1000. Sem caixa atrás | `design-system/logo.jpg` |
| **Título** | 2 linhas em Oswald 82/600; a 2ª é o destaque. No claro: destaque em `#3f7a0f`. No escuro: destaque numa tarja verde com letra escura (altura 97, folga lateral 26, cantos 13) | `design-system/titulo.jpg` |
| **Texto e frase em tarja** | 2 linhas de apoio (só quando indispensável) e a tarja: altura 56, cantos 8, folga 16; escura com letra verde no claro, verde com letra escura no escuro | |
| **O fio** | igual ao do Convello: linha de 3 px, pergunta à esquerda, botão redondo de 72 (centro em x = 964) com seta. Escuro com seta verde no claro; verde com seta escura no escuro | `design-system/fio.jpg` |
| **Moldura de print** | caixa de cantos 30, moldura branca de 8 px, sombra (`#0b120d`, 30%, distância 20, tamanho 50). Print só de trabalho real da R12, com autorização do cliente | |
| **Objeto 3D** | plástico verde `#95db30` (lupa, pino de mapa), grande, atrás da pessoa ou sozinho no meio do slide; sombra `#0b120d` | `design-system/objeto-3d.jpg` |
| **Pílula e ícone de traço** | cartões-pílula de cantos 28: claros (`#e7ffef`) no escuro, o último verde; ícone de traço de 1,5 a 2 px (estilo Lucide) à esquerda; setas finas verdes entre elas. Ícones em `exemplo/slides-pdf-seo.py` (dicionário `I`) | `design-system/pilulas-e-icones.jpg` |
| **Peça de dado** | gráfico de barras, linha no tempo, antes x depois: verde para o que importa, `#2a2f2a` para o resto, nota 30/500 em verde, rótulos em Oswald 28 a 36 | `design-system/peca-grafico.jpg` |
| **Título da capa** | linha pequena (64/600, risco verde de 6 px), palavra gigante em Oswald, tarja verde de 96 de altura com letra escura 64/700 | `design-system/capa-titulo-e-tarja.jpg` |
| **Chamada do final (botão)** | "Fale com a" ou "Comente" em branco, a palavra R12 numa tarja verde com letra escura e um botão redondo verde de 72 com seta escura | `design-system/chamada.jpg` |

## 5. Fundos permitidos

- Slide de conteúdo: só **claro** e **escuro** (com o degradê e o grão acima). O motor recusa marinho e foto inteira com texto por cima.
- Capa e final: **foto** (pessoa de estúdio recortada com objeto 3D atrás, ou foto real com crédito), escurecida num degradê único só onde vai o título.
- Faixa de foto no alto de um slide de conteúdo (até y = 600), com a logo branca por cima: pode.
- Card: claro, escuro ou foto. Stories: os mesmos.

## 6. Nunca faça

| Nunca | Por quê |
| --- | --- |
| Travessão, emoji no slide, contador de slide (2/9), numeração (01, bolinha 1 2 3) | Reprovados um a um: marca de IA, poluição, cara de apresentação |
| Fonte fora de Oswald e IBM Plex Sans | "Cara de site" |
| Verde `#95db30` como letra no fundo claro | Não dá leitura: use `#3f7a0f` |
| Fundo verde-água ou fundo de ondas do manual no slide de conteúdo | "Poluído"; o fundo é o do motor, limpo |
| Glow, brilho espalhado, fundo chapado ou marinho | "Poluído", "cru", "parece site" |
| Caixa, faixa ou contorno branco atrás da logo; logo só com o símbolo | Reprovado ("pqp", "podre") |
| Selo, cartão, bolinha ou seta por cima de foto ou de print | Esconde a prova; rótulo vai por fora, com linha fina |
| Botão em aba no rodapé | Era cópia de outra agência; a identidade tem o fio |
| Escurecer a foto inteira ou em faixas | "Poluído, essa sombra" |
| Tela de sistema desenhada ou print antigo | O post mostra trabalho de verdade |
| Mesmo personagem, pose ou capa de outro post | Cada post inova; só a identidade se repete |
| Texto encostado em outra peça, letra abaixo de 24 | Ilegível no celular |
| Mais de 75 palavras num slide de carrossel (50 no card e nos stories) | "Vai poluir e ficar difícil de ler" |

Detalhe e histórico de cada reprovação: `referencias/reprovado.md`. Os formatos: `referencias/formatos.md`.
