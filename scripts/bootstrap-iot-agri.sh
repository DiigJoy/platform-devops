#!/usr/bin/env bash
set -euo pipefail

SKIP_NODE="${SKIP_NODE:-0}"

echo "==> Creando venv en .venv"
python -m venv .venv

echo "==> Activando venv"
source .venv/bin/activate

echo "==> Instalando uv"
pip install uv

echo "==> Instalando deps API"
uv pip install -r apps/iot-agri/api/requirements.txt

echo "==> Instalando deps scripts"
uv pip install -r apps/iot-agri/requirements-dev.txt

if [ "$SKIP_NODE" -eq 0 ]; then
  echo "==> Instalando deps web"
  (cd apps/iot-agri/web && npm install)
fi

echo "==> Bootstrap OK"
