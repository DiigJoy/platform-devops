from fastapi import APIRouter, HTTPException, Query

from .influx import query_last_points, write_telemetry
from .models import TelemetryIn

router = APIRouter(prefix="/iot", tags=["iot"])


@router.post("/ingest")
def ingest(payload: TelemetryIn):
    try:
        write_telemetry(payload)
        return {"status": "ok"}
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))
    except Exception as exc:
        raise HTTPException(status_code=500, detail="ingest_failed") from exc


@router.get("/last")
def last_points(
    device_id: str = Query(..., min_length=1),
    limit: int = Query(50, ge=1, le=500),
):
    try:
        return {"items": query_last_points(device_id=device_id, limit=limit)}
    except Exception as exc:
        raise HTTPException(status_code=500, detail="query_failed") from exc
