# Copy: roteiro, texto dos slides e legenda

Modelo de roteiro e de legenda: os exemplos desta página (seções 2 e 5). Peças prontas para copiar em `exemplo/slides-pdf-seo.py`, folha em `exemplo/folha-pdf-seo.jpg`.
Voz da R12: a da seção 4 (português simples, resultado no negócio do cliente, nada de palavra de anúncio).

## 1. De onde vem o roteiro

| Situação | O que fazer |
| --- | --- |
| Quem pediu mandou o roteiro (às vezes feito no ChatGPT) | Está aprovado. Não mude a ideia nem a ordem: encaixe na planta (item 3) e monte. Se pedir duas chamadas (comentar e seguir), o slide leva uma só e a outra vai para a legenda sem ser pedido |
| Mandou só o tema | Escreva o roteiro no formato do exemplo da seção 2 (1 linha por slide), mande em texto e só monte depois do OK |

O dono da marca já reprovou um roteiro inteiro depois de montado. Texto é barato de trocar; slide montado não.
**Roteiro aprovado fica travado:** redesenho e polimento mudam só a arte (composição, peça, quebra de linha), nunca as frases. Correção de fato ou de fonte pode, e se avisa.
O roteiro encaixado fica em `<carrossel>/roteiro.md`, sempre.

## 2. A história em 6 a 10 slides

Uma ideia por slide. A estrutura que funciona:

| Slides | Papel | No exemplo abaixo |
| --- | --- | --- |
| 1 | Capa: a frase que para o dedo | Seu anúncio traz gente / PARA ONDE? |
| 2 a 4 | O problema, um passo por slide, piorando | a pessoa clica, cai num perfil sem informação, desiste |
| 5 a 8 | A saída, uma coisa por slide, cada uma com a prova | página com o que ela procura, botão do WhatsApp, aparecer no Google |
| penúltimo | Resumo para salvar: lista com ícones grandes | 3 ou 4 itens e uma frase de fecho |
| último | Final: frase que fecha e UMA chamada | Anúncio bom precisa de / UM DESTINO / Fale com a R12 |

Exemplo de roteiro (tema "anúncio sem site perde venda"), uma linha por slide:

```text
01 capa: Seu anúncio traz gente / PARA ONDE? / tarja: pense antes de pagar
02: A pessoa viu o anúncio / !e clicou. | fio: E depois do clique?
03: Caiu num perfil / !sem preço, sem endereço. | fio: O que ela faz?
04: Ela volta para a busca / !e acha outra empresa. | fio: Como segurar esse cliente?
05: Uma página feita / !para quem clicou. | fio: O que vai nela?
06: O que ela procura, / !na primeira tela. | fio: E se quiser falar?
07: Um toque e cai / !no seu WhatsApp. | fio: E sem anúncio?
08: Página boa também / !aparece no Google. | fio: Resumindo
09: resumo: anúncio, página, WhatsApp, Google
10 final: Anúncio bom precisa de / UM DESTINO / Fale com a R12
```

Post de notícia ou de opinião segue o mesmo arco: o fato, o que muda, o detalhe que importa, o que a R12 pensa, a chamada.

### Post editorial (notícia)

Para notícia de marketing, anúncio e busca (uma mudança do Google, do Instagram, da Meta) a R12 fala como quem entende do assunto, não como anúncio. Arco de 9 slides, um papel por slide:

| Slide | Papel | O que leva |
| --- | --- | --- |
| 1 | Capa (foto) | A manchete: o fato mais forte em poucas palavras, com curiosidade |
| 2 | A notícia | Quem fez o quê, quando, com a fonte por trás |
| 3 | O detalhe | O número, a contradição ou a descoberta que surpreende |
| 4 | O contexto | Como funcionava antes |
| 5 | A virada | O que está mudando |
| 6 | A consequência | Por que importa para quem anuncia ou quer aparecer no Google |
| 7 | A lição | O que isso ensina para quem tem empresa |
| 8 | A visão da R12 | Leitura de agência, sem propaganda: a R12 aparece como quem entende de tráfego, site e busca |
| 9 | Encerramento (foto) | Frase memorável na linha e na palavra gigante; a chamada convida a comentar |

