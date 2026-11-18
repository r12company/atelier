# O motor: como montar no PhotoCraft

O motor de montagem se chama Atelier. Ele comanda o PhotoCraft (um "Photoshop" de código aberto, de github.com/storytold/photocraft, licença MIT ou Apache-2.0) pela linha de comando e entrega
cada slide em PSD com camadas nomeadas (`psd/`) e em PNG para postar (`png/`). Modelo completo: `exemplo/slides.py`.

## Formato

`ALTURA = 1350` numa linha do `slides.py` monta em 4:5 (1080 x 1350); sem a linha, 3:4 (1080 x 1440, o do carrossel 02).
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

`<carrossel>` é a pasta (ou só o nome dela) dentro de `$CARROSSEIS`, por exemplo `03-chatgpt-na-disputa`.
O PhotoCraft só lê e grava dentro de `$CARROSSEIS`.

## A pasta de um carrossel

```
$CARROSSEIS/NN-tema/
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
    foto_de_pessoa('homem-capa.png', cabelo=375, queixo=672, centro=430, atras=icones)   # atras: função que põe objetos 3D
    topo('branco', arroba=False)
    titulo_de_foto('Seu cliente está', 'NO MEIO', 256)
    tarja_da_capa('da família')
    fechar(1)

def s2():                                   # CONTEÚDO (par = branco, ímpar = azul: o motor escolhe)
    abrir(2)
    manchete(['No meio disso,', '!alguém quer comprar.'])
    corpo(['Um cliente pede preço. Outro quer agendar uma visita.', 'Enquanto isso, chegam mensagens pessoais e', '!a conversa importante desce na lista.'])
    ...                                     # A PEÇA, entre PECA_Y (592) e ATE (1264), de MARGEM (80) a 1000
    fio('O problema começa aqui', primeiro=True)
    fechar(2)

def s10():                                  # FINAL
    abrir_foto(10)
    foto_de_pessoa('homem-final.png', cabelo=388, queixo=650, centro=443)
    topo('branco', arroba=False)
    titulo_de_foto('Seu WhatsApp não precisa', 'SER ASSIM', 208)
    chamada('Comente', 'CONVELLO')
    fechar(10)

SLIDES = {1: s1, 2: s2, 10: s10}
```

Nunca desenhe à mão o que o motor já faz (fundo, logo, título, texto, tarja, fio, moldura de print, enquadramento de foto):
é ali que mora o padrão aprovado. Mexer no `comum.py` ou no `planta.py` muda TODOS os carrosséis: só com pedido do dono da marca.

## Peças fixas (`comum.py`)

