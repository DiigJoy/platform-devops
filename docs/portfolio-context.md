# Contexto del portafolio (monorepo)

Este repositorio es un portafolio de 8 apps con el objetivo de demostrar
desarrollo fullstack, automatizacion de procesos, y practicas SRE/DevOps.
La meta es usarlo como evidencia de trabajo real para obtener mejores
ofertas. Cada app aborda un dominio distinto y usa tecnologias y
herramientas diferentes, pero con una base comun de CI/CD,
observabilidad y buenas practicas de ingenieria.

Este material es de estudio, asi que se necesita ayuda para definir cada
aspecto de forma clara y profesional: arquitectura, roadmap, stack final,
pruebas, CI/CD, observabilidad, seguridad y operacion.

## Estado actual
- Piloto activo: `apps/iot-agri` (IoT Agricultura).
  - Web: Next.js (App Router).
  - API: FastAPI.
  - Telemetria: MQTT -> InfluxDB.
  - Dashboards: Grafana.
- Infra local: `infra/local/docker-compose.yml` levanta MQTT, InfluxDB,
  Grafana, Postgres, API y Web.
- CI base: `.github/workflows/ci.yml` con lint/build y checks basicos.
- Release y changelog automatizado: `.github/workflows/iot-agri-release.yml`
  + `scripts/release.sh` + `scripts/cliff.template.toml` con git-cliff.
  - Versionado via Conventional Commits.
  - Tags por componente (`iot-agri-web-vX.Y.Z`, `iot-agri-api-vX.Y.Z`,
    `platform-vX.Y.Z`) y changelog por app.

## Portafolio de apps (8)
1) IoT Agricultura (piloto actual).
2) IoT Animal.
3) Microbiz (SaaS para micro-negocios).
4) Diet (dieta y macros).
5) Finance (finanzas personales).
6) Journal (diario con IA).
7) Store (tienda ecommerce).
8) Travel (turismo + arriendos mensuales).

Cada proyecto debe cubrir un enfoque tecnico distinto (IoT, SaaS, IA,
ecommerce, data/ETL, search, streaming, mobile, etc.), con tecnologias
variadas pero integradas en una misma plataforma.

## Objetivos del portafolio
- Demostrar desarrollo fullstack real: APIs, frontend, data y pipelines.
- Demostrar automatizacion: CI/CD, versionado, changelog, releases.
- Demostrar enfoque SRE: observabilidad, monitoreo, alertas, SLOs,
  resiliencia, seguridad y operacion.
- Mantener convenciones de git y versionado por app.

## Necesito ayuda con:
- Definir estrategia de cada app:
  - Problema, usuarios, scope MVP, features clave.
  - Arquitectura y patrones por dominio.
  - Stack final y decisiones tecnicas.
  - Roadmap y fases de entrega.
- Definir SRE/DevOps por proyecto:
  - CI/CD por app, IaC, despliegue y ambientes.
  - Observabilidad (logs, metrics, tracing) y alertas.
  - SLOs/SLIs basicos y estrategias de resiliencia.
  - Seguridad (secrets, scanning, hardening, backups).
- Alinear todo con el objetivo de portafolio:
  - Demostraciones claras (demos, dashboards, documentacion).
  - Evidencia de buenas practicas (ADR, changelog, tests).

## Guias y convenciones internas
- Convenciones de git y versionado: `docs/CONVENTIONS.md`.
- Diagramas y arquitectura: `docs/diagrams/` y `docs/portfolio-architecture.md`.
- ADRs: `docs/adr/`.

## Expectativa con la IA
Quiero que la IA use este contexto para ayudarme a diseñar cada app de
forma profesional y coherente, proponiendo decisiones tecnicas,
roadmaps, prioridades y tareas concretas. El enfoque debe ser practico,
demostrable, y alineado con automatizacion + SRE.
