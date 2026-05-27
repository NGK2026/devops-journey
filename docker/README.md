# Docker & Container Orchestration Laboratory

Hands-on containerization workflows using Docker and Docker Compose. Covers image management, running detached interactive networks, volume data persistence mapping, multi-container development stacks, and pushing image variants to AWS Elastic Container Registry (ECR).

## Contents
- [commands.md](./commands.md) — complete Docker CLI command cheat sheet and system configuration tracking log

## Projects
| Directory | Description |
|---|---|
| `my-project` | Flask-based Python application isolated using a lightweight runtime base image and orchestrating single-service environments |
| `tutorial-project` | Multi-container application stack grouping a Node.js server frontend with persistent MongoDB and Mongo Express dashboard backends |

## Manifests & Configurations
| File | Description |
|---|---|
| `my-project/Dockerfile` | Builds a minimalist Python automation layer; sets context paths, dependency requirements, and default entry point routines |
| `my-project/docker-compose.yml` | Declarative definitions mapping local application volumes to host resources for quick code prototyping loops |
| `tutorial-project/Dockerfile` | Bundles a Node.js backend environment by exposing server entry points, locking package dependency baselines, and handling static image assets |
| `tutorial-project/docker-compose.yml` | Production-ready multi-tier blueprint staging network bonds, environment configurations, credential parameters, and local data persistence definitions across isolated image clusters |
| `tutorial-project/mongo.yaml` | Decoupled orchestration configuration tracking data components and internal service routing rules for MongoDB workloads |