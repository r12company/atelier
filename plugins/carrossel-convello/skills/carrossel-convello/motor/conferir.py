"""Conferência final do carrossel, antes de entregar. O que dá para medir, mede aqui.

  python3 motor/conferir.py <pasta-do-carrossel>

Vale para os três formatos: carrossel (6 a 10 slides), card (post único, 1 slide) e stories (1080x1920, 3 a 6 telas).
Confere os arquivos (slides em 1080x1440, 1080x1350 ou 1080x1920, todos iguais, PSD de cada um, folha), a ordem (capa e final de foto, fundos
intercalados), o texto de cada slide (régua do TikTok: palavras e blocos), o roteiro e a legenda (primeira linha, uma
chamada só, hashtags, travessão, excesso de emoji, link, tamanho). A legenda lida é a legenda-curta.txt, se existir.
ERRO impede a entrega. AVISO é para ler e decidir.
"""
import ast
import json
import os
import re
import subprocess
import sys

RAIZ = os.path.abspath(os.path.expanduser(os.environ.get('CARROSSEIS', '~/carrosseis')))
if len(sys.argv) < 2:
    raise SystemExit(__doc__)
PASTA = sys.argv[1] if os.path.isdir(sys.argv[1]) else os.path.join(RAIZ, sys.argv[1])
erros, avisos = [], []
TRAVESSAO = re.compile('[\u2012-\u2015]')
EMOJI = re.compile('[\U0001F000-\U0001FFFF☀-➿]')
# Régua de texto por slide de conteúdo, medida no 02-tiktok-shop (o melhor da campanha de 15/11): 47 a 75 palavras, até 14 blocos.
MAX_PALAVRAS, MAX_BLOCOS = 75, 14
# Texto que não aparece no slide: nome de camada, cor, arquivo, opção de função.
TECNICO = re.compile(r'^(-?[A-Z0-9][A-Z0-9_\-{} ]*|#[0-9A-Fa-f]{3,8}|.*\.(png|jpe?g|svg|psd)|[a-z_]+|roundedRect)$')


def secao(txt, titulo):
    """Conteúdo de uma seção '## titulo' de um .md, até a próxima seção."""
    m = re.search(r'(?ms)^## ' + re.escape(titulo) + r'[^\n]*\n(.*?)(?=^## |\Z)', txt or '')
    return m.group(1).strip() if m else None


def ler(nome):
    arq = os.path.join(PASTA, nome)
    return open(arq, encoding='utf-8').read() if os.path.exists(arq) else None


# ── slides ──
png = os.path.join(PASTA, 'png')
nums = sorted(int(f[:2]) for f in os.listdir(png) if re.fullmatch(r'\d\d\.png', f)) if os.path.isdir(png) else []
if not nums:
    erros.append('não há slides em png/: monte com o montar.py')
elif nums != list(range(1, len(nums) + 1)):
    erros.append(f'os slides têm de ir de 01 a {len(nums):02d} sem pular: {nums}')
tamanhos = set()
for n in nums:
    tam = subprocess.run(['magick', 'identify', '-format', '%wx%h', os.path.join(png, f'{n:02d}.png')], capture_output=True, text=True).stdout
    tamanhos.add(tam)
    if tam not in ('1080x1440', '1080x1350', '1080x1920'):
        erros.append(f'slide {n:02d} está em {tam}: o motor monta 1080x1440 (3:4), 1080x1350 (4:5) ou 1080x1920 (stories)')
if len(tamanhos) > 1:
    erros.append(f'slides em tamanhos diferentes ({", ".join(sorted(tamanhos))}): monte todos de novo com o mesmo ALTURA')
    if not os.path.exists(os.path.join(PASTA, 'psd', f'{n:02d}.psd')):
        erros.append(f'slide {n:02d} sem PSD: tem de ser montado no PhotoCraft, pelo montar.py')
CARD = nums == [1]
STORIES = tamanhos == {'1080x1920'}
FORMATO = 'card' if CARD else ('stories' if STORIES else 'carrossel')
if STORIES and not 3 <= len(nums) <= 6:
    avisos.append(f'{len(nums)} telas de stories: o normal é de 3 a 6')
elif FORMATO == 'carrossel' and nums and not 6 <= len(nums) <= 10:
    avisos.append(f'{len(nums)} slides: o normal é de 6 a 10')
if CARD and '1080x1920' in tamanhos:
    erros.append('card é post de feed: 1080x1350 ou 1080x1440, não 1080x1920')
