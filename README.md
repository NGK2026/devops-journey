# DevOps Engineering Portfolio

Infrastructure automation and systems engineering — Linux, cloud, containers, CI/CD, monitoring.

---

## Projects

### [Project 2 — Enterprise Health Monitor](./projects/2-enterprise_health-monitor/)
Multi-node production-grade deployment of a Flask metrics app across a 4-node kubeadm Kubernetes cluster.
- Ansible provisions and configures all VMs
- Jenkins CI/CD pipeline builds, pushes to DockerHub, deploys via Helm
- Prometheus scrapes `/metrics` via ServiceMonitor, Grafana dashboards CPU, memory, disk
- **Stack:** Python, Docker, Kubernetes, Helm, Jenkins, Ansible, Prometheus, Grafana

### [Project 1 — System Health Monitor](./projects/1-health-monitor/)
End-to-end automated deployment of a Flask metrics app on AWS.
- GitHub Actions builds and pushes Docker image on every push
- Terraform provisions EC2, Prometheus scrapes `/metrics`, Grafana displays dashboard
- Bash script monitors app health and restarts if down
- **Stack:** Python, Docker, Terraform, AWS EC2, GitHub Actions, Prometheus, Grafana

---

## Skills

| Area | Tools |
|---|---|
| Cloud & IaC | AWS (EC2, S3, IAM), Terraform |
| Containers & Orchestration | Docker, Kubernetes, Helm |
| CI/CD | GitHub Actions, Jenkins |
| Configuration Management | Ansible |
| Monitoring | Prometheus, Grafana |
| Scripting | Python, Bash |
| OS | Linux (Arch, Ubuntu, CentOS) |
| Version Control | Git |

---

## Roadmap

| # | Topic | Folder |
|---|---|---|
| 1 | Python | [python](./python/) |
| 2 | Git | [git](./git/) |
| 3 | Bash | [bash](./bash/) |
| 4 | Cloud Concepts | [aws](./aws/) |
| 5 | AWS Hands On | [aws](./aws/) |
| 6 | Terraform | [terraform](./terraform/) |
| 7 | Docker | [docker](./docker/) |
| 8 | Kubernetes | [kubernetes](./kubernetes/) |
| 9 | CI/CD — GitHub Actions | [cicd](./cicd/) |
| 10 | Prometheus + Grafana | [prometheus](./prometheus/) |
| 11 | Ansible | [ansible](./ansible/) |
| 12 | Helm | [helm](./helm/) |
| 13 | Jenkins | [jenkins](./jenkins/) |