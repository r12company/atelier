# O motor: como montar no PhotoCraft

O motor de montagem se chama Atelier. Ele comanda o PhotoCraft (um "Photoshop" de código aberto, de github.com/storytold/photocraft, licença MIT ou Apache-2.0) pela linha de comando e entrega
cada slide em PSD com camadas nomeadas (`psd/`) e em PNG para postar (`png/`). Modelos: `exemplo/prova/slides.py` (monta sem imagem nenhuma) e as peças de `exemplo/slides-pdf-seo.py` (código de consulta: as imagens não vêm no pacote).

## Formato

`ALTURA = 1350` numa linha do `slides.py` monta em 4:5 (1080 x 1350); sem a linha, 3:4 (1080 x 1440).
No 4:5 o topo é igual e tudo de baixo sobe 90 px: a peça vai de 592 a 1174, o fio fica em 1254 e o rosto da foto tem 500.
Use as constantes (`PECA_Y`, `ATE`, `FIO_Y`, `TARJA_Y`, `ALTURA`), nunca o número escrito: assim o slide serve nos dois formatos.

## Comandos

```bash
M=${CLAUDE_SKILL_DIR}/motor
python3 $M/checar.py                              # o computador consegue montar? diz o que falta
PREVIA=1 python3 $M/montar.py <carrossel> 1       # monta só a capa, em <carrossel>/previa/ (para olhar e ajustar)
python3 $M/montar.py <carrossel>                  # monta todos e faz a folha.jpg (10 slides: uns 20 segundos com cache, uns 45 na primeira vez)
python3 $M/regua.py <carrossel>                   # planta/: folha-com-regua.jpg, rotas.jpg e panorama.jpg
python3 $M/conferir.py <carrossel>                # conferência final: arquivos, ordem, roteiro e legenda
python3 $M/regua.py foto <arquivo>                # régua em cima de uma foto, para medir cabelo, queixo e centro
```

`<carrossel>` é a pasta (ou só o nome dela) dentro de `$CARROSSEIS`, por exemplo `r12-03-anuncio-sem-site`.
O PhotoCraft só lê e grava dentro de `$CARROSSEIS`.

## A pasta de um carrossel

```
$CARROSSEIS/r12-NN-tema/
  roteiro.md      o roteiro encaixado na planta          slides.py     os slides (SLIDES = {1: s1, ...})
  pedidos-de-imagem.md  prompts para o Gemini/ChatGPT     copy.md       a copy da peça (legenda, alt, textos)
  recortes/       prints já recortados para a peça       geradas/      fotos e objetos gerados para este carrossel
  png/ psd/       o que o motor grava                    folha.jpg planta/ planta.json   idem
```

## O esqueleto de cada slide

```python
from comum import *   # no exemplo os nomes vêm um a um; os dois jeitos funcionam

def s1():                                   # CAPA
    abrir_foto(1)

    def atras():                            # objetos 3D verdes entre a parede e a pessoa
        objeto('LUPA', 'lupa-3d.png', 940, 470, 480, 14)
        objeto('PINO', 'pino-3d.png', 130, 720, 220, -12)

    foto_de_pessoa('dona-capa-lisa.png', cabelo=165, queixo=495, centro=345, atras=atras, rosto_x=440, rosto=460)
    topo('branco', arroba=False)
    titulo_de_foto('Seu anúncio traz gente', 'PARA ONDE?', 190)
    tarja_da_capa('pense antes de pagar')
    fechar(1)

def s2():                                   # CONTEÚDO (par = claro, ímpar = escuro: o motor escolhe)
    abrir(2)
    fim = manchete(['A pessoa viu o anúncio', '!e clicou.'], y=316, tam=92)
    ...                                     # A PEÇA, de 64 px abaixo do título (fim) até ATE (1264), de MARGEM (80) a 1000
    fio('E depois do clique?', primeiro=True)
    fechar(2)

def s10():                                  # FINAL
    abrir_foto(10)
    foto_de_pessoa('dona-final-lisa.png', cabelo=170, queixo=500, centro=360, rosto_x=420)   # medidas: regua.py foto
    topo('branco', arroba=False)
    titulo_de_foto('Anúncio bom precisa de', 'UM DESTINO', 190)
    chamada('Fale com a', 'R12')
    fechar(10)

SLIDES = {1: s1, 2: s2, 10: s10}
```

