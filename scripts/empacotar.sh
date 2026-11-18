#!/usr/bin/env bash
# Gera em dist/ um .zip por skill, para enviar no Claude.ai (Configurações > Capacidades > Skills).
#   bash scripts/empacotar.sh                 só os zips das skills
#   bash scripts/empacotar.sh --photocraft    também baixa o PhotoCraft oficial para Linux e grava
#                                             dist/photocraft-linux-x86_64.tar.gz (para anexar no Release do GitHub)
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p dist
for dir in plugins/*/skills/*/; do
  nome=$(basename "$dir")
  rm -f "dist/$nome.zip"
  python3 - "$dir" "dist/$nome.zip" <<'PY'
import os, sys, zipfile
base, saida = os.path.normpath(sys.argv[1]), sys.argv[2]
with zipfile.ZipFile(saida, 'w', zipfile.ZIP_DEFLATED) as z:
    for raiz, pastas, arquivos in os.walk(base):
        pastas[:] = sorted(p for p in pastas if p != '__pycache__')
        for a in sorted(arquivos):
            if not a.endswith('.pyc') and a != '.DS_Store':
                caminho = os.path.join(raiz, a)
                z.write(caminho, os.path.relpath(caminho, os.path.dirname(base)))
PY
  echo "dist/$nome.zip"
done
if [ "${1:-}" = "--photocraft" ]; then
  # PhotoCraft: https://github.com/storytold/photocraft (MIT ou Apache-2.0). O pacote oficial já traz as licenças em share/doc.
  versao=$(curl -fsSL https://api.github.com/repos/storytold/photocraft/releases/latest | python3 -c 'import json,sys; print(json.load(sys.stdin)["tag_name"].lstrip("v"))')
  curl -fL --progress-bar -o dist/photocraft-linux-x86_64.tar.gz \
    "https://github.com/storytold/photocraft/releases/download/v$versao/photocraft-$versao-linux-x86_64.tar.gz"
  echo "dist/photocraft-linux-x86_64.tar.gz (PhotoCraft $versao)"
fi
