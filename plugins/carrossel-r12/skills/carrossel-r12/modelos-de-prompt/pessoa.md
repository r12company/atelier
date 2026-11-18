# Personagem da capa e do final

Personagem NOVO a cada carrossel: outra pessoa (varie homem e mulher, idade, cabelo, roupa, profissão ligada ao assunto), outra pose, outro gesto.
Dentro do mesmo carrossel a capa e o final são a mesma pessoa: gere a capa primeiro e anexe ela no pedido do final.

R12: gente de verdade, dono de pequeno negócio, com roupa verde quando fizer sentido (a capa da proposta de SEO usou camisa verde, aprovada).
Foto do Gemini: antes de montar, alise a parede (`python3 $M/alisar.py <carrossel>/geradas/<foto>.png`). Ele grava `<foto>-lisa.png` e `<foto>-lisa-mascara.png`; use a `<foto>-lisa.png` no `slides.py` e o motor acha a máscara ao lado e recorta a pessoa por ela. Se o cabelo chega perto do topo, o motor faz a máscara na hora. Se a máscara cobre mais de 70% da foto (levou a parede junto), dá erro: gere outra com mais parede em volta.
O motor também dá erro se a pessoa encosta na caixa da logo (logo em cima do cabelo é proibido): por isso o bloco 4 pede parede sobrando dos lados.

Formato: 3:4 no Gemini (AI Studio) ou retrato 2:3 no ChatGPT; para stories, 9:16 (troque "Vertical 3:4 image" por "Vertical 9:16 image, with more plain wall above the head and below the waist"). Salvar em `geradas/` como PNG.

## Blocos (junte nesta ordem)

**1. Quem é** (escreva para este carrossel):
`Studio photograph of <who: age, hair, clothes, job related to the topic>.`

**2. Gente de verdade** (copie):
```text
A Brazilian person with an ordinary, real look, like the owner of a small local business (a clinic, a shop, a restaurant), not a catalog model. Natural expression, no forced smile.
```

**3. Pose e olhar** (escreva). Na capa a pessoa olha para o que importa (o celular, o objeto 3D), que fica logo acima do título. No final ela olha para a câmera, tranquila. O gesto conta o assunto: notebook, atrás do balcão da loja, apontando para cima, abrindo a porta do negócio, braços cruzados. Nem todo mundo segurando celular.

**4. Foto para recorte** (copie; é o que deixa o motor pôr objetos atrás da pessoa):
```text
Framing from the waist up: the top of the hair is close to the top edge and the face is large. The person fills about two thirds of the width, with plain wall left on both sides. Background: a very light gray studio wall, smooth and even, no strong gradient, no shadow on the wall and no objects at all: this photo will be cut out. The clothes contrast with the wall: never white, light gray or beige. Do not draw icons or anything floating. Soft studio light from the upper left, a light shadow on the right side of the face, true skin color with no orange tint. No halo and no glowing outline around the body. Sharp focus, 85mm lens. No text at all. Vertical 3:4 image.
```

## Final: a mesma pessoa

Anexe a capa aprovada e comece com:
```text
Studio photograph of the SAME person as in the attached reference image: the same face, the same age, the same hair, the same skin color and the same clothes.
```
Depois o bloco 3 (pose do final, olhando para a câmera) e o bloco 4.

## Exemplo (no estilo da capa da proposta de SEO, em `exemplo/folha-pdf-seo.jpg`)

```text
Studio photograph of a Brazilian woman in her late 30s, shoulder-length dark hair, green button-up shirt, owner of a small dental clinic. A Brazilian person with an ordinary, real look, like the owner of a small local business (a clinic, a shop, a restaurant), not a catalog model. Natural expression, no forced smile. She holds the phone at chest height and looks at the screen, curious, as if searching for something. The phone is fully visible. Framing from the waist up: ... (bloco 4 inteiro)
```

## Refaça se tiver

Rosto diferente entre a capa e o final, pessoa parecida com a de outro carrossel, pele alaranjada ou bronzeada, halo ou brilho em volta, sombra ou objeto na parede (o recorte falha), celular cortado, mão com dedo errado, qualquer texto ou letra.
