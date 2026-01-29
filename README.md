# Fullstack + DevOps Platform (Monorepo)

Estrategia del portafolio:
- **Backends**: Python (FastAPI como base, algo de Django).
- **Frontends**: React (Next.js para web y React Native en apps mobile).

Baseline stack (piloto IoT):
- **Web**: React (Next.js, App Router)
- **API**: FastAPI (Python)
- **DB**: PostgreSQL (core) + InfluxDB (telemetria)
- **Local**: Docker Compose
- **CI**: GitHub Actions (lint/test/build)
 - **IoT**: MQTT (Mosquitto)
 - **Dashboards**: Grafana

## Quick start (local)
### 1) Requirements
- Docker Desktop
- Node 18+
- Python 3.11+


### 2) Run everything (dev)
```bash
docker compose -f infra/local/docker-compose.yml up --build
```
- Web: http://localhost:3000
- API: http://localhost:8000/health
- DB (Postgres):  localhost:5433
- InfluxDB: http://localhost:8086
- Grafana: http://localhost:3001

### 3) Dev without Docker (optional)
```bash
# API
cd apps/iot-agri/api
python -m venv .venv
# mac/linux: source .venv/bin/activate
# windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# WEB (new terminal)
cd apps/iot-agri/web
npm install
npm run dev
```

## Docs
Ver `docs/README.md` para indices y arquitectura.

## Repo layout
```
apps/
  iot-agri/
    web/     Next.js
    api/     FastAPI
  iot-animal/
  microbiz/
  diet/
  finance/
  journal/
  store/
  travel/
packages/
  ui/
  schemas/
  config/
infra/
  local/docker-compose.yml
  terraform/
  k8s/
.github/workflows/
  ci.yml
docs/
  adr/
  diagrams/
  README.md
```