Nunca desenhe à mão o que o motor já faz (fundo, logo, título, texto, tarja, fio, moldura de print, enquadramento de foto):
é ali que mora o padrão aprovado. Mexer no `comum.py` ou no `planta.py` muda TODOS os carrosséis: só com pedido do dono da marca.

## Peças fixas (`comum.py`)

| Função | O que faz |
| --- | --- |
| `abrir(n, qual=None, destaque=None)` | Slide de conteúdo: fundo do tema, logo e arroba. O motor escolhe o fundo pelo número (par claro, ímpar escuro); `qual` é opcional (`'claro'` ou `'escuro'`; `'branco'` e `'azul'` são os nomes antigos e valem igual). `destaque=VERMELHO` nos slides do problema (só no claro) |
| `abrir_foto(n)` | Slide de foto: a capa (1) e o final (último) |
| `manchete([l1, l2], y=TITULO_Y, tam=82)` | Título em Oswald (82 a 92), 1 a 3 linhas. `!` no começo = linha de destaque (verde de leitura no claro, tarja verde no escuro). `[trecho]` destaca um pedaço. Devolve onde o título acaba |
| `corpo([l1, l2, '!tarja'])` | Texto de apoio. Linha com `!` vira a frase em tarja |
| `fio(pergunta, primeiro=False)` | O rodapé. `primeiro=True` só no slide 2 |
| `print_do_sistema(arquivo, apelido, y=PECA_Y, ate=ATE, x=MARGEM, w=920, gravidade=None, prefixo='PRINT')` | Print de trabalho real (com autorização do cliente) com moldura branca. `arquivo` em `recortes/`. Dois prints no mesmo slide: `prefixo` diferente |
| `foto_de_pessoa(arquivo, cabelo, queixo, centro, atras=None, rosto_x=540, rosto=540)` | Foto de pessoa no slide todo. Use a `<foto>-lisa.png` do `alisar.py`: o motor recorta pela máscara ao lado. `atras` põe objetos entre a parede e a pessoa. Dá erro se a pessoa encosta na caixa da logo. `rosto_x` (330 a 750) põe o rosto mais para um lado e `rosto` (400 a 600) muda o tamanho: é assim que a composição muda de um carrossel para o outro |
| `foto_inteira(arquivo, foco_x=0.5, foco_y=0.4, zoom=1.0, escurecer='baixo')` | Foto no slide todo sem recorte de pessoa (prédio, produto, evento), só na capa e no final |
| `abrir(n, qual, foto_no_topo=arquivo, foto_ate=600)` | Slide de conteúdo com a foto em faixa no alto, de ponta a ponta, logo branca por cima (molde "metade foto") |
| `pessoa_solta(arquivo, cabelo, queixo, centro, cx, cabelo_y, rosto=440)` | Pessoa recortada em qualquer lugar, saindo pela borda; o texto vai do outro lado (`limite=600`) |
| `recorte_de_noticia(veiculo, manchete_real, data, x, y, w)` | Cartão de notícia limpo; devolve onde termina |
| `palavra_de_impacto(texto, x, base, tam, cor, fundo=None)` | Número ou frase curta em Oswald dentro do slide de conteúdo, com tarja opcional |
| `escurecer_foto('baixo'|'cima'|'tudo'|'nenhum')` | Escurece a foto da capa ou do final onde vai o texto (também é parâmetro de `foto_de_pessoa` e `foto_inteira`) |
| `credito(texto, cor='#5B6474')` | Crédito da foto ou "Imagem ilustrativa", 24 px, em cima à direita (slide de foto) |
| `foto_na_peca(arquivo, apelido, credito_da_foto=None, ...)` | Foto real no lugar da peça, com os cantos da peça; crédito por fora, embaixo |
| `titulo_de_foto(linha, PALAVRA, tam, base=PALAVRA_BASE, cor=BRANCO, risco='#95db30', fundo_da_palavra=None)` | Linha pequena com risco e palavra gigante, em qualquer altura e cor; `fundo_da_palavra` põe a palavra numa tarja. `tam` até 256: o motor diz o valor que enche a largura |
| `tarja_da_capa(texto)` / `chamada(verbo, PALAVRA)` | O fecho da capa e o do final. Na R12: `chamada('Fale com a', 'R12')` ou `chamada('Comente', 'R12')` |
| `objeto(nome, arquivo, cx, cy, lado, giro=0)` | Objeto 3D gerado sobre branco: tira o fundo e põe com sombra |
| `icone(nome, arquivo, cx, cy, lado)` | Ícone 3D em cima de branco (fundo claro ou painel branco). Ícone de traço em qualquer cor: a função `ic` e o dicionário `I` de `exemplo/slides-pdf-seo.py` |
| `linha_fina(nome, [pontos], ...)` | Linha de 3 px para ligar um rótulo de fora a um ponto do print |
| `seta(nome, cx, cy, cor, para='direita')` | Seta desenhada |

