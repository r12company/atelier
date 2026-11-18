# Material: de onde vem cada peça

**A regra principal: material real.** O post mostra o Convello de verdade, com a logo de verdade. Nada é inventado para "ficar bonito".

| O slide fala de | A peça é | De onde vem |
| --- | --- | --- |
| Uma função do Convello (lista de conversas, ficha, funil, agenda...) | Print real da tela | Pedido à produtora, que pega com o time do Convello ou tira em modo demonstração (item 1) |
| O problema, fora do Convello (WhatsApp bagunçado, mensagem esquecida) | Desenho feito no PhotoCraft | O `exemplo/slides.py` mostra a técnica (`s2` lista, `s3` conversa, `s4` cartões). O desenho em si é novo a cada carrossel: não repita a peça do exemplo |
| Produto dos outros (ChatGPT, Instagram, Google) | Desenho simples que NÃO imita a tela deles (um balão de pergunta e resposta, um cartão) ou objeto 3D da marca | PhotoCraft, ou objeto 3D gerado pela produtora (item 2). Nunca print falso do produto dos outros |
| Um resumo, uma lista | Painel com ícones 3D grandes, no lugar de número | Ícones novos do assunto, gerados pela produtora (item 2). Modelo: `s9` do exemplo |
| Capa e final | Foto de pessoa, com objetos 3D atrás dela na capa | Personagem novo gerado pela produtora (item 2), ou foto de verdade de quem é a notícia |
| Logo, símbolo, mascote Velito | Arquivo da marca | `marca/` da skill (SVG e PNG). SVG entra com `pc.svg_png` |

Proibido: tela desenhada fingindo ser o Convello, print antigo, foto de banco com marca d'água, nome, foto ou número de cliente real, print da tela inteira do computador.

## 1. Print do sistema (a produtora traz)

Você não tira print sozinho: peça à produtora, dizendo **qual tela**, **qual pedaço** e **para provar qual frase**. Ela salva em `<carrossel>/telas/` e você recorta.

**De onde vem, em ordem de preferência:**

1. **O time do Convello manda o print.** É o caminho mais seguro: sai da versão atual, em modo demonstração.
2. **A produtora tira**, numa conta de demonstração do Convello (nunca na conta de um cliente), no Google Chrome:
   1. Abra a tela no Chrome, com a janela grande.
   2. Aperte F12 (no Mac, Cmd + Option + I) para abrir as ferramentas do Chrome.
   3. Clique no ícone de celular e tablet ("Toggle device toolbar", ou Ctrl + Shift + M).
   4. Em cima da página: escolha "Responsive", escreva 1680 por 900 e, nos três pontinhos dessa barra, ligue "Add device pixel ratio" e escolha **3**.
   5. Nos mesmos três pontinhos, clique em "Capture screenshot". Sai um PNG de 5040 por 2700, nítido para o celular.
   Zoom do navegador (Ctrl +) não serve: ele muda o layout da tela. É a escala 3x que deixa o print grande e igual.

**O print só serve se tiver** (olhe cada um com Read antes de usar):

- tema escuro, que é o padrão aprovado;
- dados de demonstração: nome, telefone e foto de cliente de mentira. Nunca cliente, corretor ou pessoa real, nem número de verdade;
- foto de atendente em toda conversa e o selo do número de WhatsApp com nome ("Vendas", "Atendimento");
- nada de faixa de "dados de exemplo", "Invalid Date", erro na tela ("deu erro") ou tela vazia;
- janela de 1680 por 900: nela a lista de conversas mostra quem atende e a origem; mais estreita, esconde.

**Telas que já funcionaram** (peça pelo nome):

| Para mostrar | Peça |
| --- | --- |
| Conversas organizadas | Lista de conversas com uma conversa aberta e a ficha ao lado |
| O cliente | A ficha completa do cliente (só o resumo ficou "frio") |
| Funil de vendas | O cartão em forma de funil do Painel |
| Mudar de etapa | O funil em colunas (Pipeline) com um cartão sendo arrastado: esse é difícil de tirar sozinho, peça ao time do Convello |

Depois de receber:

1. **Recorte só o pedaço que prova a frase**, grande o bastante para ler no celular (duas conversas legíveis valem mais que a tela inteira miúda). A peça inteira tem 920 x 672:
   `magick telas/X.png -crop LARGURAxALTURA+X+Y +repage recortes/nome.png` e, no slide, `print_do_sistema('nome.png', 'apelido')`.
2. Nome certo para cada coisa: "funil de vendas" é o cartão em forma de funil do Painel; o quadro de colunas do Pipeline é o funil em colunas (kanban).
3. Print reaproveitado de outro carrossel: confira se a tela ainda é assim. O motor avisa quando o arquivo tem mais de 30 dias.
4. Se a tela que o roteiro pede não existe, mude a peça. Nunca desenhe uma tela parecida.

