import time
import uuid

import structlog
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .settings import settings
from .db import db_healthcheck
from .telemetry import router as telemetry_router
from .telemetry.mqtt import start_mqtt_consumer, stop_mqtt_consumer
from .logging_config import configure_logging

configure_logging(settings.service_name, settings.env, settings.log_level)
logger = structlog.get_logger(__name__)

app = FastAPI(title="Platform API", version=settings.version)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_list(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(telemetry_router)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = request.headers.get("x-request-id", str(uuid.uuid4()))
    start = time.perf_counter()
    structlog.contextvars.bind_contextvars(
        request_id=request_id,
        http_method=request.method,
        http_path=request.url.path,
        client_ip=request.client.host if request.client else None,
    )
    try:
        response = await call_next(request)
        latency_ms = (time.perf_counter() - start) * 1000
        logger.info(
            "request",
            http_status=response.status_code,
            latency_ms=round(latency_ms, 2),
        )
        response.headers["x-request-id"] = request_id
        return response
    except Exception as exc:
        latency_ms = (time.perf_counter() - start) * 1000
        logger.exception(
            "request_error",
            error_type=exc.__class__.__name__,
            error_msg=str(exc),
            latency_ms=round(latency_ms, 2),
        )
        raise
    finally:
        structlog.contextvars.clear_contextvars()

@app.on_event("startup")
def on_startup():
    start_mqtt_consumer()
    logger.info("startup_complete")

@app.on_event("shutdown")
def on_shutdown():
    stop_mqtt_consumer()
    logger.info("shutdown_complete")

@app.get("/health")
def health():
    db_ok = db_healthcheck()
    return {"status": "ok" if db_ok else "degraded", "db": "ok" if db_ok else "down"}

@app.get("/version")
def version():
    return {"service": settings.service_name, "version": settings.version}
