# Kubernetes

Hands-on Kubernetes using Minikube. Covers deployments, services, secrets, configmaps, namespaces, and ingress.

## Contents
- [setup.md](./setup.md) — full setup walkthrough with troubleshooting
- [commands.md](./commands.md) — kubectl command reference

## Manifests
| File | Description |
|---|---|
| `nginx-deployment.yaml` | Basic nginx deployment and service |
| `mongo.yaml` | MongoDB deployment and internal service |
| `mongo-express.yaml` | Mongo Express deployment and external LoadBalancer service |
| `mongo-secret.yaml` | Base64-encoded credentials secret |
| `mongo-configmap.yaml` | ConfigMap for MongoDB connection URL |
| `dashboard-ingress.yaml` | Ingress rule routing dashboard.com to Kubernetes dashboard |