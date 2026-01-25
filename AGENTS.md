# AGENTS.md

Purpose: help coding agents work in this monorepo with minimal context.

## Repo overview
- Monorepo with multiple apps under `apps/` and shared packages under `packages/`.
- Primary app today: `apps/iot-agri` (Next.js web + FastAPI API).
- CI/CD uses GitHub Actions in `.github/workflows/`.

## Release + changelog flow (iot-agri)
- Workflow: `.github/workflows/iot-agri-release.yml` runs on pushes to `main`
  when files under `apps/iot-agri/**` or the workflow/script change.
- Tagging: `scripts/iot-agri-release.sh` inspects Conventional Commits that
  touched `apps/iot-agri` since the latest `iot-agri-vX.Y.Z` tag.
  - BREAKING CHANGE / `!` in subject -> major
  - `feat` -> minor
  - `fix`/`perf` -> patch
  - No matching commits -> no tag
- Changelog: `apps/iot-agri/cliff.toml` configures `git-cliff` to generate
  `apps/iot-agri/CHANGELOG.md` from Conventional Commits and per-app tags.
- PR requirement: changelog updates are committed via
  `peter-evans/create-pull-request` using `REPO_BOT_TOKEN`.

## Conventions
- Use Conventional Commits for all app changes.
- Tags are per-app: `iot-agri-vX.Y.Z`.
- Keep changelog content app-scoped; do not mix other apps' commits.

## Adding release automation for a new app
- Duplicate the iot-agri workflow and script, adjust:
  - paths filter
  - tag prefix
  - app path
  - changelog output path
  - cliff config path
- Add a per-app `cliff.toml` with `include_path` scoped to the app.
