from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from .models import TelemetryIn
from ..settings import settings


def write_telemetry(payload: TelemetryIn) -> None:
    if not payload.has_metrics():
        raise ValueError("Telemetry payload requires at least one metric field.")

    with InfluxDBClient(
        url=settings.influxdb_url,
        token=settings.influxdb_token,
        org=settings.influxdb_org,
    ) as client:
        point = Point("telemetry").tag("device_id", payload.device_id)
        if payload.temperature_c is not None:
            point.field("temperature_c", payload.temperature_c)
        if payload.humidity_pct is not None:
            point.field("humidity_pct", payload.humidity_pct)
        if payload.soil_moisture_pct is not None:
            point.field("soil_moisture_pct", payload.soil_moisture_pct)
        if payload.ts is not None:
            point.time(payload.ts)

        write_api = client.write_api(write_options=SYNCHRONOUS)
        write_api.write(bucket=settings.influxdb_bucket, record=point)


def query_last_points(device_id: str, limit: int = 50) -> list[dict]:
    limit = max(1, min(limit, 500))
    flux = f"""
from(bucket: "{settings.influxdb_bucket}")
  |> range(start: -24h)
  |> filter(fn: (r) => r._measurement == "telemetry")
  |> filter(fn: (r) => r.device_id == "{device_id}")
  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
  |> sort(columns: ["_time"], desc: true)
  |> limit(n: {limit})
"""
    with InfluxDBClient(
        url=settings.influxdb_url,
        token=settings.influxdb_token,
        org=settings.influxdb_org,
    ) as client:
        tables = client.query_api().query(flux)
        rows: list[dict] = []
        for table in tables:
            for record in table.records:
                rows.append(
                    {
                        "time": record.get_time(),
                        "device_id": record.values.get("device_id"),
                        "temperature_c": record.values.get("temperature_c"),
                        "humidity_pct": record.values.get("humidity_pct"),
                        "soil_moisture_pct": record.values.get("soil_moisture_pct"),
                    }
                )
        return rows