| Função | O que faz |
| --- | --- |
| `abrir(n, qual=None, destaque=None)` | Slide de conteúdo: fundo do tema, logo e arroba. O motor escolhe o fundo pelo número (par branco, ímpar azul); `qual` é opcional, só para deixar escrito. `destaque=VERMELHO` nos slides do problema (só no branco) |
| `abrir_foto(n)` | Slide de foto: a capa (1) e o final (último) |
| `manchete([l1, l2])` | Título de 2 linhas. `!` no começo = linha de destaque. `[trecho]` destaca um pedaço (no branco) |
| `corpo([l1, l2, '!tarja'])` | Texto de apoio. Linha com `!` vira a frase em tarja |
| `fio(pergunta, primeiro=False)` | O rodapé. `primeiro=True` só no slide 2 |
| `print_do_sistema(arquivo, apelido, y=PECA_Y, ate=ATE, x=MARGEM, w=920, gravidade=None, prefixo='PRINT')` | Print real com moldura branca. `arquivo` em `recortes/`. Dois prints no mesmo slide: `prefixo` diferente |
| `foto_de_pessoa(arquivo, cabelo, queixo, centro, atras=None, rosto_x=540, rosto=540)` | Foto de pessoa no slide todo. `atras` põe objetos entre a parede e a pessoa. `rosto_x` (330 a 750) põe o rosto mais para um lado e `rosto` (400 a 600) muda o tamanho: é assim que a composição muda de um carrossel para o outro |
| `foto_inteira(arquivo, foco_x=0.5, foco_y=0.4, zoom=1.0, escurecer='baixo')` | Foto no slide todo sem recorte de pessoa (prédio, produto, evento), só na capa e no final |
| `abrir(n, qual, foto_no_topo=arquivo, foto_ate=600)` | Slide de conteúdo com a foto em faixa no alto, de ponta a ponta, logo branca por cima (molde "metade foto") |
| `pessoa_solta(arquivo, cabelo, queixo, centro, cx, cabelo_y, rosto=440)` | Pessoa recortada em qualquer lugar, saindo pela borda; o texto vai do outro lado (`limite=600`) |
| `recorte_de_noticia(veiculo, manchete_real, data, x, y, w)` | Cartão de notícia limpo; devolve onde termina |
| `palavra_de_impacto(texto, x, base, tam, cor, fundo=None)` | Número ou frase curta em Oswald dentro do slide de conteúdo, com tarja opcional |
| `escurecer_foto('baixo'|'cima'|'tudo'|'nenhum')` | Escurece a foto da capa ou do final onde vai o texto (também é parâmetro de `foto_de_pessoa` e `foto_inteira`) |
| `credito(texto, cor='#5B6474')` | Crédito da foto ou "Imagem ilustrativa", 24 px, em cima à direita (slide de foto) |
| `foto_na_peca(arquivo, apelido, credito_da_foto=None, ...)` | Foto real no lugar da peça, com os cantos da peça; crédito por fora, embaixo |
| `titulo_de_foto(linha, PALAVRA, tam, base=PALAVRA_BASE, cor=BRANCO, risco='#2E86FF', fundo_da_palavra=None)` | Linha pequena com risco e palavra gigante, em qualquer altura e cor; `fundo_da_palavra` põe a palavra numa tarja. `tam` até 256: o motor diz o valor que enche a largura |
| `tarja_da_capa(texto)` / `chamada(verbo, PALAVRA)` | O fecho da capa e o do final |
| `objeto(nome, arquivo, cx, cy, lado, giro=0)` | Objeto 3D gerado sobre branco: tira o fundo e põe com sombra |
| `icone(nome, arquivo, cx, cy, lado)` | Ícone 3D em cima de branco (fundo branco ou painel branco) |
| `linha_fina(nome, [pontos], ...)` | Linha de 3 px para ligar um rótulo de fora a um ponto do print |
| `seta(nome, cx, cy, cor, para='direita')` | Seta desenhada |

Constantes: `MARGEM, PECA_Y, ATE, MIOLO, FIO_Y, TEXTO_Y, AZUL, BRANCO, VERMELHO, ESCURO, CINZA, PROFUNDO, TEXTO, SOMBRA, IMPACTO, REC`.

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
Prontas para copiar do exemplo: `conversa`, `etiqueta`, `balao` (peças de aplicativo de mensagem), a lista do `s2`, os cartões do `s4`, os rótulos do `s5`, o painel de resumo do `s9`.

Peça no fundo branco é escura (`ESCURO`, com `SOMBRA`). Peça no fundo azul é clara (`BRANCO` ou bege `#EBE4D8`).
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
| "a foto não cobre o slide nesse enquadramento" | Medidas erradas ou foto com a pessoa pequena | Meça de novo com `regua.py foto`. Se a pessoa for pequena, gere outra com enquadramento fechado |
| "o ponto do rosto caiu fora da pessoa" | `centro`, `cabelo` ou `queixo` errados no recorte | Meça de novo |
| "o PhotoCraft fechou no meio" ou "not enough working memory" | Falta de memória | `free -m`, fechar programas, montar um slide por vez |
| `doc.place ... path` recusado | Imagem fora de `$CARROSSEIS` | Copie para a pasta do carrossel |

## O que já se aprendeu do PhotoCraft

- Imagem entra por `doc.place` (o `file.placeEmbedded` é recusado no modo `serve`). O `pc.imagem` já usa.
- `edit.transform` só aceita id de camada. Redimensione a imagem ANTES, com o ImageMagick (`pc.recorte`).
- Degradê radial: `offset` é fração da altura. Grão: camada `Overlay` com `fillNeutral` e `filter.noise.addNoise` (`grao()`). Sai sempre igual.
- `layer.removeBackground` sai grosseiro: não use. Objeto: `objeto()`. Pessoa: `foto_de_pessoa(atras=...)`, que recorta pela cor da parede.
- SVG para PNG: `pc.svg_png(arquivo, altura, apelido)`. Converter com densidade alta gastava 2 GB e derrubava o PhotoCraft.
- A montagem sai idêntica toda vez: o carrossel aprovado remontado dá zero pixel de diferença. Mudou um pixel, foi você.