- Cada afirmação sai da pesquisa verificada (`pesquisa.md`). O que não está confirmado não vira fato: sai, ou vai no condicional com a ressalva ("segundo o Google", "em teste").
- Nunca invente número, declaração ou lançamento. Teste não é lançamento; anúncio não é disponibilidade.
- Fala de terceiros: parafraseie. No máximo uma citação curta (até 15 palavras) por carrossel, com quem disse.
- Slide 8 sem "contrate", sem preço, sem "a R12 resolve". Mostra o ponto de vista.

### Fontes, data e revisão factual

Ficam no `copy.md` da peça (seção 7): o tipo (notícia ou serviço), a data da notícia, a revisão factual e as fontes com link. O `conferir.py` lê de lá.

## 3. O encaixe na planta

O slide tem lugares fixos. O texto do roteiro é distribuído neles, cortando até caber, sem mudar a ideia.
O motor mede cada linha e dá erro com quantos px passou: encurte, nunca diminua a letra.

| Lugar | Cabe | Papel |
| --- | --- | --- |
| Capa: linha pequena | até uns 26 caracteres | começa a frase |
| Capa: palavra gigante | 1 ou 2 palavras em maiúsculas. Até umas 7 letras sai em 256; com 9 ou 10 letras cai para uns 190 (o motor diz o valor) | o centro da frase |
| Capa: tarja | até uns 22 caracteres | termina a frase |
| Título do slide | 2 linhas em Oswald 82 a 92, até uns 20 caracteres cada | a ideia do slide. A 2ª linha é o destaque (começa com `!`) |
| Texto de apoio | 2 linhas, até uns 52 caracteres cada, só quando indispensável | prepara a frase em tarja |
| Frase em tarja | 1 linha, até uns 45 caracteres | a conclusão: quem pula o texto lê só isto |
| Pergunta do fio | até uns 30 caracteres | a ponte: é o assunto do slide seguinte |
| Final: linha, palavra e chamada | como a capa; chamada = verbo + palavra | "Fale com a" + "R12", ou "Comente" + "R12" |

### Régua de texto por slide de conteúdo

Dono da marca: "não pôr tanto conteúdo textual, que vai poluir e ficar difícil de ler". O visual aprovado da R12 (proposta de SEO, `exemplo/folha-pdf-seo.jpg`) é ainda mais enxuto: título grande, UMA imagem, o fio.

| Pode ter | Limite |
| --- | --- |
| Título | 2 linhas |
| Texto de apoio | 2 linhas, só quando indispensável |
| Tarja | 1 |
| Texto dentro da peça | rótulos curtos, até uns 20 palavras no total |
| Fonte | no máximo 1 linha |
| Fio | 1 pergunta |
| Total | mire em 40 palavras; o `conferir.py` avisa acima de 75 palavras ou 14 blocos |

Nada de nota, ressalva, rótulo e cartão empilhados. O detalhe que não cabe vai para a legenda.

- As três partes da capa leem como UMA frase. Frase comprida no roteiro vira: começo na linha, o miolo forte na palavra, o resto na tarja.
- Texto e tarja são uma frase contínua: "Quando ela não acha o preço," + tarja "volta para a busca e clica no próximo."
- A pergunta do fio de um slide é respondida pelo título do seguinte: "O que ela faz?" e depois "Ela volta para a busca."
- Citação ou pergunta que o roteiro traz entre aspas vira a PEÇA (um balão, um cartão de busca), não texto de apoio.
- O que não coube no slide vai para a legenda.

## 4. Regras de texto

- Português simples, frase curta. Fale do resultado no negócio do cliente ("mais gente chamando no WhatsApp", "aparecer no Google quando procuram o que você vende"), não da ferramenta.
- Nunca: travessão, emoji nos slides (na legenda, só como pontuação, ver a seção 5), palavra de anúncio ("revolucionário", "solução completa", "potencializar", "alavancar").
- Nunca inventar número, estatística, depoimento ou caso de cliente. Sem prova, a frase fica sem número.
- Nunca citar cliente da R12 sem autorização dele, nem concorrente. Nunca prometer resultado garantido ("primeiro lugar garantido", "dobra as vendas").
- O texto do slide fala do que a peça mostra. Se o texto cita "botão do WhatsApp", a peça mostra o botão.
- Vermelho é só para o problema. A solução é verde.

