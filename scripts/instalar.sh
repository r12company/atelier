#!/usr/bin/env bash
# Instalador do Atelier para o Claude Code (Linux e Mac).
#
#   curl -fsSL https://raw.githubusercontent.com/r12company/atelier/main/scripts/instalar.sh | bash
#   curl -fsSL .../instalar.sh | bash -s -- carrossel-r12      instala só uma skill
#
# O que faz: baixa a versão mais nova do repositório, copia as skills para ~/.claude/skills/ (a versão que já
# existia fica guardada como <nome>.antiga), instala as fontes, instala o PhotoCraft no Linux se faltar e roda o
# checar.py para dizer o que ainda falta. Pode rodar quantas vezes quiser.
# Teste sem baixar nada: ORIGEM=/caminho/do/repositorio bash scripts/instalar.sh
set -euo pipefail

REPO=r12company/atelier
SKILLS=(carrossel-convello carrossel-r12)
[ $# -gt 0 ] && SKILLS=("$@")
DESTINO="$HOME/.claude/skills"
PATH_ORIGINAL="$PATH"
diga() { printf '%s\n' "$*"; }

tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

# 1. Baixar o repositório
if [ -n "${ORIGEM:-}" ]; then
  fonte="$ORIGEM"
  diga "Usando a cópia local em $fonte"
elif command -v git >/dev/null 2>&1; then
  diga "Baixando o Atelier (git)..."
  git clone -q --depth 1 "https://github.com/$REPO.git" "$tmp/atelier"
  fonte="$tmp/atelier"
else
  diga "Baixando o Atelier (sem git, pelo arquivo do GitHub)..."
  curl -fsSL "https://github.com/$REPO/archive/refs/heads/main.tar.gz" | tar -xz -C "$tmp"
  fonte=$(find "$tmp" -mindepth 1 -maxdepth 1 -type d | head -1)
fi

# 2. Copiar as skills
mkdir -p "$DESTINO"
for nome in "${SKILLS[@]}"; do
  origem="$fonte/plugins/$nome/skills/$nome"
  if [ ! -f "$origem/SKILL.md" ]; then
    diga "Não existe a skill \"$nome\". As que existem: carrossel-convello, carrossel-r12."
    exit 1
  fi
  if [ -d "$DESTINO/$nome" ]; then
    rm -rf "$DESTINO/$nome.antiga"
    mv "$DESTINO/$nome" "$DESTINO/$nome.antiga"
    diga "Já existia a skill $nome: a versão anterior ficou guardada em $DESTINO/$nome.antiga"
  fi
  cp -R "$origem" "$DESTINO/$nome"
  rm -rf "$DESTINO/$nome/motor/__pycache__"
  diga "Skill $nome instalada em $DESTINO/$nome"
done
skill="$DESTINO/${SKILLS[0]}"

# 3. Fontes (IBM Plex Sans e Oswald, licença OFL)
case "$(uname -s)" in
  Darwin) pasta_fontes="$HOME/Library/Fonts" ;;
  *) pasta_fontes="$HOME/.local/share/fonts/atelier" ;;
esac
if ! (command -v fc-list >/dev/null 2>&1 && fc-list : family | grep -q "IBM Plex Sans" && fc-list : family | grep -q "Oswald"); then
  mkdir -p "$pasta_fontes"
  cp "$skill"/fontes/*.ttf "$pasta_fontes/"
  command -v fc-cache >/dev/null 2>&1 && fc-cache -f "$pasta_fontes" >/dev/null 2>&1 || true
  diga "Fontes IBM Plex Sans e Oswald instaladas em $pasta_fontes"
fi

# 4. PhotoCraft (o programa que o Atelier usa para montar), só no Linux de 64 bits e só se faltar
if ! command -v photocraft-cli >/dev/null 2>&1 && [ ! -x "$HOME/.local/bin/photocraft-cli" ]; then
  if [ "$(uname -s)" = "Linux" ] && [ "$(uname -m)" = "x86_64" ]; then
    diga "Instalando o PhotoCraft (uns 140 MB)..."
    pacote="$tmp/photocraft.tar.gz"
    if [ -n "${PHOTOCRAFT_TAR:-}" ]; then
      cp "$PHOTOCRAFT_TAR" "$pacote"
    elif ! curl -fsSL -o "$pacote" "https://github.com/$REPO/releases/latest/download/photocraft-linux-x86_64.tar.gz"; then
      versao=$(curl -fsSL https://api.github.com/repos/storytold/photocraft/releases/latest | sed -n 's/.*"tag_name": *"v\{0,1\}\([^"]*\)".*/\1/p' | head -1)
      curl -fsSL -o "$pacote" "https://github.com/storytold/photocraft/releases/download/v$versao/photocraft-$versao-linux-x86_64.tar.gz"
    fi
    mkdir -p "$HOME/.local/opt/photocraft" "$HOME/.local/bin"
    tar -xzf "$pacote" -C "$HOME/.local/opt/photocraft"
    bin=$(find "$HOME/.local/opt/photocraft" -path '*/bin/photocraft-cli' -type f | sort | tail -1)
    ln -sf "$bin" "$HOME/.local/bin/photocraft-cli"
    diga "PhotoCraft instalado: $HOME/.local/bin/photocraft-cli"
  else
    diga "PhotoCraft: baixe em https://github.com/storytold/photocraft/releases"
    diga "  Mac: o arquivo photocraft-cli-...-macos-universal.zip; descompacte e ponha o photocraft-cli numa pasta do PATH (por exemplo ~/.local/bin)."
    diga "  Sem ele, as skills fazem roteiro, legenda e pedidos de imagem, e a montagem vai pelo caminho B (Photoshop ou Figma)."
  fi
fi
export PATH="$HOME/.local/bin:$PATH"
# Outro photocraft-cli (instalado à parte) também serve: só avisa qual vai ser usado.
usado=$(command -v photocraft-cli 2>/dev/null || true)
if [ -n "$usado" ] && [ "$usado" != "$HOME/.local/bin/photocraft-cli" ]; then
  diga "PhotoCraft: usando o que já estava instalado, $usado (não é o que o Atelier instala; tudo bem)."
fi

# 5. Conferir o que falta
diga ""
if command -v python3 >/dev/null 2>&1; then
  python3 "$skill/motor/checar.py" || true
else
  diga "Falta o Python 3 (python.org, ou no Mac: brew install python). Sem ele o Atelier não monta."
fi
case ":$PATH_ORIGINAL:" in
  *":$HOME/.local/bin:"*) ;;
  *)
    diga ""
    diga "Atenção: a pasta $HOME/.local/bin (onde fica o photocraft-cli) não está no PATH deste terminal. Rode:"
    diga ""
    diga '  export PATH="$HOME/.local/bin:$PATH"'
    diga ""
    diga "e cole essa mesma linha no fim do ~/.bashrc (ou do ~/.zshrc, no Mac e em quem usa zsh) para valer nos próximos terminais."
    ;;
esac
diga ""
diga "Pronto. Abra o Claude Code e peça, por exemplo: faz um carrossel do Convello sobre <o tema>."
