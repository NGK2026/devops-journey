# Project 1 — System Health Monitor

Flask app that collects CPU, memory, and disk metrics and exposes them at `/metrics` in Prometheus format. Fully automated deployment to AWS.

## Stack
- **App:** Python, Flask, psutil, prometheus-client
- **Container:** Docker
- **Infrastructure:** Terraform (AWS EC2, VPC, Security Groups)
- **CI/CD:** GitHub Actions — builds and pushes Docker image on every push, SSHs into EC2 and redeploys
- **Monitoring:** Prometheus scrapes `/metrics`, Grafana displays dashboard
- **Health Check:** Bash script runs via cron, restarts any stopped containers

## Structure
├── app/app.py # Flask app — collects and exposes metrics 
├── Dockerfile # Container definition 
├── docker-compose.yml # Local development 
├── main.tf # Terraform — provisions EC2, VPC, security groups 
├── health-monitor.yml # GitHub Actions pipeline 
├── prometheus.yml # Prometheus scrape config 
├── 02-health-service.sh # Bash health check and restart script 
└── 01-psutil.py # psutil exploration (development notes)


## How to Run Locally
```bash
docker-compose up
curl http://localhost:5000/metrics
```