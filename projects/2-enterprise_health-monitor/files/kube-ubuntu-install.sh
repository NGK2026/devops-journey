#!/bin/bash
# install kubernetes on ubuntu

# Force apt to run entirely non-interactively
export DEBIAN_FRONTEND=noninteractive

apt-get update
apt-get install -y -o Dpkg::Options::="--force-confnew" apt-transport-https ca-certificates curl gpg
curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.36/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.36/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
apt-get update
apt-get install -y -o Dpkg::Options::="--force-confnew" kubelet kubeadm kubectl
apt-mark hold kubelet kubeadm kubectl
systemctl enable --now kubelet