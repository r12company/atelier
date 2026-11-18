# Personagem da capa e do final

Personagem NOVO a cada carrossel: outra pessoa (varie homem e mulher, idade, cabelo, roupa, profissão ligada ao assunto), outra pose, outro gesto.
Dentro do mesmo carrossel a capa e o final são a mesma pessoa: gere a capa primeiro e anexe ela no pedido do final.

R12: gente de verdade, dono de pequeno negócio, com roupa verde quando fizer sentido (a capa da proposta de SEO usou camisa verde, aprovada).
Foto do Gemini: antes de montar, alise a parede (`python3 $M/alisar.py <carrossel>/geradas/<foto>.png`) e use o recorte pela máscara (`_recorte_pela_mascara` em `exemplo/slides-pdf-seo.py`). O recorte automático leva a parede junto.

Formato: 3:4 no Gemini (AI Studio) ou retrato 2:3 no ChatGPT; para stories, 9:16 (troque "Vertical 3:4 image" por "Vertical 9:16 image, with more plain wall above the head and below the waist"). Salvar em `geradas/` como PNG.

## Blocos (junte nesta ordem)

**1. Quem é** (escreva para este carrossel):
`Studio photograph of <who: age, hair, clothes, job related to the topic>.`

**2. Gente de verdade** (copie):
```text
A Brazilian person with an ordinary, real look, like a small business owner or someone from a sales team, not a catalog model. Natural expression, no forced smile.
```

**3. Pose e olhar** (escreva). Na capa a pessoa olha para o que importa (o celular, o objeto), que fica logo acima do título. No final ela olha para a câmera, tranquila. O gesto conta o assunto: notebook, café, abrindo uma caixa, sacolas de compras, sofá com controle remoto, braços cruzados, mala de viagem. Nem todo mundo segurando celular.

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

## Exemplo (no estilo da capa do carrossel 02, em `exemplo/folha.jpg`)

```text
Studio photograph of a Brazilian man in his early 30s, short dark hair, trimmed beard, navy blue button-up shirt. A Brazilian person with an ordinary, real look, like a small business owner or someone from a sales team, not a catalog model. Natural expression, no forced smile. He holds the phone with both hands at chest height and looks at the screen, worried, eyebrows raised and mouth slightly open. The phone is fully visible. Framing from the waist up: ... (bloco 4 inteiro)
```

## Refaça se tiver

Rosto diferente entre a capa e o final, pessoa parecida com a de outro carrossel, pele alaranjada ou bronzeada, halo ou brilho em volta, sombra ou objeto na parede (o recorte falha), celular cortado, mão com dedo errado, qualquer texto ou letra.
