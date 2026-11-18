# Material: de onde vem cada peça

**A regra principal: material real.** O post mostra a R12 de verdade, com a logo de verdade e trabalho que a R12 fez de verdade. Nada é inventado para "ficar bonito".

| O slide fala de | A peça é | De onde vem |
| --- | --- | --- |
| Um trabalho da R12 (site de cliente, landing page, campanha, resultado) | Print real, com autorização do cliente | Pedido à produtora, que pega com quem pediu o post (item 1) |
| Uma ideia de marketing (anúncio x SEO, o caminho do clique, o custo de não aparecer) | Peça de dado ou desenho feito no PhotoCraft | `exemplo/slides-pdf-seo.py` mostra a técnica: `s3` barras, `s4` busca com o lugar vazio, `s5` fluxo, `s6` anúncio x SEO no tempo, `s19` torre, `s21` equação "10 meses = 1 venda". O desenho em si é novo a cada carrossel: não repita a peça do exemplo |
| Produto dos outros (Google, Instagram, ChatGPT) | Desenho simples que NÃO imita a tela deles (um cartão de busca genérico, um balão) ou a logo da marca | PhotoCraft, ou objeto 3D gerado pela produtora (item 2). Nunca print falso do produto dos outros |
| Um resumo, uma lista | Painel com ícones grandes, no lugar de número | Ícones de traço do dicionário `I` do exemplo, ou ícones 3D verdes gerados pela produtora (item 2) |
| Capa e final | Foto de pessoa, com objetos 3D verdes atrás dela na capa | Personagem novo gerado pela produtora (item 2), ou foto de verdade de quem é a notícia |
| Logo, símbolo | Arquivo da marca | `marca/` da skill (PNG e SVG). SVG entra com `pc.svg_png` |

Proibido: tela inventada fingindo ser trabalho da R12, print de cliente sem autorização dele, print antigo de um site que já mudou, foto de banco com marca d'água, nome, telefone ou número de cliente que ele não liberou, print da tela inteira do computador, número de resultado que não veio de quem pediu.

## 1. Print de trabalho real (a produtora traz)

Você não tira print sozinho: peça à produtora, dizendo **qual trabalho**, **qual pedaço** e **para provar qual frase**. Ela salva em `<carrossel>/telas/` e você recorta.

**Antes de pedir, a autorização.** Site, campanha ou número de cliente só entram com o OK do cliente, dado a quem pediu o post. Pergunte em 1 linha se ele autorizou e anote no `copy.md` da peça (seção "Imagens"). Sem OK, a peça vira desenho genérico, sem nome nem marca do cliente.

**De onde vem, em ordem de preferência:**

1. **Quem pediu o post manda o print** (do gerenciador de anúncios, do relatório, do site no ar), já com o dado que pode aparecer.
2. **A produtora tira** do site do cliente no ar, no Google Chrome:
   1. Abra o site no Chrome, com a janela grande.
   2. Aperte F12 (no Mac, Cmd + Option + I) para abrir as ferramentas do Chrome.
   3. Clique no ícone de celular e tablet ("Toggle device toolbar", ou Ctrl + Shift + M).
   4. Em cima da página: escolha "Responsive", escreva 1680 por 900 (computador) ou 390 por 844 (celular) e, nos três pontinhos dessa barra, ligue "Add device pixel ratio" e escolha **3**.
   5. Nos mesmos três pontinhos, clique em "Capture screenshot". Sai um PNG nítido para o celular.
   Zoom do navegador (Ctrl +) não serve: ele muda o layout da tela. É a escala 3x que deixa o print grande e igual.

**O print só serve se** (olhe cada um com Read antes de usar):

- for da versão atual do site ou da campanha;
- não mostrar dado pessoal de ninguém: nome, telefone, e-mail ou foto de cliente final. Corte ou peça outro;
- não mostrar valor de verba, custo ou faturamento que o cliente não liberou;
- não tiver erro na tela, página em branco, aviso de cookie cobrindo o conteúdo ou banner de teste.

**Prints que costumam provar bem** (peça pelo nome):

| Para mostrar | Peça |
| --- | --- |
| Site ou landing page | A primeira tela no celular: título, foto e o botão do WhatsApp |
| Aparecer no Google | O resultado da busca com o site do cliente, com o nome autorizado |
| Campanha | O anúncio como aparece no feed (não o painel de gestão cheio de número) |
| Resultado | Só o número que o cliente liberou, recortado grande, com o período |

Depois de receber:

1. **Recorte só o pedaço que prova a frase**, grande o bastante para ler no celular (o botão e o título legíveis valem mais que a página inteira miúda):
   `magick telas/X.png -crop LARGURAxALTURA+X+Y +repage recortes/nome.png` e, no slide, `print_do_sistema('nome.png', 'apelido')`.
2. Print reaproveitado de outro carrossel: confira se o site ainda é assim. O motor avisa quando o arquivo tem mais de 30 dias.
3. Se o print que o roteiro pede não existe ou não foi autorizado, mude a peça para um desenho genérico. Nunca desenhe uma tela parecida com a de um cliente.

