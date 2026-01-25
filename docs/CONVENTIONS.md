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
- `feat`, `fix`, `perf`, `docs`, `chore`, `refactor`, `test`, `build`, `ci`, `style`, `revert`

Ejemplos por tipo:
- `feat(iot-agri): add soil moisture trend chart`
- `fix(iot-agri): avoid mqtt reconnect loop`
- `perf(iot-agri): batch telemetry writes`
- `docs(iot-agri): document api auth flow`
- `chore(iot-agri): update dev dependencies`
- `refactor(iot-agri): extract sensor parsing`
- `test(iot-agri): add mqtt retry coverage`
- `build(iot-agri): pin python base image`
- `ci(iot-agri): add path filters for app`
- `style(iot-agri): format lint rules`
- `revert: revert "feat(iot-agri): add irrigation alerts"`

Buenas practicas (si los commits son la documentacion):
- Commits pequenos y coherentes (1 idea o 1 cambio claro por commit).
- El resumen debe explicar el "que" y no el "como" (max ~72 chars).
- Usa `scope` por app o area: `iot-agri`, `infra`, `docs`, `ci`.
- Evita commits "WIP" en `main`. Si necesitas un checkpoint, hazlo en una rama.

Cuando hacer commit:
- Al terminar una unidad completa de trabajo (funcion, endpoint, pantalla, fix).
- Cuando un cambio rompe compatibilidad, separalo y usa `!` o `BREAKING CHANGE`.
- Si el cambio es grande, divide en commits que mantengan el build funcionando.

Tareas largas:
- Trabaja en una rama y haz commits intermedios con mensajes claros.
- Antes de mergear a `main`, reordena/squash si los pasos fueron exploratorios.
- Mantener `main` limpio y con historia que cuente "que se entrego".

## Reglas de versionado automatico (por componente)
Basado en SemVer y Conventional Commits, el tag se calcula asi:
- `BREAKING CHANGE` o `!` en el subject: `X.Y.Z` -> `(X+1).0.0`
- `feat`: `X.Y.Z` -> `X.(Y+1).0`
- `fix` o `perf`: `X.Y.Z` -> `X.Y.(Z+1)`
- Otros tipos (ej: `docs`, `chore`, `refactor`) no generan nueva version.

Ejemplo: si el ultimo tag es `iot-agri-v0.4.2` y hay un breaking change, el siguiente sera `iot-agri-v1.0.0`.

## Tipos que cambian version (con ejemplos)
- Major: `feat(iot-agri)!: remove legacy mqtt endpoint`
- Minor: `feat(iot-agri): add irrigation alerts`
- Patch: `fix(iot-agri): handle null sensor id`
- Patch: `perf(iot-agri): batch writes to influx`

## Tags por componente
- Frontend: `iot-agri-web-vX.Y.Z`
- Backend: `iot-agri-api-vX.Y.Z`
- Platform/DevOps: `platform-vX.Y.Z`

## Changelog
- Frontend: `apps/iot-agri/web/CHANGELOG.md`
- Backend: `apps/iot-agri/api/CHANGELOG.md`
- Platform/DevOps: `CHANGELOG.md`
- Basado en Conventional Commits y tags por componente.

## Changelog automatico (git-cliff)
El CI usa un template comun y lo parametriza por componente.

Template:
- `scripts/cliff.template.toml`

Ejemplo manual (frontend iot-agri):
```
sed \
  -e "s|{{TAG_PATTERN}}|iot-agri-web-v[0-9].*|g" \
  -e "s|{{INCLUDE_PATHS}}|\"apps/iot-agri/web/**\"|g" \
  scripts/cliff.template.toml > /tmp/cliff.toml
git-cliff -c /tmp/cliff.toml -o apps/iot-agri/web/CHANGELOG.md
```

## Flujo automatico de changelog y tags (CI)
- En cada merge a `main`, el workflow crea tags por componente segun Conventional Commits.
- Se regenera el changelog de cada componente afectado y se commitea automaticamente.
- El desarrollador solo debe escribir commits bien formateados y enfocados.

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
