# ADR-0002: IoT Pilot Ingestion (MQTT + InfluxDB)

## Status
Accepted

## Context
Necesitamos un piloto IoT (agricultura) que demuestre ingesta en tiempo real, persistencia time-series, alertas y dashboards. El objetivo es un vertical slice rapido de mostrar en entrevistas y que luego pueda escalarse a un stack completo.

## Decision
- Usar MQTT como canal principal de ingesta desde sensores.
- Persistir telemetria en InfluxDB.
- Exponer una API FastAPI para:
  - Ingesta de respaldo via REST.
  - Consultas agregadas para el dashboard.
- Visualizar con Grafana.

## Rationale
- MQTT es el estandar practico para IoT, facil de simular localmente.
- InfluxDB es optimo para time-series y write-heavy, ideal para telemetria.
- FastAPI permite iterar rapido y mantener el stack base del repo.
- Grafana acelera la demo de dashboards sin construir todo desde cero.

## Consequences
- La telemetria vive en InfluxDB, mientras el dominio core seguira en PostgreSQL.
- Si se requieren joins complejos con datos transaccionales, se agregara un proceso de sync o se evaluara TimescaleDB.
- Se mantiene un endpoint REST para testing sin MQTT.

## Alternatives considered
- TimescaleDB: mejor para SQL y joins, pero menos directo para un piloto de IoT puro.
- No usar MQTT: mas simple, pero pierde realismo IoT y limita demostracion.
