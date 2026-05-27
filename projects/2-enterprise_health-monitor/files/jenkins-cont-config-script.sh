#!/bin/bash

# configure jenkins container
# run inside container

# N O T I C E ! ! ! !
# get GID of docker on host and replace here BEFORE running script
# getent group docker | cut -d: -f3

curl https://get.docker.com | sh
usermod -aG docker jenkins
groupmod -g 947 docker # <----- REPLACE ME!!
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
mv kubectl /usr/local/bin/
mkdir -p /var/jenkins_home/.kube
chown -R jenkins:jenkins /var/jenkins_home/.kube