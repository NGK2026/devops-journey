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

# test ssh
╰─❯ ssh 192.168.0.124
student@ubuntu2204:~$ cat .ssh/authorized_keys 
# ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIM0r8bfS9QwfphWKX8BSzPDaAWlLapnnYrde4wLfRc2D VMs

╰─❯ ssh 192.168.0.3
student@ubuntu2604:~$ cat .ssh/authorized_keys 
# ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIM0r8bfS9QwfphWKX8BSzPDaAWlLapnnYrde4wLfRc2D VMs
```
#### 5. create ansible key and transfer to vms
```sh
╰─❯ ssh-keygen -t ed25519 -C "ansible"
Enter file in which to save the key (/home/student/.ssh/id_ed25519): /home/student/.ssh/ansible
# no passphrase

╰─❯ ssh-copy-id -i ~/.ssh/ansible.pub 192.168.0.124  
╰─❯ ssh-copy-id -i ~/.ssh/ansible.pub 192.168.0.139
╰─❯ ssh-copy-id -i ~/.ssh/ansible.pub 192.168.0.3  
╰─❯ ssh-copy-id -i ~/.ssh/ansible.pub 192.168.0.66  

# check VM
student@ubuntu2204:~$ cat .ssh/authorized_keys 
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIM0r8bfS9QwfphWKX8BSzPDaAWlLapnnYrde4wLfRc2D VMs
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINZV/VjSdJNEj5jcdZFz+fq6Nmticv2of6SgNNxlr+Xx ansible
```
#### 6. ssh with specific key
```sh
# -i (input file)
╰─❯ ssh -i ~/.ssh/ansible 192.168.0.3
student@ubuntu2604:~$
```
#### 7. enable ssh-agent for less passphrase prompting
```sh
# eval (ties env variables to the following command)
╰─❯ eval $(ssh-agent)
# Agent pid 35824

# specify whick key if not default
╰─❯ ssh-add ~/.ssh/VMs        
Enter passphrase for /home/student/.ssh/VMs: 
# Identity added: /home/student/.ssh/VMs (VMs)
```
- or use alias (add in ~/.bashrc)
```sh
╰─❯ alias ssha='eval $(ssh-agent) && ssh-add ~/.ssh/VMs'

╰─❯ ssha
# Agent pid 35824
Enter passphrase for /home/student/.ssh/VMs: 
# Identity added: /home/student/.ssh/VMs (VMs)
```