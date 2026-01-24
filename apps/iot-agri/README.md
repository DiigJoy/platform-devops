# IoT Agricultura (App)

## Objetivo
Piloto IoT con ingesta MQTT, persistencia en InfluxDB y dashboards en Grafana.

## Componentes
- API: FastAPI (`apps/iot-agri/api`)
- Web: Next.js (`apps/iot-agri/web`)
- Scripts: simulador de sensores (`apps/iot-agri/scripts`)

## Run local (root)
```bash
docker compose -f infra/local/docker-compose.yml up --build
```

## Simular telemetria
```bash
python apps/iot-agri/scripts/simulate_sensor.py
```

## Bootstrap local (Windows)
```powershell
scripts\bootstrap.ps1
scripts\bootstrap-iot-agri.ps1
```

## Bootstrap local (Linux/Mac)
```bash
./scripts/bootstrap.sh
./scripts/bootstrap-iot-agri.sh
```

## Notas
- Usamos `uv` para instalar dependencias mas rapido.

## Changelog
- `apps/iot-agri/CHANGELOG.md`
- Tags: `iot-agri-vX.Y.Z`

## Convenciones de git
- Ver `docs/CONVENTIONS.md`

## Endpoints
- `GET /health`
- `POST /iot/ingest`
- `GET /iot/last?device_id=sensor-001&limit=10`

## UI
- `GET /` overview
- `GET /iot` dashboard IoT
