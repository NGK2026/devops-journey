#### 1. install 4 VMs, bridged network
- 2 Ubuntu 26.04 servers
- 2 Ubuntu 22.04 servers
#### 2. install ssh on servers
```sh
sudo apt update
sudo apt install openssh-server

# enable system process
sudo systemctl enable --now ssh

# verify
systemctl status ssh
```
#### 3. create ssh keys
```sh
ssh-keygen -t ed22519 -C "VMs"
# save as /home/student/.ssh/VMs
# create passphrase
```
#### 4. migrate public keys to servers
```sh
╰─❯ ssh-copy-id -i ~/.ssh/VMs.pub 192.168.0.124
# Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
# student@192.168.0.124's password: 
# Number of key(s) added: 1

╰─❯ ssh-copy-id -i ~/.ssh/VMs.pub 192.168.0.139  
╰─❯ ssh-copy-id -i ~/.ssh/VMs.pub 192.168.0.3
╰─❯ ssh-copy-id -i ~/.ssh/VMs.pub 192.168.0.66
```