## Health Monitor App
. Monitor's the system's CPU, Memory & Disk usage % using a Python app.
. The App is located inside a Docker container, deploying a Python Flask server.

### Step 1 — The App -- Done
1. Create /projects/health-monitor/app/app.py
2. Use psutil to collect CPU, memory, disk usage
3. Use Flask to expose it at http://localhost:5000/metrics
4. Test it runs locally on your Arch machine


### Step 2 — Containerize -- Done
5. Write Dockerfile for the app
6. Write docker-compose.yml to run it locally
7. Test it runs in Docker

### Step 3 — Infrastructure -- Done
8. Write Terraform to provision AWS EC2 instance and security groups
9. Apply it, verify instance is running

### Step 4 — CI/CD  -- Done
10. Write GitHub Actions pipeline — on push, build Docker image, push to Docker Hub

### Step 5 — Monitoring -- Done
13. Add Prometheus scrape config to target your app
14. Open Grafana, build one simple dashboard showing CPU and memory

### Step 6 — Bash -- Done
15. Write a bash script that checks if the app is running and restarts it if not

#### How to use
1. Pull the files and app folder
2. Run 
```sh
╰─❯ docker-compose up

╰─❯ curl http://localhost:5000/metrics
{"CPU":1.0,"Home":45.4,"RAM":18.8,"Root":45.4}
```

