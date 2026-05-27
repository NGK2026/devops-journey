# Helm Kubernetes Package Management

Hands-on Kubernetes application orchestration using Helm. Covers remote repository integration, chart parameter injection overrides, persistent value file abstractions, Service mutations (`ClusterIP` to `NodePort`), declarative local manifest compilation via template engines, and direct `kubectl` engine enforcement layers.

## Contents
- [setup.md](./setup.md) — multi-component deployment labs tracking manual overrides, state conflicts, value templates, and local engine unpack configurations
- [commands.md](./commands.md) — operational CLI references detailing active application releases, upstream index synchronizations, and discovery lookups

## Manifests & Configurations
| File | Description |
|---|---|
| `values.yaml` | Active configuration parameter overrides mapping user administrative permissions and customized networking rules onto complex nested deployment charts |
| `values copy.yaml` | Baseline duplicate backup template of specific runtime configuration trees used during variable drift comparison cycles |