# Régua de texto: carrossel 75 palavras e 14 blocos por slide; card e stories são lidos mais rápido
MIRA = 60  # o alvo de palavras por slide (referencias/copy.md, seção 3); card e stories: 30 (referencias/formatos.md)
if FORMATO != 'carrossel':
    MAX_PALAVRAS, MAX_BLOCOS, MIRA = 50, 10, 30
if nums and not os.path.exists(os.path.join(PASTA, 'folha.jpg')):
    erros.append('sem folha.jpg: rode o montar.py sem número de slide')

fichas = json.loads(ler('planta.json') or '{}')
for n in nums:
    f = fichas.get(str(n))
    if not f:
        erros.append(f'slide {n:02d} não foi montado pelo motor (não está em planta.json)')
        continue
    if CARD:
        if f['tipo'] not in ('card', 'foto'):
            erros.append('card: monte com abrir(1, card=True) ou abrir_foto(1)')
        continue
    certo = 'foto' if n in (1, nums[-1]) else 'conteudo'
    if f['tipo'] != certo:
        erros.append(f'slide {n:02d}: a capa e o final são de foto e os do meio de conteúdo')
    if certo == 'conteudo' and f.get('tema') != ('branco' if n % 2 == 0 else 'azul'):
        erros.append(f'slide {n:02d}: fundo fora da ordem (par branco, ímpar azul)')

codigo = ler('slides.py')
if codigo is None:
    erros.append('sem slides.py na pasta do carrossel')
elif TRAVESSAO.search(codigo):
    erros.append('travessão dentro do slides.py')
if codigo:
    # Conta o texto visível de cada slide do meio: toda frase escrita dentro da função sN (sem docstring nem nome de camada).
    # ponytail: texto montado fora da função sN (constante do módulo, helper) não entra na conta.
    try:
        funcs = {int(f.name[1:]): f for f in ast.parse(codigo).body
                 if isinstance(f, ast.FunctionDef) and re.fullmatch(r's\d+', f.name)}
    except SyntaxError:
        funcs = {}
    cheios = []
    for n in (nums if CARD else nums[1:-1]):
        if n not in funcs:
            continue
        doc = (ast.get_docstring(funcs[n]) or '').strip()
        blocos = [c.value.strip().lstrip('!') for c in ast.walk(funcs[n])
                  if isinstance(c, ast.Constant) and isinstance(c.value, str) and c.value.strip()
                  and c.value.strip() != doc and not TECNICO.match(c.value.strip())]
        palavras = sum(len(b.split()) for b in blocos)
        if palavras > MAX_PALAVRAS or len(blocos) > MAX_BLOCOS:
            cheios.append(f'{n:02d} ({palavras} palavras, {len(blocos)} blocos)')
    if cheios:
        avisos.append(f'texto demais (régua: até {MAX_PALAVRAS} palavras e {MAX_BLOCOS} blocos por slide no {FORMATO}, mire em {MIRA}): '
                      + ', '.join(cheios) + '. Corte notas, rótulos e cartões empilhados')
for sobra in ('previa',):
    if os.path.isdir(os.path.join(PASTA, sobra)):
        avisos.append(f'a pasta {sobra}/ ainda existe: os slides que valem são os de png/. Apague a prévia quando terminar')

COPY = ler('copy.md')  # a copy da peça (modelo em referencias/copy.md, seção 7)
LEGENDA = ler('legenda-curta.txt') or ler('legenda.txt') or secao(COPY, 'Legenda')
if not LEGENDA or LEGENDA.strip().lower().startswith('não tem'):  # stories não têm legenda
    LEGENDA = None

# ── roteiro ──
roteiro = ler('roteiro.md')
if roteiro is None:
    erros.append('sem roteiro.md: o roteiro aprovado fica guardado na pasta do carrossel')
elif TRAVESSAO.search(roteiro):
    erros.append('travessão no roteiro.md')

# ── publicação: texto alternativo, fontes, data e revisão factual ──
pub = ler('publicacao.md') or COPY
if pub is None:
    erros.append('sem copy.md (formato, gancho, legenda, chamada, hashtags, texto alternativo, texto de cada slide, fontes): modelo em referencias/copy.md, seção 7')
