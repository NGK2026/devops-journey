# GitHub Actions CI/CD Pipeline Automation

Hands-on continuous integration and continuous deployment workflows using GitHub Actions. Covers build automation, secure secret management, build-time caching optimization, Docker Hub registry routing, and multi-architecture image compilation.

## Contents
- [setup.md](./setup.md) — step-by-step external provider authentication, secret mappings, and workflow compilation guides
- [commands.md](./commands.md) — baseline workflow operational logic and deployment tracking logs

## Pipeline Architecture & Workflows
| File / Directory | Description |
|---|---|
| `.github/workflows/pipeline.yml` | Primary automation blueprint containing triggers, build jobs, testing contexts, and Docker image publication states |