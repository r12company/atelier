# Design system do Convello (posts de Instagram)

A identidade que se repete em todo post: carrossel, card e stories. Dá para montar no Figma só com esta página; o motor (`motor/comum.py`, `motor/planta.py`) usa exatamente estes números.
Prancha visual: `design-system/prancha.jpg`. Os recortes de exemplo estão em `design-system/` (tirados dos slides aprovados).

## 1. Cores

| Nome | Hex | Quando usar |
| --- | --- | --- |
| Azul Convello | `#005DE1` | destaque: 2ª linha do título no fundo branco, tarjas, fio e botão no branco, tarja da capa, chamada |
| Azul Profundo | `#0B1423` | título no fundo branco |
| Texto | `#2A3445` | texto de apoio no fundo branco |
| Cinza | `#5B6474` | arroba e crédito no fundo branco, rótulos secundários |
| Branco | `#FFFFFF` | título e fio no fundo azul, tarja no fundo azul (com letra azul), moldura de print |
| Texto no azul | `#F1F6FF` | texto de apoio no fundo azul |
| Vermelho | `#D92D34` | só nos slides do problema e só no fundo branco |
| Escuro das telas | `#1C1C1F` | fundo de peça escura (lista, cartão) no fundo branco, fundo atrás do print |
| Bege de conversa | `#EBE4D8` | peça clara de aplicativo de mensagem no fundo azul |
| Risco da capa | `#2E86FF` | o risco embaixo da linha pequena da capa |
| Escurecer foto | `#04070F` | degradê que escurece a foto onde vai o título (0% a 97% de opacidade) |

Fundos (nunca chapados: degradê leve e grão):

| Fundo | Degradê | Grão |
| --- | --- | --- |
| Branco | linear a -62°: `#FFFFFF` 0%, `#F5F6F8` 45%, `#D8DDE6` 100% | camada Sobrepor (Overlay) cinza 50% com ruído de 3%, monocromático |
| Azul | radial, escala 140%, centro 15% abaixo do meio: `#3D8BF7` 0%, `#2B7AEF` 25%, `#1A69E4` 40%, `#1260DC` 60%, `#0A4BC4` 100% | ruído de 8% |
| Foto (capa e final) | a foto inteira, escurecida só onde vai o título | ruído de 9% |

Contraste: peça escura no fundo branco, peça clara no fundo azul. Azul em cima de azul e claro em cima de claro, nunca.

## 2. Tipografia

Só duas fontes (arquivos em `fontes/`, licença OFL): **IBM Plex Sans** em tudo e **Oswald** só na palavra de impacto.

| Papel | Fonte | Tamanho | Peso | Espaço entre letras | Entrelinha |
| --- | --- | --- | --- | --- | --- |
| Título (manchete) | IBM Plex Sans | 64 | 700 | -15 (Figma: -1,5%) | 80 entre linhas de base |
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

## 4. Componentes