**Notícia ou fato de fora** (o que o Google ou a Meta mudou, uma regra nova, um dado de mercado): confira na fonte com WebSearch antes de montar e anote o link e a data no `roteiro.md`. O que não confirmar, não afirme: avise o dono da marca em 1 linha e escreva no condicional ou tire.

## 5. Legenda (seção "Legenda" do `copy.md` da peça)

1. **Primeira linha: até 125 caracteres.** É o que aparece antes do "mais". Uma cena concreta, não um resumo. Sem saudação nem hashtag; um emoji no começo para marcar o tom pode (⚠️, 📲).
2. **Curta e com cara de post** (dono da marca: "não muito extensa", "mais uma copy do post"): 400 a 900 caracteres, não 2.000. O `conferir.py` avisa acima de 1.000 e lê a `legenda-curta.txt` quando ela existe. **Parágrafos curtos**, com uma linha em branco entre eles; o que é lista vira lista curta, uma linha por item. Conte a história do carrossel em texto corrido, com as palavras que a pessoa buscaria ("anúncio no Instagram", "aparecer no Google", "landing page") em frase normal.
3. **Uma chamada só**, a mesma do último slide: "Fale com a R12 e a gente olha o seu caso." ou "Comente R12 que a gente te chama."
4. **3 hashtags** específicas, na seção "Hashtags" do `copy.md` (quem posta cola na última linha): `#R12Company` e duas do assunto. O Instagram aceita no máximo 5.
5. **Emoji quando ajuda** (dono da marca: "tem que ter emojis quando necessário"): como pontuação, nunca enfeite. Um no começo para o tom, um por item de lista curta (✅, 📍, 🔎, 💬) e um 👇 na chamada. No máximo uns 8. Nos slides, nenhum.
6. Sem link (não é clicável), sem travessão. WhatsApp e site ficam na bio do @r12_company, não na legenda.

Exemplo de legenda (o roteiro da seção 2):

```text
📲 A pessoa viu seu anúncio, clicou e caiu num perfil sem preço e sem endereço.

Ela não pergunta. Volta para a busca e clica na próxima empresa.

Anúncio traz gente. O que segura essa gente é o lugar onde ela cai:
✅ o que ela procura logo na primeira tela
💬 um botão que abre o seu WhatsApp
🔎 uma página que também aparece no Google

Antes de aumentar a verba, olhe para onde o anúncio está mandando.

👇 Fale com a R12 e a gente olha o seu caso.
```

O `motor/conferir.py` mede tudo isso (lê a seção "Legenda" do `copy.md` da peça). As skills `ig-caption` e `ig-human` só leem inglês: a nota delas não vale para texto em português.
Nada é postado por você: quem posta cola a legenda e publica.

## 6. Ganchos em forma de história

O gancho é a capa (ou a 1ª tela, ou o card) e a primeira linha da legenda. Cinco moldes que funcionam. Escolha um por peça e varie entre as peças da semana.
Regra para todos: **nada inventado**. Hora, número, fala e caso só se forem reais (do cliente, com autorização, da pesquisa, da fonte); nos exemplos os números são de mentira, só para mostrar a forma.

### 6.1 A história hora a hora

```
21h10: alguém procura "dentista perto de mim".
21h11: sua clínica não aparece na busca.
21h12: ela marca com a primeira que apareceu.
```
- **Como:** 3 ou 4 marcas de hora, uma ação curta em cada, a última é a perda (ou a virada). No carrossel, uma hora por slide; nos stories, uma por tela; no card, as três numa peça só (linha do tempo).
- **Quando usar:** problema que acontece com o tempo (busca sem resposta, clique que não vira contato, cliente que esfria).
- **Regra:** hora no formato 21h10, verbo no presente, nada de adjetivo. A conclusão fica para o slide seguinte ou para a legenda.

### 6.2 A pergunta que acusa

