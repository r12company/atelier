# Quatro ícones 3D numa imagem só

Para o slide de resumo: ícone grande (120 px) no lugar de número. Uma imagem com os quatro sai mais barata e todos ficam no mesmo estilo.
Formato: 1:1, fundo branco puro (o ícone entra em modo multiplicar, em cima de branco).

```text
Four 3D objects in a 2 by 2 grid, all the same size, each centered in its quadrant, with plenty of white space between them. Each object is a loose piece, seen from the front with a slight tilt, made of glossy green plastic (green #95db30), rounded and chubby, with volume, soft reflections and small white details. IMPORTANT: there is no plate, square, circle or button behind the objects. They are not app icons. Only the loose objects on white. Top left: <object 1>. Top right: <object 2>. Bottom left: <object 3>. Bottom right: <object 4>. Background: pure white (#FFFFFF), flat, no gradient, no floor, no cast shadow. No text, no letters, no numbers, no watermark.
```

Exemplo para um resumo da R12 (anúncio, página, WhatsApp, Google): um megafone; uma página de site com um botão; dois balões de conversa sobrepostos; uma lupa. Sem logo de outra marca: o objeto é genérico.

Depois de salvar em `geradas/icones.png`, recorte cada um:
```bash
magick geradas/icones.png -crop 2x2@ +repage -fuzz 4% -trim +repage geradas/icone-%d.png
```
e dê nome a cada arquivo (`icone-megafone.png`...).
