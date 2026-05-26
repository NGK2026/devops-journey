#!/bin/bash

# load flannel 
modprobe br_netfilter # sudo
echo "br_netfilter" | sudo tee /etc/modules-load.d/br_netfilter.conf
sysctl -w net.bridge.bridge-nf-call-iptables=1 # sudo
echo "net.bridge.bridge-nf-call-iptables=1" | sudo tee /etc/sysctl.d/99-kubernetes.conf
sysctl --system # sudo

# kubectl rollout restart daemonset kube-flannel-ds -n kube-flannel
# kubectl get pods -n kube-flannel -o wide