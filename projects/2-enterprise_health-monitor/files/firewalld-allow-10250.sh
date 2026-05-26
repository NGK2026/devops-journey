#!/bin/bash

# firewalld allow 10250

sudo firewall-cmd --permanent --add-port=10250/tcp --add-port=10251/tcp --add-port=10252/tcp --add-port=10255/tcp
sudo firewall-cmd --reload