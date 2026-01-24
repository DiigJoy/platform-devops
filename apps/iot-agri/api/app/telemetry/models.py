from datetime import datetime
from pydantic import BaseModel, Field


class TelemetryIn(BaseModel):
    device_id: str = Field(..., min_length=1, max_length=128)
    temperature_c: float | None = None
    humidity_pct: float | None = None
    soil_moisture_pct: float | None = None
    ts: datetime | None = None

    def has_metrics(self) -> bool:
        return any(
            value is not None
            for value in (self.temperature_c, self.humidity_pct, self.soil_moisture_pct)
        )
