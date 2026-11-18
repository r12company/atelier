---
name: carrossel-convello
description: Use quando pedirem carrossel, card (post único), stories, post de slides ou arte de Instagram do Convello (CRM de atendimento e vendas pelo WhatsApp, @convello.com.br), colarem um roteiro de slides ("SLIDE 1, SLIDE 2..."), pedirem capa, legenda, foto ou print para post do Convello, ou ajuste em carrossel já feito ("muda o slide 3", "troca a foto da capa"). Monta no padrão visual aprovado pela marca, no motor Atelier (PhotoCraft), e escreve os prompts das imagens para gerar no Gemini ou no ChatGPT.
license: MIT (texto e código). As marcas e logos Convello são registradas e só podem ser usadas em material do próprio Convello.
---

# Carrossel do Convello

O padrão que o dono da marca aprovou em 15/11/2026 está guardado em código: o motor (Atelier) monta sempre igual. O que muda de um post para o outro é o seu trabalho: o roteiro encaixado, o material real e a peça de cada slide.

**Material real, montado pelo motor, conferido com a régua, mostrado cedo.**

Pasta desta skill: `${CLAUDE_SKILL_DIR}` (a pasta onde está este SKILL.md). Pasta de trabalho: `$CARROSSEIS` (padrão `~/carrosseis`), um carrossel por pasta: `$CARROSSEIS/NN-tema/`.

Antes de tudo, veja o resultado aprovado, `exemplo/folha.jpg` (Read), o melhor da campanha editorial, `exemplo/tiktok-folha.jpg` (por que funciona: `referencias/moldes.md`), o exemplo de composições (`exemplo/moldes.jpg`) e as capas que vocês já fizeram, `$CARROSSEIS/*/png/01.png`: a identidade você repete; personagem, capa, layout e ordem do texto, não.

Esta skill vence `ig-carousel` e `ig-caption` em tudo que divergir (elas pedem HTML e contador de slide: os dois foram reprovados).

**Três formatos, mesma identidade** (`referencias/formatos.md`): carrossel (1080 x 1440 ou 1080 x 1350, 6 a 10 slides), card (post único, 1080 x 1350 ou 1080 x 1440) e stories (1080 x 1920, 3 a 6 telas). A identidade inteira (cores, fontes, medidas, componentes, o que nunca fazer) está em `DESIGN-SYSTEM.md`. Quando e quanto postar: `referencias/calendario.md`.

## Quem faz o quê

| Quem | Faz |
| --- | --- |
| Você (Claude) | Roteiro encaixado, pedidos de imagem (prompts prontos), lista de prints, slides no motor, conferência, legenda |
| A produtora | Gera as imagens no Gemini ou no ChatGPT com os seus prompts, traz os prints do sistema, aprova e posta |

Você não gera imagem nem tira print sozinho. Peça, com o pedido pronto, e espere o arquivo chegar na pasta.

## Passo a passo

Faça na ordem. Ao chegar em cada passo, leia o arquivo indicado: é lá que está o detalhe.

| # | Passo | Leia | Pronto quando |
| --- | --- | --- | --- |
| 0 | `python3 $M/checar.py` | | Disse "ATELIER PRONTO PARA MONTAR". Se não, diga em 1 linha o que falta e siga pelo caminho B (`referencias/caminho-b.md`) |
| 1 | Formato (carrossel, card ou stories) e roteiro encaixado na planta, em `NN-tema/roteiro.md`, com um gancho da seção 6. Post de notícia: pesquisa verificada antes (`pesquisa.md`) e arco editorial de 9 slides | `referencias/copy.md`, `referencias/formatos.md` | Roteiro de quem pediu: encaixado. Roteiro seu: quem pediu deu OK no texto |
| 2 | Material de cada slide: pedidos de imagem em `NN-tema/pedidos-de-imagem.md` e lista de prints | `referencias/material.md`, `modelos-de-prompt/LEIA-ME.md` | A produtora salvou os arquivos em `geradas/` e `telas/`, e você olhou cada imagem (Read) |
| 3 | Capa montada e mostrada | `referencias/motor.md` | Mostrou a capa (caminho do PNG). Siga sem esperar resposta |
| 4 | Os outros slides em `slides.py`, com uma direção de arte própria escrita no topo | `referencias/moldes.md`, `referencias/motor.md`, `referencias/arquitetura-visual.md` | `montar.py` sem erro; pelo menos 4 moldes diferentes nos slides do meio |
| 5 | Conferência | `referencias/reprovado.md` | `copy.md` da peça escrito (`referencias/copy.md`, seção 7), `regua.py` rodado, você olhou cada slide, `planta/folha-com-regua.jpg` e `planta/panorama.jpg`, e `conferir.py` disse "CONFERIDO" |
| 6 | Entrega | | Mostrou `folha.jpg`, os PNG (e os PSD com camadas) e o `copy.md` da peça: formato e horário sugeridos, gancho, legenda pronta para colar, chamada, hashtags, texto alternativo, texto de cada slide (e, nos stories, o adesivo sugerido) |

Quem posta agenda pelo app do Instagram, para pôr música. Nada é postado por você.