## 2. Foto e objeto 3D (a produtora gera)

A skill não gera imagem sozinha. Você **escreve o pedido** e a produtora gera no **Gemini** (app ou AI Studio, modelo de imagem Nano Banana) ou no **ChatGPT** (Images). Como escrever: `modelos-de-prompt/` (leia o `LEIA-ME.md` de lá antes do primeiro pedido).

1. Escreva todos os pedidos do carrossel em `<carrossel>/pedidos-de-imagem.md`, um bloco por imagem, no formato do `modelos-de-prompt/LEIA-ME.md`: 1 linha em português do que é, o nome do arquivo, a ferramenta, o formato, a lista de anexos e o prompt em inglês num bloco pronto para copiar.
2. Prepare os anexos em `<carrossel>/referencias/` (logo da R12 em PNG para objeto de marca, foto de referência, a capa já aprovada) e diga o caminho de cada um.
3. Mostre os pedidos para a produtora e espere: ela gera, escolhe a melhor e salva com o nome pedido em `<carrossel>/geradas/`.
4. Olhe cada imagem que chegar (Read) antes de usar.

Mande o pedido da capa primeiro: é ela que trava o personagem, e a do final usa a capa como anexo. Até umas 12 imagens por carrossel; passou disso, pergunte antes.

**Acervo.** A proposta de SEO (`exemplo/folha-pdf-seo.jpg`) é a referência de estilo da R12: dona de empresa de camisa verde, lupa 3D verde grande atrás, pino de mapa do outro lado, luz de estúdio. As imagens dela não vêm no pacote e não se repetem em outro carrossel. Para referência, as medidas que a capa dela usou em `foto_de_pessoa`: `cabelo=165, queixo=495, centro=345, rosto_x=440, rosto=460`. Imagens aprovadas que vocês quiserem reaproveitar como referência de estilo ficam em `$CARROSSEIS/geradas/` (o motor também procura lá).

### Foto do Gemini: alisar a parede

A parede das fotos do Gemini vem com vinheta e o cabelo costuma encostar no topo. Antes de montar:

```bash
python3 $M/alisar.py <carrossel>/geradas/<foto>.png
```

Ele grava `<foto>-lisa.png` e `<foto>-lisa-mascara.png` ao lado. Use a `<foto>-lisa.png` no `slides.py`: o motor acha a máscara ao lado e recorta a pessoa por ela. Se o cabelo chega perto do topo e não há máscara, o motor faz a máscara na hora. Se a máscara cobre mais de 70% da foto (o recorte levou a parede junto), dá erro: gere outra foto com mais parede em volta.
O motor também dá erro se a pessoa encosta na caixa da logo: logo em cima do cabelo é proibido. Meça de novo, diminua o rosto (`rosto`) ou leve o rosto para o lado (`rosto_x`).

### Inovar a cada carrossel (regra do dono da marca)

"Não pode ser o mesmo homem. Sempre elementos e personagens diferentes, posições diferentes. Layout e hierarquia boa, mas tem que inovar cada carrossel."

| Muda sempre | Não muda nunca |
| --- | --- |
| O personagem: outra pessoa (varie homem e mulher, idade, cabelo, roupa, ramo do negócio ligado ao assunto: clínica, loja, restaurante, oficina) | A planta: margens, alturas, a rota do olho |
| A pose e o gesto: nem todo mundo segurando celular. Um no notebook, outro atrás do balcão, outro apontando para cima, outro abrindo a porta da loja, de braços cruzados. O gesto conta o assunto | A tipografia e os tamanhos de letra |
| A posição: rosto no meio, mais à esquerda ou mais à direita (`rosto_x`), pessoa maior ou menor (`rosto`) | A logo, o fio, os fundos intercalados e as cores |
| Os objetos 3D: próprios do assunto (lupa, pino de mapa, alvo, megafone, gráfico), em outro arranjo | "Objeto grande atrás da pessoa", "nada por cima de foto ou print" |
| As peças do meio: não repita a mesma sequência de peças do carrossel anterior | Print real para trabalho da R12 |

Antes de criar, olhe as capas que já existem (`$CARROSSEIS/r12-*/png/01.png` e `exemplo/folha-pdf-seo.jpg`) e faça diferente de todas.
Dentro do MESMO carrossel, a capa e o final são a mesma pessoa (exceto quando a capa é uma pessoa real da notícia: aí o final é um personagem gerado). Gere a capa primeiro e use a foto dela como referência do final.

### Foto real de empresa, produto ou acontecimento