else:
    if TRAVESSAO.search(pub):
        erros.append('travessão no copy.md')
    tipo = re.search(r'(?im)^- \*\*Tipo:\*\*\s*(\S+)', pub)
    revisao = re.search(r'(?im)^- \*\*Revisão factual:\*\*\s*(.+)$', pub)
    if not tipo:
        erros.append('copy.md sem a linha "- **Tipo:** notícia" (ou produto)')
    if not revisao:
        erros.append('copy.md sem a linha "- **Revisão factual:** ..."')
    elif revisao.group(1).strip().lower().startswith('bloquead'):
        erros.append(f'revisão factual: {revisao.group(1).strip()}. Não publicar')
    alts = re.findall(r'(?m)^(\d{2}):\s*\S', secao(pub, 'Texto alternativo') or '')
    if sorted(int(a) for a in alts) != nums:
        erros.append(f'texto alternativo: tem de haver uma linha "NN: ..." para cada slide ({len(nums)}), achei {len(alts)}')
    if tipo and tipo.group(1).lower().startswith('not'):
        fontes = re.findall(r'https?://\S+', secao(pub, 'Fontes') or '')
        if len(fontes) < 2:
            erros.append(f'post de notícia com {len(fontes)} fonte(s) em "## Fontes": precisa de pelo menos 2, com link')
        if not re.search(r'(?im)^- \*\*Data da notícia:\*\*\s*\d{1,2}/\d{1,2}/\d{4}', pub):
            erros.append('post de notícia sem "- **Data da notícia:** DD/MM/AAAA"')
    imagens = secao(pub, 'Imagens') or ''
    leg_txt = LEGENDA or ''
    if re.search(r'CC BY', imagens) and not re.search(r'(?i)foto', leg_txt):
        erros.append('foto com licença CC BY e a legenda sem o crédito ("Foto: autor, Wikimedia Commons (licença)")')
    primeira = re.search(r'(?im)^- \*\*Primeira frase:\*\*\s*(.+)$', pub) or re.search(r'(?s)(.+)', secao(pub, 'Gancho') or '')
    leg = LEGENDA
    if not primeira and not STORIES:
        erros.append('copy.md sem a seção "## Gancho" (a primeira linha da legenda)')
    elif leg and primeira.group(1).strip() != leg.strip().splitlines()[0].strip():
        avisos.append('o gancho do copy.md não é a primeira linha da legenda')

# ── legenda ──
legenda = LEGENDA
if legenda is None and STORIES:
    pass  # stories não têm legenda
elif legenda is None:
    erros.append('sem legenda.txt')
else:
    linhas = [l for l in legenda.strip().splitlines()]
    if TRAVESSAO.search(legenda):
        erros.append('travessão na legenda')
    emojis = EMOJI.findall(legenda)
    if len(emojis) > 8:
        erros.append(f'{len(emojis)} emojis na legenda: emoji é pontuação (tom, itens de lista, chamada), no máximo uns 8')
    if re.search(r'https?://|www\.', legenda):
        erros.append('link na legenda: no Instagram ele não é clicável. Link vai na bio')
    if len(linhas[0]) > 125:
        erros.append(f'a primeira linha da legenda tem {len(linhas[0])} caracteres: o Instagram corta em 125')
    tags = re.findall(r'#\w+', legenda)
    if len(tags) > 5:
        erros.append(f'{len(tags)} hashtags: o Instagram aceita até 5 (o padrão aqui é 3)')
    if tags and not linhas[-1].startswith('#'):
        avisos.append('as hashtags vão sozinhas na última linha')
    pedidos = re.findall(r'(?i)\b(comente|comenta|salve|salva|compartilhe|envie|mande|siga|segue|clique|acesse|chame|marque)\b', legenda)
    if len(pedidos) != 1:
        (erros if not pedidos else avisos).append(
            f'a legenda tem {len(pedidos)} pedidos ({", ".join(pedidos) or "nenhum"}): é uma chamada só, a mesma do último slide')
    if len(legenda) > 2200:
        erros.append('legenda com mais de 2.200 caracteres')
    elif len(legenda) > 1000:
        avisos.append(f'legenda com {len(legenda)} caracteres: o padrão é curto, de 400 a 900 (referencias/copy.md, seção 5)')
    chamada = re.search(r"chamada\(\s*'([^']*)'\s*,\s*'([^']*)'", codigo or '')
    if chamada and chamada.group(2).lower() not in legenda.lower():
        erros.append(f'o último slide pede "{chamada.group(1)} {chamada.group(2)}" e a legenda não repete essa chamada')

for a in avisos:
    print('AVISO:', a)
for e in erros:
    print('ERRO:', e)
print()
if erros:
    print(f'NÃO ESTÁ PRONTO: {len(erros)} erro(s).')
    sys.exit(1)
print(f'CONFERIDO ({FORMATO}): {len(nums)} slide(s), roteiro e legenda. Falta o seu olho: abra planta/folha-com-regua.jpg e planta/panorama.jpg.')