## 2. Foto e objeto 3D (a produtora gera)

A skill não gera imagem sozinha. Você **escreve o pedido** e a produtora gera no **Gemini** (app ou AI Studio, modelo de imagem Nano Banana) ou no **ChatGPT** (Images). Como escrever: `modelos-de-prompt/` (leia o `LEIA-ME.md` de lá antes do primeiro pedido).

1. Escreva todos os pedidos do carrossel em `<carrossel>/pedidos-de-imagem.md`, um bloco por imagem, no formato do `modelos-de-prompt/LEIA-ME.md`: 1 linha em português do que é, o nome do arquivo, a ferramenta, o formato, a lista de anexos e o prompt em inglês num bloco pronto para copiar.
2. Prepare os anexos em `<carrossel>/referencias/` (logo da marca em PNG, foto de referência, a capa já aprovada) e diga o caminho de cada um.
3. Mostre os pedidos para a produtora e espere: ela gera, escolhe a melhor e salva com o nome pedido em `<carrossel>/geradas/`.
4. Olhe cada imagem que chegar (Read) antes de usar.

Mande o pedido da capa primeiro: é ela que trava o personagem, e a do final usa a capa como anexo. Até umas 12 imagens por carrossel; passou disso, pergunte antes.

**Acervo.** O carrossel 02 (`exemplo/folha.jpg`) é a referência de estilo: luz, enquadramento, material dos objetos. As imagens dele não vêm no pacote e não se repetem em outro carrossel. Para referência, as medidas que ele usou em `foto_de_pessoa`: homem da capa `cabelo=375, queixo=672, centro=430`; homem do final `cabelo=388, queixo=650, centro=443`. Imagens aprovadas que vocês quiserem reaproveitar como referência de estilo ficam em `$CARROSSEIS/geradas/` (o motor também procura lá).

### Inovar a cada carrossel (regra do dono da marca)

"Não pode ser o mesmo homem. Sempre elementos e personagens diferentes, posições diferentes. Layout e hierarquia boa, mas tem que inovar cada carrossel."

| Muda sempre | Não muda nunca |
| --- | --- |
| O personagem: outra pessoa (varie homem e mulher, idade, cabelo, roupa, profissão ligada ao assunto) | A planta: margens, alturas, a rota do olho |
| A pose e o gesto: nem todo mundo segurando celular. Um no notebook, outro tomando café, outro abrindo uma caixa, com sacolas de compras, no sofá com o controle remoto, de braços cruzados, com a mala de viagem. O gesto conta o assunto | A tipografia e os tamanhos de letra |
| A posição: rosto no meio, mais à esquerda ou mais à direita (`rosto_x`), pessoa maior ou menor (`rosto`) | A logo, o fio, os fundos intercalados e as cores |
| Os objetos 3D: próprios do assunto, em outro arranjo | "Objeto grande atrás da pessoa", "nada por cima de foto ou print" |
| As peças do meio: não repita a mesma sequência de desenhos do carrossel anterior | Print real para função do Convello |

Antes de criar, olhe as capas que já existem (`$CARROSSEIS/*/png/01.png`, as que vocês já fizeram, e `exemplo/folha.jpg`, `exemplo/tiktok-folha.jpg`) e faça diferente de todas.
Dentro do MESMO carrossel, a capa e o final são a mesma pessoa (exceto quando a capa é uma pessoa real da notícia: aí o final é um personagem gerado). Gere a capa primeiro e use a foto dela como referência do final.


### Foto real de empresa, produto ou acontecimento