Constantes: `MARGEM, PECA_Y, ATE, MIOLO, FIO_Y, TEXTO_Y, AZUL, BRANCO, VERMELHO, ESCURO, CINZA, PROFUNDO, TEXTO, SOMBRA, IMPACTO, REC`.
Os nomes ficaram do motor de origem: na R12, `AZUL` é o verde `#95db30` e `PROFUNDO` é o escuro `#161616`.

## Dentro da peça (o que é livre)

`pc` é a ponte com o PhotoCraft. Cada chamada cria uma camada com nome (nomes em MAIÚSCULAS, sem repetir no slide).

| Chamada | Devolve |
| --- | --- |
| `pc.texto(nome, txt, x, y, tam, peso=400, cor=PROFUNDO, alinhar='left', espaco=0, fonte=FONTE, entrelinha=None)` | `(id, x0, y0, x1, y1)` da tinta. `y` é a linha de base. `\n` quebra a linha |
| `pc.forma(nome, 'rect' ou 'roundedRect', x, y, w, h, cor, raio=0, borda=(largura, cor), sombra=SOMBRA)` | id. `cor` pode ser degradê: `{'gradient': {'stops': [[0, '#fff'], [1, '#ddd']], 'angle': -62}}`. `raio` aceita `[a, b, c, d]` |
| `pc.bola(nome, cx, cy, diametro, cor)` | id |
| `pc.imagem(nome, caminho, cx, cy, prender=False)` | id. O arquivo tem de estar dentro de `$CARROSSEIS` |
| `pc.abaixo_de(camada, alvo)` | Põe uma camada atrás de outra (fundo criado depois do texto, para ter o tamanho dele) |
| `pc.ex(comando, **params)` | Qualquer comando do PhotoCraft. Lista: `photocraft-cli commands --json` |

Receita do fundo do tamanho do texto (tarja, etiqueta, balão): crie o texto, leia a largura no que ele devolve, crie a forma e ponha `abaixo_de`.
Prontas para copiar de `exemplo/slides-pdf-seo.py`: as barras do `s3`, a busca com o lugar vazio do `s4`, o fluxo do `s5`, a linha no tempo do `s6`, a torre do `s19`, a equação do `s21` e os ícones de traço (`ic` e o dicionário `I`).

Peça no fundo claro é escura (`PROFUNDO`, com `SOMBRA`). Peça no fundo escuro é clara (`#e7ffef`) ou verde (`AZUL`).
Altura inteira em cartão e linha (`//`), senão a borda sai borrada. Linha em pé com x terminado em `.5` sai nítida.

## Vários agentes

