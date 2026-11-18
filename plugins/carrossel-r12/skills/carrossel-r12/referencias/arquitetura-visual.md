# Arquitetura visual: para onde o olho vai

A planta que todo slide segue: onde cada coisa fica, quanto de respiro tem e por onde o olho passa.
Os números moram em `motor/planta.py` e o `motor/comum.py` já monta nessa planta. Você só decide a PEÇA.
Para ver o resultado aprovado: `exemplo/folha-pdf-seo.jpg` (peças em `exemplo/slides-pdf-seo.py`). Para conferir um carrossel com a régua por cima: `python3 motor/regua.py <pasta>`.

## 1. A rota do olho

**Slide de conteúdo.** O olho desce pela margem esquerda e sai pelo canto de baixo à direita.

| Ordem | O quê | Por quê |
| --- | --- | --- |
| 1º | Título | É a maior letra e fica no canto de cima à esquerda, onde a leitura começa |
| 2º | Frase em tarja | Bloco de cor chapada: é lida até por quem pula o texto |
| 3º | A peça (gráfico, busca desenhada, print de trabalho real) | É a prova. Fica no centro e começa sempre na mesma altura |
| 4º | O fio | A pergunta que puxa o próximo slide e o botão redondo, no canto onde a leitura termina |

**Slide de foto (capa e final).**

| Ordem | O quê | Por quê |
| --- | --- | --- |
| 1º | O rosto | Rosto segura o olhar |
| 2º | Para onde a pessoa olha | Na capa ela olha para o que importa (o objeto 3D, o celular), logo acima do título |
| 3º | A palavra gigante | O maior elemento do slide |
| 4º | A tarja (capa) ou a chamada (final) | Fecha a frase |

Regras que saem daí:

- **Uma coisa só chama mais que as outras em cada slide.** Tamanho e contraste decidem quem é visto primeiro. Se duas coisas brigam, uma diminui.
- **Na capa a pessoa olha para o que importa** (a lupa, o pino de mapa, o celular). O leitor segue o olhar do rosto da foto.
- **No final a pessoa olha para a câmera.** O rosto de frente segura a atenção nele mesmo, e a chamada vem logo abaixo.
- **Título em cima à esquerda, saída embaixo à direita.** É o caminho natural da leitura e combina com o gesto de arrastar.
- **A peça prova o que o título disse.** Se o texto fala de uma coisa, ela aparece na peça, grande o bastante para ler no celular.

## 2. A planta (slide de 1080 x 1440)

| Guia | Altura | O que é |
| --- | --- | --- |
| Margem | 80 de cada lado | Tudo começa em 80 e termina em 1000 |
| Logo | 56 a 120 | Sempre no canto de cima à esquerda. Arroba à direita nos slides de conteúdo |
| Título | 1ª linha de base em 244, a 2ª uns 92 px abaixo | Oswald 82, duas linhas (no exemplo, 92 a partir de y = 316) |
| Texto | logo abaixo do título (o motor calcula) | 34 px, duas linhas, só quando indispensável |
| Frase em tarja | logo abaixo do texto | 34 px, negrito |
| Peça | até 1264 (`ATE`) | 64 px abaixo do último texto. Nenhuma peça passa de 1264. No exemplo a imagem começa em 560 |
| Fio | 1344 | 80 px abaixo da peça. A faixa do rodapé vai de 1296 a 1392 |

Slide sem texto de apoio (o padrão aprovado da R12: título, uma imagem, o fio): a peça sobe para logo abaixo do título.

Slides de foto: cabelo começa em 48, rosto com 540 de altura, palavra gigante assenta em 1272 e a
tarja ou a chamada ocupa a faixa do rodapé (1296 a 1392). A foto escurece de 800 para baixo, para o título aparecer.

## 3. Espaçamento

Uma régua só, em múltiplos de 8: **8, 16, 24, 40, 48, 64, 80**.

- 80: margens, logo até o título, peça até o fio.
- 64: tarja até a peça.
- 48: entre cartões e entre dois prints.
- 40: por dentro de cartão e de lista (`MIOLO`).
- 24: entre texto e a peça colada nele (pergunta e fio, palavra e tarja).

Texto nunca encosta em outra peça. Dois rótulos lado a lado ficam grudados: use um rótulo só.

## 4. Tipografia limpa

- **Oswald** (condensada) no título das páginas (82 a 92, peso 600), na palavra gigante da capa e do final e no número de impacto dentro da peça.
- **IBM Plex Sans** no resto: texto normal (34), frase em tarja em negrito (34), pergunta do fio (34), rótulos da peça.
- Título em tamanho de manchete. Gigante (palavra de 180 a 256) só na capa, no final e no número de impacto.
- Nada abaixo de 24 px. O slide aparece no celular com cerca de um terço do tamanho.
- Quebra de linha escolhida à mão, sem palavra sozinha na última linha.
- Dentro da peça desenhada: nome 34 ou 35 em negrito, mensagem 28 ou 29, hora 25. Rótulo que aponta para print: 30, peso 600.

