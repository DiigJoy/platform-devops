# Checklist SRE minimo (por app)

Este checklist es el minimo para considerar una app "demoable" y operable.
Sirve como Definition of Done SRE para cada proyecto del portafolio.

## 1) Observabilidad basica
- Logs estructurados (JSON) con nivel y contexto.
- Health check (`/health`) con dependencias criticas.
- Metrics minimas (latencia, errores, throughput).
- Dashboard basico (Grafana o similar) con 3-5 paneles.

## 2) Confiabilidad y resiliencia
- Timeouts y retries definidos para llamadas externas.
- Backoff y manejo de errores en integraciones.
- Validaciones de entrada en API.
- Circuit breaker o limite de fallos en puntos criticos (si aplica).

## 3) Seguridad minima
- Configuracion por variables de entorno (sin secrets en repo).
- CORS y headers basicos (API + web).
- Dependencias con versiones fijas y escaneo basico (Snyk/Trivy/Dependabot).
- Politica simple de backups (si hay data persistente).

## 4) CI/CD y calidad
- Lint + tests basicos en CI.
- Build reproducible (Dockerfile o build script).
- Changelog automatico y versionado por tags.
- Release notes o PR automatica (si aplica).

## 5) Operacion local y documentacion
- `README` con pasos de ejecucion local.
- `docker-compose` o script de bootstrap.
- Diagrama simple (C4 o flujo principal).
- ADRs para decisiones clave.

## 6) SLOs minimos (definicion inicial)
- Latencia p95 endpoint principal.
- Error rate (% 5xx).
- Disponibilidad esperada (ej: 99% para demo).

## 7) Pruebas minimas
- Pruebas unitarias para logica critica.
- Prueba de integracion basica (API -> DB o cola).
- Smoke test post-deploy (script o endpoint).
