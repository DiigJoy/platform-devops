# Logging estructurado (estandar del portafolio)

Este documento define el esquema base de logs para todas las apps.
La implementacion depende del lenguaje, pero el formato y campos deben
ser compatibles.

## Formato
- JSON por linea (stdout).
- Un log por evento.
- Campos consistentes para poder filtrar en dashboards.

## Campos base (minimos)
- `timestamp`: ISO8601 UTC.
- `level`: debug|info|warning|error|critical.
- `service`: nombre del servicio (ej: iot-agri-api).
- `env`: entorno (local, staging, prod).
- `request_id`: ID por request.
- `message`: descripcion corta del evento.

## Campos recomendados (HTTP)
- `http.method`
- `http.path`
- `http.status`
- `latency_ms`
- `client_ip`

## Campos recomendados (errores)
- `error.type`
- `error.msg`
- `error.stack` (si aplica)

## Campos recomendados (tracing)
- `trace_id`
- `span_id`

## Reglas
- No loggear secrets (tokens, passwords).
- Evitar PII directa; usar IDs anonimizados.
- Logs deben ser suficientes para debug y SRE basico.

## Ejemplo
{"timestamp":"2026-01-29T12:01:22Z","level":"info","service":"iot-agri-api","env":"local","request_id":"7f1c2b","message":"request","http":{"method":"GET","path":"/health","status":200},"latency_ms":12.4}
