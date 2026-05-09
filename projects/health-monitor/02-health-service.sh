!#/bin/bash

# variables
IS_RUNNING="docker ps --filter name=romantic_lovelace --format "{{.Names}}""
# arrays
NAMES=("health-monitor" "prometheus" "grafana")
CHECK=()
RUN=()

# TODO: check if container is running by filter
for NAME in ${NAMES[@]}; do
    COMMAND='docker ps --filter name=$NAME --format "{{.Names}}"'
    if [ ! "$COMMAND" = "$NAME"]; then
        CHECK+=("$NAME")
    fi

# TODO: if not running check if exists but stopped or
# not exist at all
# TODO: if exists: start
for NAME in ${CHECK[@]}; do
    COMMAND='docker ps -a --filter name=$NAME --format "{{.Names}}"'
    if [ "$COMMAND" = "$NAME"]; then
        docker start $NAME
    else
        RUN+=($"NAME")
    fi

# TODO: if not exist: run
for NAME in ${RUN[@]}; do
    if [ "$NAME" = "health-monitor" ]; then
        docker run -d --name health-monitor --network monitor-net -p 5000:5000 ngk2026/health-monitor:latest
    fi
    if [ "$NAME" = "prometheus" ]; then
        docker run -d \
            --name prometheus \
            --network monitor-net \
            -p 9090:9090 \
            -v /home/ec2-user/devops-journey/projects/health-monitor/prometheus.yml:/etc/prometheus/prometheus.yml \
            prom/prometheus
    fi
    if [ "$NAME" = "grafana" ]; then
        docker run -d \
            --name grafana \
            --network monitor-net \
            -p 3000:3000 \
            grafana/grafana
    fi