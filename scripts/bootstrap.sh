#!/usr/bin/env bash
set -euo pipefail

echo "==> Creando venv en .venv"
python -m venv .venv

echo "==> Activando venv"
source .venv/bin/activate

echo "==> Instalando uv"
pip install uv

echo "==> Instalando pre-commit"
uv pip install pre-commit
pre-commit install

echo "==> Bootstrap global OK"
echo "==> Siguiente: ./scripts/bootstrap-iot-agri.sh"