```
O anúncio não vende. Quem é o culpado?
```
- **Como:** um fato curto e uma pergunta que aponta (quem, o quê, onde). A resposta vem no slide 2, e quase nunca é quem o leitor pensa (é o caminho depois do clique, não o anúncio).
- **Quando usar:** quando o post desmonta uma culpa comum ("o algoritmo", "o Instagram", "a verba").
- **Regra:** a pergunta acusa a situação, nunca uma pessoa ou empresa real. Não use para atacar concorrente.

### 6.3 O número que choca

```
300 cliques. 2 mensagens.
```
- **Como:** dois números curtos, lado a lado, que não batem. Na capa, o número vai na palavra gigante; no card, no molde "número que choca" (`formatos.md`).
- **Quando usar:** quando há um dado real que mostra o tamanho do problema (de um cliente, com autorização, ou de pesquisa com fonte).
- **Regra:** sem fonte, sem número. Escreva a fonte na legenda ou em 1 linha no slide. Arredondar pode; inventar, nunca.

### 6.4 O que faz e o que não faz

```
O que o SEO faz: põe sua empresa na busca de quem procura.
O que ele não faz: trazer cliente na semana que vem.
```
- **Como:** duas colunas ou dois slides seguidos, "faz" e "não faz", 3 itens no máximo de cada lado. Fecha com o que o leitor tem de fazer.
- **Quando usar:** para tirar expectativa errada (anúncio, site, SEO) e ganhar confiança. Funciona bem perto do fim do carrossel.
- **Regra:** o "não faz" é verdade e é dito sem medo; prometer demais foi reprovado (nunca resultado garantido).

### 6.5 O post único (estático): uma frase e uma peça

```
Quem procura no Google escolhe entre os três primeiros.
```
- **Como:** um card (`formatos.md`): a frase no título (até 2 linhas) e uma peça só que prova a frase (uma busca desenhada, um gráfico, um objeto). Nada de texto de apoio comprido.
- **Quando usar:** ideia que cabe numa frase e não precisa de passo a passo; dia de agenda cheia; resposta rápida a um assunto do momento.
- **Regra:** se precisar de mais de uma peça para provar, vira carrossel. Frase com dado (como a do exemplo) só com fonte.

## 7. O `copy.md` da peça (entrega obrigatória)

Toda peça (carrossel, card ou stories) tem um `copy.md` na pasta dela, **sempre com estes títulos, nesta ordem**. É o que vai para quem aprova e o que o `conferir.py` lê.

```markdown
# Copy: <tema da peça>

## Formato e horário
- **Formato:** carrossel (10 slides, 3:4)       (ou card 4:5, ou stories 4 telas)
- **Data e horário sugeridos:** segunda 08/12, 9h   (do referencias/calendario.md)
- **Tipo:** serviço            (ou notícia)
- **Revisão factual:** aprovada   (ou "aprovada com ressalvas: ...", ou "bloqueada: motivo")
- **Data da notícia:** 05/12/2026   (só em notícia)

## Gancho
A primeira linha da legenda, até 125 caracteres, igual à que abre a legenda.

## Legenda
A legenda inteira, pronta para colar: a mesma primeira linha, parágrafos curtos, emoji como
pontuação, a chamada uma vez. Sem hashtag aqui (elas ficam na seção abaixo). Stories: escreva "não tem".

## Chamada
Fale com a R12      (uma só, a mesma do último slide)

## Hashtags
#R12Company #TrafegoPago #LandingPage      (até 5; o padrão é 3)

## Texto alternativo
01: o que a imagem mostra, em uma frase, com o texto principal
02: ...

## Texto de cada slide
01: Seu anúncio traz gente / PARA ONDE? / pense antes de pagar
02: A pessoa viu o anúncio / e clicou. | fio: E depois do clique?

## Adesivo
(só stories) tela 3: enquete "Seu anúncio leva para onde?" Site / Perfil, entre 900 e 1200 px

## Fontes
- [Título da matéria](https://...), Veículo, 05/12/2026      (só notícia: pelo menos 2, com link)

## Imagens
- capa: gerada por IA, marcada como ilustrativa      (ou arquivo, autor, licença e link da foto real)
- slide 6: site de cliente da R12, autorizado por ele      (print real: diga de onde veio e que há autorização)
```

Na hora de postar, quem posta cola a seção "Legenda" e, na linha de baixo, as "Hashtags".
