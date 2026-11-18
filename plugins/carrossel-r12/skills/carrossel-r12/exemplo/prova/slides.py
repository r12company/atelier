"""Prova de instalação: monta 1 slide de conteúdo sem precisar de nenhuma imagem.

  cp -r exemplo/prova "${CARROSSEIS:-$HOME/carrosseis}/00-prova"
  python3 motor/montar.py 00-prova 2

Saiu png/02.png e psd/02.psd na pasta 00-prova? O Atelier está funcionando neste computador.
"""
from comum import ATE, BRANCO, MARGEM, PECA_Y, SOMBRA, abrir, corpo, fechar, fio, manchete, pc, tema


def s2():
    abrir(2)
    y = manchete(['O Atelier está', '!funcionando aqui.'])
    corpo(['Este slide foi montado pelo motor, com a planta,', 'as fontes e a logo da marca.', '!Pode apagar a pasta 00-prova.'], y)
    pilulas = ['Fundo, logo e título: motor', 'A peça: você desenha', 'O fio: sempre no rodapé']
    h, vao = 120, 48
    topo = PECA_Y + (ATE - PECA_Y - 3 * h - 2 * vao) // 2
    for i, txt in enumerate(pilulas):
        yy = topo + i * (h + vao)
        pc.forma(f'PILULA-{i + 1}', 'roundedRect', MARGEM, yy, 920, h, tema()['tit'], h // 2, sombra=SOMBRA)
        pc.texto(f'PILULA-{i + 1}-TEXTO', txt, MARGEM + 56, yy + h // 2 + 12, 34, 600, tema()['tarja_texto'] if tema()['nome'] == 'azul' else BRANCO)
    fio('Agora é o seu carrossel', primeiro=True)
    fechar(2)


SLIDES = {2: s2}
