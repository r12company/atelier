---
name: carrossel-r12
description: Use quando pedirem carrossel, card (post único), stories, post de slides ou arte de Instagram da R12 Company (@r12_company, agência de marketing e tráfego pago), não do Convello. Também quando pedirem capa, legenda ou ajuste em carrossel da R12. Monta no motor Atelier (PhotoCraft) com cores, logo, fontes e contato da R12, já guardados na skill, e escreve os prompts das imagens para gerar no Gemini ou no ChatGPT.
license: MIT (texto e código). As marcas e logos R12 e R12 Company são registradas e só podem ser usadas em material da própria R12.
---

# Carrossel da R12 Company

O mesmo método aprovado do carrossel do Convello, com a marca da R12 (agência de marketing e tráfego pago, @r12_company).
**Leia antes:** `referencias/marca.md` (quem é a R12, contato e frases da marca) e `DESIGN-SYSTEM.md` (cores, fontes, medidas, componentes e o que nunca fazer).
Três formatos, mesma identidade: carrossel, card e stories (`referencias/formatos.md`). Quando postar: `referencias/calendario.md`.

Pasta desta skill: `${CLAUDE_SKILL_DIR}` (a pasta onde está este SKILL.md). Pasta de trabalho: `$CARROSSEIS` (padrão `~/carrosseis`), com o prefixo `r12-` para separar dos carrosséis do Convello: `$CARROSSEIS/r12-NN-tema/`.

O passo a passo, as regras de texto, os moldes, o material, os pedidos de imagem e a lista do que foi reprovado são os do Convello, copiados aqui:
`referencias/copy.md`, `referencias/moldes.md`, `referencias/reprovado.md`, `referencias/material.md`, `referencias/arquitetura-visual.md`, `referencias/motor.md`, `referencias/caminho-b.md` e `modelos-de-prompt/`.
Onde aquelas regras falam "Convello", leia "R12". Onde divergirem, esta skill vence.
Os exemplos que elas citam (`exemplo/folha.jpg`, `exemplo/tiktok-folha.jpg`, `exemplo/moldes.jpg`, `exemplo/slides.py`) ficam na skill `carrossel-convello`; aqui o exemplo é `exemplo/folha-pdf-seo.jpg`.

## Quem faz o quê

| Quem | Faz |
| --- | --- |
| Você (Claude) | Roteiro encaixado, pedidos de imagem (prompts prontos), slides no motor, conferência, legenda |
| A produtora | Gera as imagens no Gemini ou no ChatGPT com os seus prompts, traz os prints do trabalho real da R12, aprova e posta |

## Passo a passo

| # | Passo | Pronto quando |
| --- | --- | --- |
| 0 | `python3 $M/checar.py` | "ATELIER PRONTO PARA MONTAR". Se não, diga o que falta em 1 linha e siga pelo caminho B (`referencias/caminho-b.md`) |
| 1 | Formato (carrossel, card ou stories) e roteiro encaixado na planta (`referencias/copy.md`, com um gancho da seção 6), em `r12-NN-tema/roteiro.md` | Roteiro de quem pediu: encaixado. Roteiro seu: OK no texto |
| 2 | Pedidos de imagem em `pedidos-de-imagem.md` (`modelos-de-prompt/`) e lista de prints | A produtora salvou os arquivos e você olhou cada um (Read) |
| 3 | Capa montada e mostrada (`PREVIA=1`) | Mostrou o caminho do PNG. Siga sem esperar |
| 4 | Os outros slides em `slides.py`, com direção de arte própria no topo | `montar.py` sem erro, 4+ moldes no meio |
| 5 | Conferência (`referencias/reprovado.md`) | `copy.md` da peça escrito (`referencias/copy.md`, seção 7), `regua.py` e `conferir.py` rodados, você olhou cada slide |
| 6 | Entrega | `folha.jpg`, PNG, PSD e o `copy.md` da peça (formato e horário, gancho, legenda, chamada, hashtags, texto alternativo, texto de cada slide) |

## O que muda do Convello

| Item | Convello | R12 |
| --- | --- | --- |
| Motor | `carrossel-convello/motor` | `motor/` desta skill (cópia com a marca da R12; mude estilo só aqui) |
| Fundos | branco e azul | claro quase branco e escuro `#161616` com toque de verde |
| Destaque, tarja, botão do fio | azul | verde `#95db30` com letra escura; em fundo claro o destaque de texto é `#3f7a0f` |
| Logo no topo | Convello | R12 company (`marca/r12-logo-64.png` e `-branca-64.png`) |
| Arroba | @convello.com.br | @r12_company |
| Título das páginas | IBM Plex 64 | **Oswald 82 a 92**, a letra da capa |
| Prints | telas do Convello | trabalho real da R12: sites de clientes, campanhas, resultados que quem pediu mostrar, sempre com autorização do cliente. Nunca tela inventada |
| Objeto 3D e ícones | plástico azul `#0A6BF0` | plástico verde `#95db30` (os `modelos-de-prompt/` daqui já vêm em verde) |
| Chamada do final | Comente CONVELLO | `chamada('Fale com a', 'R12')` ou `chamada('Comente', 'R12')`; uma só |
| Legenda | #Convello | `#R12Company` e duas do assunto; WhatsApp e site na bio, não na legenda |

## Visual aprovado (16/11/2026, na proposta de SEO)

- Slide limpo como a capa: título grande, UMA imagem, o fio. Pouco texto: o apoio de 2 linhas só quando for indispensável.
- Mais visual por estratégia, não por imagem gerada: gráfico de barras, linha no tempo, fluxo com setas, antes x depois, equação visual. Peças prontas para copiar em `exemplo/slides-pdf-seo.py` (`s3` barras, `s4` busca com o lugar vazio, `s5` fluxo, `s6` anúncio x SEO no tempo, `s19` torre de preço, `s21` 10 meses = 1 venda). Folha: `exemplo/folha-pdf-seo.jpg` (os 10 primeiros dos 23 slides; os outros citavam clientes e preços).
- Capa: pessoa de verdade (gerada), roupa verde quando fizer sentido, objeto 3D verde atrás (lupa, pino de mapa), palavra gigante em Oswald e tarja verde.
- Foto gerada no Gemini: alise a parede antes (`python3 $M/alisar.py <pasta>/geradas/foto.png`) e use o recorte pela máscara (`_recorte_pela_mascara` no exemplo). O recorte automático leva a parede junto.

## Comandos

```bash
M="${CLAUDE_SKILL_DIR}/motor"
python3 $M/checar.py
python3 $M/alisar.py "$CARROSSEIS/r12-NN-tema/geradas/<foto>.png"
PREVIA=1 python3 $M/montar.py r12-NN-tema 1          # só a capa: mostre na hora
python3 $M/montar.py r12-NN-tema                     # todos, mais a folha.jpg
python3 $M/regua.py r12-NN-tema
python3 $M/conferir.py r12-NN-tema
```

Primeira vez neste computador: monte as provas (`exemplo/prova/`, `exemplo/prova-card/` e `exemplo/prova-stories/` dizem como).

## Regras sem exceção

- Nada inventado sobre a R12: número de clientes, resultado, depoimento. Só o que está no site ou o que quem pediu disser.
- Nome de cliente da R12 só com autorização dele, e nunca dado que não seja público.
- Sem travessão, sem emoji no slide, sem contador de slide.
- Capa primeiro; toda imagem é mostrada com o caminho do arquivo.
- Nada é postado por você.
