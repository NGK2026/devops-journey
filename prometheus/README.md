# Prometheus & Grafana Monitoring Stack

Hands-on deployment of an enterprise monitoring engine using Docker Compose. Covers time-series database scraping architectures, node-level hardware metrics extraction via host-network bindings, persistent runtime storage virtualization volumes, and granular container resources monitoring.

## Manifests & Configurations
| File | Description |
|---|---|
| `docker-compose.yml` | Declarative service blueprint managing internal routing, volume scopes, and kernel-level resource mappings |
| `prometheus.yml` | Time-series control file defining data aggregation cadences and targeted endpoint discovery endpoints |