Na entrega, diga em poucas linhas: o que é de mentira (print em modo demonstração, foto gerada por IA), quantas imagens foram pedidas e o que você cortou do roteiro para caber.

Como mostrar imagem: o terminal não mostra imagem para quem pediu. Diga o caminho completo de cada arquivo (a capa primeiro) e, se a sua ferramenta tiver um jeito de enviar arquivo, envie.

## Regras sem exceção

| Regra | Por quê |
| --- | --- |
| Função do Convello só aparece em print real da versão atual, em modo demonstração, trazido pela produtora (`referencias/material.md`, item 1) | Tela inventada ou antiga foi a primeira reprovação |
| Slide só se monta com `motor/montar.py` (PhotoCraft). Sem Atelier, só o caminho B (Photoshop ou Figma, `referencias/caminho-b.md`). Nunca HTML, Canva ou PIL | O dono da marca quer PSD com camadas e reprovou a versão em página |
| Fundo, logo, título, texto, tarja, fio, moldura de print e enquadramento de foto vêm das funções do `comum.py`. Você desenha só a peça, entre `PECA_Y` e `ATE` | O padrão aprovado mora nessas funções |
| Não edite `motor/comum.py` nem `motor/planta.py` para "fazer caber" ou "passar" | Muda todos os carrosséis. Erro do motor se resolve no texto ou na peça |
| Pouco texto por slide: título de 2 linhas, apoio curto, tarja, no máximo 1 linha de fonte, fio. Mire em 60 palavras (`referencias/copy.md`, seção 3) | "Não pôr tanto conteúdo textual, que vai poluir e ficar difícil de ler" |
| Roteiro aprovado fica travado: o redesenho muda só a arte | Quem pediu aprova o texto antes e não quer revisar de novo |
| Capa e final limpos: só muda a posição. Sem escurecer a foto inteira, sem sombra em faixas | "Poluído, essa sombra" |
| Post sobre uma marca mostra a logo dela: na capa, no final (3D ou plana, conferida na web) e nas peças onde a marca é citada (`referencias/material.md`) | "Logos são representações boas sempre que tiver uma marca" |
| Cada carrossel inova: personagem, pose, objetos, peças E também layout, ritmo de fundos e ordem do texto (`referencias/moldes.md`). O que se repete é a identidade: logo, fontes, cores, margens, o fio | "Não pode ser o mesmo homem. Tem que inovar cada carrossel" |
| Imagem gerada só pelo pedido escrito com os `modelos-de-prompt/`. Pessoa real da notícia: só foto de verdade com licença livre, nunca rosto gerado por IA | Imagem falsa de pessoa real derruba o post |
| Nunca inventar número, depoimento, cliente ou notícia. Fato de fora se confere na fonte antes | O post vai para cliente ver |
| Sem travessão em nada; nos slides, sem emoji, contador de slide, numeração, glow, nada por cima de foto ou print | Lista completa em `referencias/reprovado.md` |
| Capa primeiro, assim que ficar pronta | Demora sem mostrar nada foi reprovado |
| Mexa só no que pediram | Trocar o rosto quando pediram luz foi reprovado |

## Quando bater a pressa

A resposta para a pressa é mostrar a capa cedo, não pular etapa.

| Pensamento | O que fazer |
| --- | --- |
| "Não tem print dessa tela, desenho uma parecida" | Peça o print à produtora. Se a tela não existe, mude a peça, não invente |
| "Monto em HTML que é mais rápido" | 10 slides no motor levam 20 segundos |
| "Esse dado todo mundo conhece" | Sem fonte, sai o número |
| "A linha passou só 12 px, diminuo a letra" | Encurte a frase |
| "O motor não deixa, ajusto o motor" | Ajuste o slide |
| "Já olhei a folha, não preciso da régua" | A régua e o panorama mostram o que a folha esconde |
| "Mando tudo no fim" | Capa primeiro |
| "Reaproveito a foto de outro carrossel" | O acervo é referência de estilo. Personagem e objetos são novos |
| "Escrevo o prompt do zero" | Junte os blocos aprovados dos `modelos-de-prompt/` |
| "É gosto: pergunto em texto" | 3 ou 4 opções numa imagem só, quem pediu escolhe riscando |

## Comandos

```bash
M="${CLAUDE_SKILL_DIR}/motor"
python3 $M/checar.py
PREVIA=1 python3 $M/montar.py NN-tema 1     # só a capa, em previa/
python3 $M/montar.py NN-tema                # todos, mais a folha.jpg
python3 $M/regua.py NN-tema                 # planta/: régua, rotas do olho e panorama
python3 $M/regua.py foto <arquivo>          # régua sobre uma foto: medir cabelo, queixo e centro do rosto
python3 $M/conferir.py NN-tema              # conferência final
```

Primeira vez neste computador: monte as provas (`exemplo/prova/`, `exemplo/prova-card/` e `exemplo/prova-stories/` dizem como). Se sair o slide, está tudo instalado.

Ajuste em carrossel pronto: mude o `slides.py`, monte só aquele slide com `PREVIA=1`, olhe, depois monte de verdade, rode `regua.py` e `conferir.py` e mostre o slide novo.