Post de notícia pede imagem real quando há direito de uso: Wikimedia Commons em domínio público, CC0 ou CC BY (CC BY-SA só em último caso, porque obriga a licenciar o slide igual). Baixe para `<carrossel>/fotos/` com `curl`, anote arquivo, autor, licença e link no `publicacao.md` ("## Imagens") e ponha o crédito:
- foto no slide todo (capa sem pessoa recortável: prédio, produto, avião): `foto_inteira(arquivo, foco_x, foco_y, zoom)` e `credito('Foto: Autor / Wikimedia (CC BY 2.0)')`;
- foto dentro da peça: `foto_na_peca(arquivo, apelido, 'Foto: ...')`, crédito embaixo, por fora da foto;
- **post sobre marca leva a logo da marca, sempre** (dono da marca, 15/11: "logos são representações boas sempre que tiver uma marca"). Na capa e no final, o objeto atrás da pessoa é a logo da marca do assunto em 3D (ou plana), não um objeto genérico (TV, alvo, envelope, cupom, play). Modelo: a logo 3D do TikTok em `exemplo/tiktok-folha.jpg`. Nas peças, onde o nome da marca aparece como rótulo (Netflix, Disney+, TikTok), use a logo. Antes de usar, pesquise na web (WebSearch) como é a logo ATUAL da marca, versão e cores, porque marcas trocam de logo, e compare o arquivo baixado com o que achou.
- logo de outra empresa: o arquivo oficial, plano, nas cores dela, sem deformar. Fonte boa de SVG: Simple Icons (`curl -sfL https://cdn.jsdelivr.net/npm/simple-icons@16.37.0/icons/<marca>.svg`, nome em minúsculas sem espaço, ex.: `tiktok`, `whatsapp`, `nubank`). Algumas marcas pediram para sair das versões novas (a Microsoft, por exemplo): tente `simple-icons@11.0.0` ou o Commons. Converta com `pc.svg_png`.
- objeto 3D de marca alheia no Gemini ou no ChatGPT: SEMPRE com a logo real ANEXADA de referência (o PNG do SVG acima, salvo em `<carrossel>/referencias/` para a produtora anexar), senão ele inventa o desenho (já saiu uma flor no lugar do ChatGPT). Confira no olho antes de usar. No post de notícia mantenha as cores da marca; o WhatsApp azul do carrossel 02 foi pedido do dono da marca para aquele post.
Imagem gerada por IA num post de notícia leva `credito('Imagem ilustrativa')`: ninguém pode achar que é foto do fato.


### Pessoa real (quem é a notícia)

Em post sobre uma empresa ou um fato, o personagem pode ser a pessoa de verdade da notícia (por exemplo, o fundador da empresa num post sobre o produto dela).

- **Só foto de verdade**, com licença que deixa usar e adaptar em post de empresa: Wikimedia Commons em domínio público ou CC BY (CC BY-SA em último caso). Baixe com `curl`, guarde em `<carrossel>/fotos/` e anote no `publicacao.md` o link, o autor e a licença.
- Achar a foto: a API do Commons, por categoria (`https://commons.wikimedia.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:Nome_da_Pessoa&cmtype=file&cmlimit=50&format=json`) e depois `prop=imageinfo&iiprop=url|extmetadata` no arquivo escolhido para ler autor e licença. Prefira foto grande, nítida, com o rosto de frente ou três quartos.
- Outra pessoa no quadro: corte para ela não aparecer. O crédito diz que a foto foi recortada: `Foto: Autor / Wikimedia (CC BY 2.0), recortada`.
- Logo do Convello em cima da foto: escura quando o canto de cima é claro (`topo('branco')`), branca quando é escuro (`topo('azul')`). Nunca em cima do rosto ou do cabelo: mova o rosto (`rosto_x`) ou escolha outra foto.
- **Crédito na legenda**, numa linha antes das hashtags: `Foto: Nome do autor, Wikimedia Commons (CC BY 2.0)`.
- **Nunca gere por IA o rosto de uma pessoa real**, nem peça ao Gemini ou ao ChatGPT para "melhorar" ou trocar a expressão dela. Imagem falsa de pessoa real é o tipo de coisa que derruba post e dá processo.
- Não ponha fala na boca dela e não sugira que ela usa ou recomenda o Convello. O texto fala do fato.
- Foto de evento não tem parede lisa, então o recorte automático não funciona: use `foto_de_pessoa` SEM `atras` (a foto ocupa o slide, escurecida embaixo) e ponha o objeto 3D só na beirada, como emenda para o slide 2.
- Não achou foto livre e boa (rosto grande, nítido, de frente ou três quartos)? Use o símbolo da empresa em objeto 3D e um personagem novo gerado, e diga isso na entrega.
- O final continua com personagem gerado (o dono de negócio que o post quer alcançar), nunca com a pessoa real fazendo a chamada.


**Olhe cada imagem gerada (Read) antes de usar.** Refaça se tiver: rosto diferente entre a capa e o final, pessoa parecida com a de outro carrossel, pele alaranjada ou bronzeada, halo ou brilho em volta, sombra ou objeto na parede (o recorte falha), celular cortado, mão com dedo errado, texto ou letra, objeto com placa atrás, ícone na cor errada. Peça para a produtora guardar a anterior com outro nome (às vezes a primeira era a melhor).

**Medir a foto** antes de pôr no slide: `python3 $M/regua.py foto <arquivo>` desenha uma régua de 50 em 50 px. Leia onde começa o cabelo, onde fica o queixo e o centro do rosto na largura, e passe para `foto_de_pessoa`. O enquadramento sai igual em todo carrossel: pessoa grande e o celular aparecendo acima do título.

"Melhora a luz" quer dizer a MESMA foto com outra luz: passe a foto de referência e peça para manter tudo e mudar só a iluminação. Trocar o rosto foi reprovado.

Nunca use gerador de imagem para tela de sistema (ele inventa a interface) nem para escrever texto na imagem.

Na entrega, diga quantas imagens foram pedidas e quais são geradas por IA.
