# Quatro ícones 3D numa imagem só

Para o slide de resumo: ícone grande (120 px) no lugar de número. Uma imagem com os quatro sai mais barata e todos ficam no mesmo estilo.
Formato: 1:1, fundo branco puro (o ícone entra em modo multiplicar, em cima de branco).

```text
Four 3D objects in a 2 by 2 grid, all the same size, each centered in its quadrant, with plenty of white space between them. Each object is a loose piece, seen from the front with a slight tilt, made of glossy blue plastic (blue #0A6BF0), rounded and chubby, with volume, soft reflections and small white details. IMPORTANT: there is no plate, square, circle or button behind the objects. They are not app icons. Only the loose objects on white. Top left: <object 1>. Top right: <object 2>. Bottom left: <object 3>. Bottom right: <object 4>. Background: pure white (#FFFFFF), flat, no gradient, no floor, no cast shadow. No text, no letters, no numbers, no watermark.
```

Exemplo que deu certo (carrossel 02): dois balões de conversa sobrepostos; um boneco simples de pessoa com um selo redondo branco de confirmação; um relógio de parede redondo com mostrador branco; um funil de três faixas.

Depois de salvar em `geradas/icones.png`, recorte cada um:
```bash
magick geradas/icones.png -crop 2x2@ +repage -fuzz 4% -trim +repage geradas/icone-%d.png
```
e dê nome a cada arquivo (`icone-conversas.png`...).
