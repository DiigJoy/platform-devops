# Fullstack + DevOps Platform (Sprint 0 Foundation)

Baseline stack:
- **Web**: Next.js (TypeScript, App Router)
- **API**: FastAPI (Python)
- **DB**: PostgreSQL
- **Local**: Docker Compose
- **CI**: GitHub Actions (lint/test/build)

## Quick start (local)
### 1) Requirements
- Docker Desktop
- Node 18+
- Python 3.11+

### 2) Run everything (dev)
```bash
docker compose up --build
```
- Web: http://localhost:3000
- API: http://localhost:8000/health
- DB:  localhost:5432

### 3) Dev without Docker (optional)
```bash
# API
cd apps/api
python -m venv .venv
# mac/linux: source .venv/bin/activate
# windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000

# WEB (new terminal)
cd apps/web
npm install
npm run dev
```

## Repo layout
```
apps/
  web/     Next.js
  api/     FastAPI
infra/
  docker-compose.yml
.github/workflows/
  ci.yml
docs/adr/
```
