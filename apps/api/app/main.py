from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .settings import settings
from .db import db_healthcheck

app = FastAPI(title="Platform API", version=settings.version)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_list(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    db_ok = db_healthcheck()
    return {"status": "ok" if db_ok else "degraded", "db": "ok" if db_ok else "down"}

@app.get("/version")
def version():
    return {"service": settings.service_name, "version": settings.version}
