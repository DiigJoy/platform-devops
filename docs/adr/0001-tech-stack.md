# ADR-0001: Baseline Tech Stack

## Decision
Use:
- Next.js (TypeScript) for web
- FastAPI for API
- PostgreSQL for persistence
- Docker Compose for local dev
- GitHub Actions for CI

## Rationale
Ship fast, keep it cloud-native-ready, and optimize for portfolio visibility.

## Consequences
We can later swap CI engines (GitLab CI), move to GitOps (ArgoCD), and split modules into services when justified.
