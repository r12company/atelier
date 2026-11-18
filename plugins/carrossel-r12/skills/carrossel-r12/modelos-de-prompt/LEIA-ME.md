# Modelos de prompt: como pedir as imagens (R12)

Iguais aos do Convello, com o verde da R12 (#95db30) no lugar do azul. Exemplos de "carrossel 02" são do Convello: servem pelo jeito de pedir.

A skill não gera imagem. Ela escreve o pedido; a produtora cola no gerador, baixa o resultado e salva na pasta indicada.
Os blocos daqui são os que deram certo nos carrosséis aprovados (e os cuidados vêm do que foi reprovado). Junte os blocos; não reescreva do zero.

## Onde gerar

| Ferramenta | Onde | Formato |
| --- | --- | --- |
| Gemini, modelo de imagem Nano Banana | app do Gemini (gemini.google.com) ou Google AI Studio (aistudio.google.com, escolha o modelo de imagem) | No AI Studio, escolha a proporção no painel ("Aspect ratio"). No app, a proporção vai escrita no prompt |
| ChatGPT Images | chatgpt.com, pedindo uma imagem | Retrato sai em 2:3 (1024 x 1536), quadrado em 1:1. Escreva o formato no prompt |

Os dois aceitam imagem anexada (clipe ou arrastar). Prompt em inglês rende melhor nos dois.
Sempre baixe em PNG, no maior tamanho que a ferramenta der.

## Como cada pedido é escrito (em `<carrossel>/pedidos-de-imagem.md`)

````markdown
## capa-pessoa.png
O que é: a pessoa da capa, aflita, olhando o celular (o problema do post).
Onde gerar: Gemini (AI Studio, proporção 3:4) ou ChatGPT (retrato 2:3).
Anexar: nada (ou `referencias/estilo-luz.png`, só como referência de luz).
Salvar como: `geradas/capa-pessoa.png`

```text
<o prompt em inglês, pronto para copiar>
```
````

Um bloco por imagem, na ordem em que devem ser geradas (a capa antes do final, o objeto antes da versão "do outro lado").
Depois de mandar, espere a produtora salvar e olhe cada imagem (Read).

## Os modelos

| Arquivo | Para quê | Formato | Fundo |
| --- | --- | --- | --- |
| `pessoa.md` | personagem da capa e do final (a mesma pessoa) | 3:4 (Gemini) ou 2:3 (ChatGPT) | parede cinza clara lisa: o motor recorta a pessoa e põe objetos atrás dela |
| `objeto-3d.md` | objeto 3D da marca (atrás da pessoa, emenda entre slides) e logo de marca em 3D | 1:1 | branco puro (Gemini) ou transparente (ChatGPT); o motor aceita os dois |
| `icones.md` | 4 ícones 3D para a lista de resumo, numa imagem só | 1:1 | branco puro |
| `ajustes.md` | refazer só a luz, ver o objeto do outro lado, consertar um detalhe | o da imagem original | o da imagem original |

## Anexos: o que mandar junto

| Pedido | Anexe |
| --- | --- |
| Pessoa do final | a capa já aprovada (`geradas/capa-pessoa.png`): é o que mantém o mesmo rosto |
| Logo de outra marca em 3D | a logo oficial em PNG (a skill baixa e converte para `referencias/`). Sem ela o gerador inventa o desenho |
| Objeto "visto do outro lado" | o primeiro objeto aprovado |
| Ajuste de luz | a própria foto, e diga que só a luz muda |
| Estilo de luz e enquadramento | uma imagem aprovada de carrossel anterior, com "outra pessoa" escrito no prompt |

## Nunca peça

- rosto de pessoa real (gente da notícia): só foto de verdade, com licença livre (`referencias/material.md`);
- tela de sistema ou print: o gerador inventa a interface;
- texto, letra ou número dentro da imagem: o motor escreve o texto;
- a mesma pessoa de outro carrossel: personagem novo a cada carrossel.
