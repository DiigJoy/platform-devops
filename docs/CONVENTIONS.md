# Convenciones de Git y Versionado

## Branching
- `main` siempre estable y desplegable.
- Ramas cortas por cambio: `feat/`, `fix/`, `chore/`, `docs/`.
- Nombres: `feat/iot-agri-telemetry`, `fix/mqtt-callback`.

## Conventional Commits
Formato:
```
<type>(<scope>): <summary>
```
Ejemplos:
- `feat(iot-agri): add telemetry ingest endpoint`
- `fix(iot-agri): handle mqtt v2 callback`
- `chore(ci): add path filters`

Tipos recomendados:
- `feat`, `fix`, `docs`, `chore`, `refactor`, `test`

## Tags por app
Para releases de `iot-agri`:
- `iot-agri-vX.Y.Z`

## Changelog
- Mantener en `apps/iot-agri/CHANGELOG.md`.
- Basado en Conventional Commits y tags `iot-agri-vX.Y.Z`.

## Changelog automatico (git-cliff)
Instalacion:
```
cargo install git-cliff
```
Generar/actualizar changelog de iot-agri (solo paths de la app):
```
git cliff --config apps/iot-agri/cliff.toml --output apps/iot-agri/CHANGELOG.md
```
Release:
```
git tag iot-agri-v0.1.0
git cliff --config apps/iot-agri/cliff.toml --output apps/iot-agri/CHANGELOG.md
```

## Pre-commit
Instalacion:
```
pip install pre-commit
pre-commit install
```
Ejecucion manual:
```
pre-commit run --all-files
```