## 5. Cor e contraste

- Fundos intercalados: capa com foto, claro, escuro, claro, escuro... e final com foto. O motor escolhe pelo número do slide (`abrir(n, 'claro')` ou `'escuro'` para deixar escrito).
- Fundo claro (quase branco) leva peça escura. Fundo escuro (`#161616` com toque de verde) leva peça clara ou verde. Escuro nunca em cima de escuro, claro nunca em cima de claro.
- Print de trabalho real (site de cliente, campanha) leva moldura branca fina nos dois fundos: `print_do_sistema` já põe.
- Vermelho (`#D92D34`) só nos slides do problema, e só em cima de claro: `abrir(n, destaque=VERMELHO)`.
- Verde `#95db30` é o destaque, a tarja e o botão no escuro. No claro o destaque de texto é o verde de leitura `#3f7a0f` (o `#95db30` não dá leitura no claro). Escuro `#161616` é o título no claro.
- Fundo nunca chapado: degradê leve com grão. Já vem pronto no `abrir`.

## 6. Ícone, objeto e logo

- **Em foto:** objeto 3D grande, ATRÁS da pessoa e meio escondido por ela, um de cada lado, os dois virados para o meio. Nunca pequeno e boiando na frente, nunca com brilho em volta. Como: `foto_de_pessoa(..., atras=funcao)`.
- **No lugar de número:** lista de itens leva ícone 3D grande (120 px) ou ícone de traço (dicionário `I` em `exemplo/slides-pdf-seo.py`), nunca "1, 2, 3", "01" ou bolinha numerada.
- **A logo da R12** (símbolo verde e "company") não gira, não deforma e não leva caixa nem faixa atrás. No escuro é a versão com "company" claro. `topo` já faz.
- **Nada por cima de foto ou de print:** sem selo, etiqueta, bolinha, cartão ou seta em cima. Para explicar um print: rótulo do lado de fora e linha fina até o ponto (`linha_fina`).

## 7. O fio: o rodapé da R12

No lugar do botão em aba das agências, a R12 tem o **fio**: uma linha fina que corre de ponta a
ponta na mesma altura em todos os slides, como o fio de uma conversa.

- A pergunta que puxa o próximo slide assenta no fio, à esquerda.
- O fio termina num botão redondo no canto de baixo à direita, onde a leitura acaba e o dedo começa a arrastar.
- Ele sai pela beirada direita e entra pela esquerda do slide seguinte (`primeiro=True` no slide 2, onde ele nasce).
- No último slide o fio chega na chamada e para ali.

## 8. Juntar um slide no outro (emenda)

Uma peça começa na beirada direita de um slide e continua na esquerda do seguinte, na mesma altura e no mesmo tamanho. Dá vontade de arrastar.

- Objeto 3D: `objeto(nome, arquivo, 1080, y, lado)` num slide e `objeto(nome, arquivo, 0, y, lado)` no seguinte.
- Print largo: `print_do_sistema(..., x=X, w=W)` num slide e `x=X - 1080` no seguinte, com o mesmo recorte.
- A peça que atravessa fica POR CIMA do que está no slide (atrás, fica tapada) e não encosta em texto.
- Confira no `planta/panorama.jpg`: os slides aparecem emendados.

Uma ou duas emendas por carrossel. Ex.: a lupa 3D da capa continuando no slide 2.

## 9. O que é fixo e o que muda

A identidade (logo, fontes, cores, margens, o fio) é o que faz o carrossel ser reconhecido como da R12. A planta acima é o molde clássico, não o único: cada carrossel tem layout, ritmo de fundos e ordem de texto próprios (`moldes.md`). Dentro dela, cada carrossel é novo:
personagem, pose, lado em que a pessoa fica, objetos 3D e o desenho das peças mudam sempre (`material.md`, "Inovar a cada carrossel").
Inovar é mudar composição, ritmo e ordem mantendo a hierarquia: uma coisa só chama mais que as outras, texto legível, o fio no rodapé.

## De onde saiu

- [Palcu, Sudkamp e Florack (2017): olhar do rosto no anúncio leva a atenção ao produto](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5454066/)
- [Sajjacholapunt e Ball (2014): rosto de frente segura a atenção nele mesmo](https://pmc.ncbi.nlm.nih.gov/articles/PMC3941030)
- [Ramotion: princípios de hierarquia visual](https://www.ramotion.com/blog/visual-hierarchy/)
- [UX Collective: o diagrama de Gutenberg hoje](https://uxdesign.cc/gutenberg-modern-day-ux-14ac545e151c)
- [Figma, Design Systems: espaço, grades e layouts](https://www.designsystems.com/space-grids-and-layouts/)
- Referências de estilo: carrosséis de outras agências no Instagram (não vêm no pacote: são de terceiros). Inspiração, não cópia: o fio existe porque o botão em aba era cópia.
