#!/usr/bin/env bash
set -euo pipefail

echo "Lint API (FastAPI)"
cd apps/iot-agri/api
python -m pip install uv > /dev/null
uv pip install -r requirements.txt > /dev/null
uv pip install ruff > /dev/null
ruff check app

echo "Lint Web (Next.js)"
cd ../web
npm install
npm run lint