Post de notícia pede imagem real quando há direito de uso: Wikimedia Commons em domínio público, CC0 ou CC BY (CC BY-SA só em último caso, porque obriga a licenciar o slide igual). Baixe para `<carrossel>/fotos/` com `curl`, anote arquivo, autor, licença e link no `copy.md` da peça ("## Imagens") e ponha o crédito:
- foto no slide todo (capa sem pessoa recortável: prédio, produto, evento): `foto_inteira(arquivo, foco_x, foco_y, zoom)` e `credito('Foto: Autor / Wikimedia (CC BY 2.0)')`;
- foto dentro da peça: `foto_na_peca(arquivo, apelido, 'Foto: ...')`, crédito embaixo, por fora da foto;
- **post sobre marca leva a logo da marca** (Google, Instagram, Meta): na capa e no final, o objeto atrás da pessoa pode ser a logo da marca do assunto em 3D (ou plana), não um objeto genérico. Nas peças, onde o nome da marca aparece como rótulo, use a logo. Antes de usar, pesquise na web (WebSearch) como é a logo ATUAL da marca, versão e cores, porque marcas trocam de logo, e compare o arquivo baixado com o que achou.
- logo de outra empresa: o arquivo oficial, plano, nas cores dela, sem deformar, só em post de notícia ou explicação sobre aquela plataforma (nunca sugerindo parceria). Fonte boa de SVG: Simple Icons (`curl -sfL https://cdn.jsdelivr.net/npm/simple-icons@16.37.0/icons/<marca>.svg`, nome em minúsculas sem espaço, ex.: `google`, `instagram`, `meta`). Algumas marcas pediram para sair das versões novas: tente `simple-icons@11.0.0` ou o Commons. Converta com `pc.svg_png`.
- objeto 3D de marca alheia no Gemini ou no ChatGPT: SEMPRE com a logo real ANEXADA de referência (o PNG do SVG acima, salvo em `<carrossel>/referencias/` para a produtora anexar), senão ele inventa o desenho. Confira no olho antes de usar. No post de notícia mantenha as cores da marca.
Imagem gerada por IA num post de notícia leva `credito('Imagem ilustrativa')`: ninguém pode achar que é foto do fato.

### Pessoa real (quem é a notícia)

Em post sobre uma empresa ou um fato, o personagem pode ser a pessoa de verdade da notícia.

- **Só foto de verdade**, com licença que deixa usar e adaptar em post de empresa: Wikimedia Commons em domínio público ou CC BY (CC BY-SA em último caso). Baixe com `curl`, guarde em `<carrossel>/fotos/` e anote no `copy.md` da peça o link, o autor e a licença.
- Achar a foto: a API do Commons, por categoria (`https://commons.wikimedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:Nome_da_Pessoa&cmtype=file&cmlimit=50&format=json`) e depois `prop=imageinfo&iiprop=url|extmetadata` no arquivo escolhido para ler autor e licença. Prefira foto grande, nítida, com o rosto de frente ou três quartos.
- Outra pessoa no quadro: corte para ela não aparecer. O crédito diz que a foto foi recortada: `Foto: Autor / Wikimedia (CC BY 2.0), recortada`.
- Logo da R12 em cima da foto: escura quando o canto de cima é claro (`topo('branco')`), branca quando é escuro (`topo('escuro')`). Nunca em cima do rosto ou do cabelo: o motor dá erro; mova o rosto (`rosto_x`) ou escolha outra foto.
- **Crédito na legenda**, numa linha antes das hashtags: `Foto: Nome do autor, Wikimedia Commons (CC BY 2.0)`.
- **Nunca gere por IA o rosto de uma pessoa real**, nem peça ao Gemini ou ao ChatGPT para "melhorar" ou trocar a expressão dela. Imagem falsa de pessoa real é o tipo de coisa que derruba post e dá processo.
- Não ponha fala na boca dela e não sugira que ela usa ou recomenda a R12. O texto fala do fato.
- Foto de evento não tem parede lisa, então o recorte não funciona: use `foto_de_pessoa` SEM `atras` (a foto ocupa o slide, escurecida embaixo) e ponha o objeto 3D só na beirada, como emenda para o slide 2.
- Não achou foto livre e boa? Use a logo da empresa do assunto ou um objeto 3D verde e um personagem novo gerado, e diga isso na entrega.
- O final continua com personagem gerado (o dono de negócio que o post quer alcançar), nunca com a pessoa real fazendo a chamada.

**Olhe cada imagem gerada (Read) antes de usar.** Refaça se tiver: rosto diferente entre a capa e o final, pessoa parecida com a de outro carrossel, pele alaranjada ou bronzeada, halo ou brilho em volta, sombra ou objeto na parede (o recorte falha), celular cortado, mão com dedo errado, texto ou letra, objeto com placa atrás, objeto que não é verde `#95db30`. Peça para a produtora guardar a anterior com outro nome (às vezes a primeira era a melhor).

**Medir a foto** antes de pôr no slide: `python3 $M/regua.py foto <arquivo>` desenha uma régua de 50 em 50 px. Leia onde começa o cabelo, onde fica o queixo e o centro do rosto na largura, e passe para `foto_de_pessoa`.

"Melhora a luz" quer dizer a MESMA foto com outra luz: passe a foto de referência e peça para manter tudo e mudar só a iluminação. Trocar o rosto foi reprovado.

Nunca use gerador de imagem para print de site, de anúncio ou de resultado (ele inventa a tela e o número) nem para escrever texto na imagem.

Na entrega, diga quantas imagens foram pedidas, quais são geradas por IA e quais prints de cliente entraram (com a autorização).
