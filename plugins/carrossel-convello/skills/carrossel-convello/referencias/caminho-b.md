# Caminho B: montar à mão no Photoshop ou no Figma

Use quando o Atelier não roda neste computador (o `checar.py` disse o que falta) ou no Claude.ai, onde o PhotoCraft não instala.
O Claude continua fazendo roteiro, legenda, pedidos de imagem e o plano de cada slide; a produtora monta seguindo a planta abaixo.
Os números são os mesmos do `motor/planta.py`: um slide montado à mão tem de cair nas mesmas guias.

## O que o Claude entrega no caminho B

Para cada slide, uma ficha em `<carrossel>/plano.md`:

```markdown
## Slide 3 (fundo azul, molde clássico)
Título: Você viu. / [destaque] Mas esqueceu de responder.
Texto: Não foi falta de interesse. A mensagem ficou / para depois. Quando você lembra,
Tarja: o cliente pode já ter procurado outra empresa.
Peça: conversa clara (bege #EBE4D8), de 80,592 a 1000,1264, com ...
Fio: E se tiver uma equipe?
Camadas: FUNDO, FUNDO-GRAO, LOGO, ARROBA, TITULO-1, TITULO-2, TEXTO-1, TEXTO-2, TEXTO-3-TARJA, PECA-..., FIO-...
```

## Documento

- 1080 x 1440 px (3:4) ou 1080 x 1350 px (4:5), 72 ppi, RGB. Um arquivo por slide, ou uma prancheta por slide no Figma.
- Exportar PNG em 1080 de largura (no Figma, 1x) e guardar o PSD ou o arquivo do Figma com as camadas nomeadas.

## Guias (crie todas)

| Guia | 3:4 (1440) | 4:5 (1350) |
| --- | --- | --- |
| Margens laterais | x = 80 e x = 1000 | igual |
| Logo | de y = 56 a 120 (meio em 88), em x = 80 | igual |
| Título, linhas de base | 244 e 324 | igual |
| Texto de apoio, linhas de base | 400 e 448 | igual |
| Frase em tarja | 472 a 528 | igual |
| Peça | 592 a 1264 | 592 a 1174 |
| Fio | 1344 (faixa do rodapé de 1296 a 1392) | 1254 |
| Foto: cabelo começa | 48 | 48 |
| Foto: rosto (cabelo ao queixo) | 540 de altura | 500 |
| Foto: escurece a partir de | 800 | 710 |
| Foto: palavra gigante assenta | 1272 | 1182 |
| Foto: tarja ou chamada | 1296 a 1392 | 1206 a 1302 |

Respiros sempre da régua de 8: 8, 16, 24, 40, 48, 64, 80 (`arquitetura-visual.md`, seção 3).

## Letras

| Onde | Fonte | Tamanho | Peso | Espaço entre letras |
| --- | --- | --- | --- | --- |
| Título | IBM Plex Sans | 64 | 700 | -15 |
| Texto de apoio | IBM Plex Sans | 34 | 400 | 0 |
| Frase em tarja | IBM Plex Sans | 34 | 700, dentro de uma tarja de 56 de altura, cantos de 8 | 0 |
| Pergunta do fio | IBM Plex Sans | 34 | 600 | 0 |
| Arroba | IBM Plex Sans | 27 | 500 | 0 |
| Palavra gigante (capa e final) | Oswald | até 256, enchendo de 80 a 1000 | 700 | 0 |
| Linha pequena acima da palavra | IBM Plex Sans | 64 | 600, com um risco de 6 px embaixo | -10 |
| Tarja da capa | IBM Plex Sans | 64 | 700, tarja de 96 de altura, cantos de 16 | -5 |

Nada abaixo de 24 px. As fontes estão em `fontes/` da skill (instale antes de abrir o Photoshop ou o Figma).
No Figma, o espaço entre letras -15 do motor corresponde a -1,5%.

## Cores e fundos

As cores, os degradês e o grão de cada fundo estão no `motor/comum.py` (função `abrir`) e no `motor/pc.py`: copie os valores de lá.
Fundo nunca chapado: degradê leve e uma camada de grão por cima (Photoshop: camada cinza 50% em modo Sobrepor com Filtro > Ruído > Adicionar ruído, uns 3% no claro e 8% no escuro).
A logo vem pronta em `marca/` (`*-64.png` tem a altura do topo do slide).

## O fio

Linha de 3 px na altura do fio, de ponta a ponta. A pergunta assenta nela à esquerda (em x = 80); a linha recomeça 24 px depois do texto e vai até um botão redondo de 72 px encostado na margem direita (centro em x = 964), com uma seta fina dentro; depois do botão a linha sai pela beirada. No slide 2 ela não vem da esquerda; do 3 em diante entra pela beirada esquerda até 24 px antes do texto.

## Depois de montar

Exporte os PNG como `png/01.png`, `png/02.png`... na pasta do carrossel e peça ao Claude a conferência: ele olha cada slide contra `reprovado.md` e a planta. O `conferir.py` exige os PSD e o `planta.json` do motor, então no caminho B a conferência é no olho.