Os slides do meio são independentes. Para ir rápido: cada agente escreve os seus em um arquivo próprio na pasta do carrossel
(`slides_a.py` com `SLIDES = {2: s2, 4: s4}`) e o `slides.py` junta: `SLIDES = {**slides_a.SLIDES, **slides_b.SLIDES, ...}`.
Só divida quando houver muitas peças difíceis: um agente só monta 7 slides do meio em segundos. Montagem é uma de cada vez (cada montagem gasta uns 2 GB de memória). Para dois agentes não montarem juntos, todos chamam com a mesma trava:
`flock $CARROSSEIS/.cache/montagem.lock env PREVIA=1 python3 $M/montar.py <carrossel> 2 4`.
Subagente devolve os caminhos dos arquivos; quem mostra para quem pediu é a sessão principal.

## Quando dá erro

| Mensagem | Causa | O que fazer |
| --- | --- | --- |
| "passa da margem direita em N px" ou "sai da margem (80 a 1000)" | Linha comprida (vale para todo texto, inclusive dentro da peça) | Encurte ou quebre em outro ponto. No título e no texto, não diminua a letra |
| "palavra sozinha na linha" | Quebra ruim no texto de apoio | Suba uma palavra para a linha |
| "os fundos intercalam" | Chamou `abrir` com o tema errado, ou `abrir(1)` | Não passe o tema. Capa e final usam `abrir_foto` |
| "slide N sem o fio" (ou logo, título, fecho) | Faltou uma peça fixa | Chame a função que falta antes do `fechar` |
| "travessão", "emoji", "fonte fora do padrão", "letra de N px" | Regra de texto | Corrija o texto. Não contorne |
| "não cabe entre as margens: use tam=N" | Palavra gigante larga demais | Use o `tam` sugerido ou uma palavra mais curta |
| "a pessoa encosta na logo" | O cabelo ou a cabeça tocam a caixa da logo (logo em cima do cabelo é proibido) | Meça de novo com `regua.py foto`, diminua `rosto` ou leve o rosto para o lado (`rosto_x`) |
| O recorte diz que a máscara cobre mais de 70% da foto | O recorte levou a parede junto | Rode `alisar.py` na foto e use a `-lisa.png`; se continuar, gere outra foto com mais parede em volta |
| "a foto não cobre o slide nesse enquadramento" | Medidas erradas ou foto com a pessoa pequena | Meça de novo com `regua.py foto`. Se a pessoa for pequena, gere outra com enquadramento fechado |
| "o ponto do rosto caiu fora da pessoa" | `centro`, `cabelo` ou `queixo` errados no recorte | Meça de novo |
| "o PhotoCraft fechou no meio" ou "not enough working memory" | Falta de memória | `free -m`, fechar programas, montar um slide por vez |
| `doc.place ... path` recusado | Imagem fora de `$CARROSSEIS` | Copie para a pasta do carrossel |

## O que já se aprendeu do PhotoCraft

- Imagem entra por `doc.place` (o `file.placeEmbedded` é recusado no modo `serve`). O `pc.imagem` já usa.
- `edit.transform` só aceita id de camada. Redimensione a imagem ANTES, com o ImageMagick (`pc.recorte`).
- Degradê radial: `offset` é fração da altura. Grão: camada `Overlay` com `fillNeutral` e `filter.noise.addNoise` (`grao()`). Sai sempre igual.
- `layer.removeBackground` sai grosseiro: não use. Objeto: `objeto()`. Pessoa: `foto_de_pessoa(atras=...)`, que recorta pela máscara do `alisar.py` (a `<foto>-lisa-mascara.png` ao lado da foto). Sem máscara e com o cabelo perto do topo, o motor faz a máscara na hora.
- SVG para PNG: `pc.svg_png(arquivo, altura, apelido)`. Converter com densidade alta gastava 2 GB e derrubava o PhotoCraft.
- A montagem sai idêntica toda vez: o carrossel aprovado remontado dá zero pixel de diferença. Mudou um pixel, foi você.