| Componente | Medidas | Exemplo |
| --- | --- | --- |
| **Logo e arroba** | logo completa (símbolo e "Convello") com 64 de altura, em x = 80, meio no y da guia; contorno preto de 1 px (`#05080F`). No fundo azul ou na foto escura, a versão branca com sombreado (`marca/convello-logo-escuro-64.png` em tons de 68% a 100% de branco). Arroba `@convello.com.br` alinhada à direita em x = 1000, linha de base 9 px abaixo do meio da logo. Sem caixa, faixa ou sombra atrás | `design-system/logo.jpg` |
| **Título** | 2 linhas; a 2ª é o destaque. No branco: destaque em azul. No azul: destaque numa tarja branca com letra azul (altura 76, folga lateral 20, cantos 10) | `design-system/titulo.jpg` |
| **Texto e frase em tarja** | 2 linhas de apoio e a tarja: altura 56, cantos 8, folga lateral 16; azul com letra branca no fundo branco, branca com letra azul no fundo azul. Texto e tarja leem como uma frase | `design-system/texto-e-tarja.jpg` |
| **O fio** | linha de 3 px de ponta a ponta na altura do fio; pergunta à esquerda em x = 80; a linha recomeça 24 px depois do texto até um botão redondo de 72 (centro em x = 964) com seta fina de 4 px; depois sai pela beirada. No slide 2 não vem da esquerda. Azul no branco (seta branca), branco no azul (seta azul) | `design-system/fio.jpg` |
| **Moldura de print** | caixa de cantos 30 com moldura branca de 8 px e sombra (`#001230`, 30%, distância 20, tamanho 50); dentro, fundo `#1C1C1F` de cantos 22 e o print recortado no tamanho da caixa. Rótulo do lado de fora (30/600) e linha fina de 3 px até o ponto; nada por cima do print | `design-system/print-com-moldura.jpg` |
| **Objeto 3D** | plástico azul `#0A6BF0`, grande (300 a 480 px), atrás da pessoa e meio escondido por ela, um de cada lado, virados para o meio; sombra `#001230` 38%, distância 14, tamanho 26. Nunca pequeno boiando na frente | `design-system/objeto-3d.jpg` |
| **Ícone no lugar de número** | ícone 3D azul de 120 px, em painel branco de cantos 30, linhas de 176 de altura separadas por fio de 2 px `#DDE3EC`; texto 44/700 com o destaque em azul | `design-system/icone-3d.jpg` |
| **Título da capa** | linha pequena (64/600, risco `#2E86FF` de 6 px embaixo), palavra gigante em Oswald, tarja azul de 96 de altura, cantos 16, folga 40, letra branca 64/700 | `design-system/capa-titulo-e-tarja.jpg` |
| **Chamada do final (botão)** | verbo em branco, a palavra numa tarja azul de 96 de altura (cantos 16, folga 32) e um botão redondo branco de 72 com seta azul para baixo; o fio entra pela esquerda e para na chamada | `design-system/chamada.jpg` |
| **Pílula** | retângulo de cantos totalmente redondos (raio = metade da altura), fundo sólido (escuro no branco, branco ou bege no azul), texto 30 a 34/600 com folga de 28 a 56. Nunca contorno transparente | prova do card em `exemplo/prova/` |

## 5. Fundos permitidos

- Slide de conteúdo: só **branco** e **azul** (com o degradê e o grão acima). O motor recusa marinho e foto inteira com texto por cima.
- Capa e final: **foto** (pessoa de estúdio recortada com objeto 3D atrás, ou foto real com crédito), escurecida num degradê único só onde vai o título.
- Faixa de foto no alto de um slide de conteúdo (até y = 600), com a logo branca por cima: pode.
- Card: branco, azul ou foto. Stories: os mesmos.

## 6. Nunca faça

| Nunca | Por quê |
| --- | --- |
| Travessão, emoji no slide, contador de slide (2/9), numeração (01, bolinha 1 2 3) | Reprovados um a um: marca de IA, poluição, cara de apresentação |
| Fonte fora de IBM Plex Sans e Oswald (Sora, Fira Sans, Anton) | "Cara de site" |
| Título gigante em todo slide | Gigante só na capa e no final; o resto é manchete de 64 |
| Glow, brilho espalhado, fundo chapado ou marinho | "Poluído", "cru", "parece site" |
| Caixa, faixa ou contorno branco atrás da logo; logo só com o símbolo | Reprovado ("pqp", "podre") |
| Selo, cartão, bolinha ou seta por cima de foto ou de print | Esconde a prova; rótulo vai por fora, com linha fina |
| Botão em aba no rodapé | Era cópia de outra agência; o Convello tem o fio |
| Escurecer a foto inteira ou em faixas | "Poluído, essa sombra" |
| Tela de sistema desenhada ou print antigo | O post mostra o produto de verdade |
| Mesmo personagem, pose ou capa de outro post | Cada post inova; só a identidade se repete |
| Texto encostado em outra peça, letra abaixo de 24 | Ilegível no celular |
| Mais de 75 palavras num slide de carrossel (50 no card e nos stories) | "Vai poluir e ficar difícil de ler" |

Detalhe e histórico de cada reprovação: `referencias/reprovado.md`. Os formatos: `referencias/formatos.md`.
