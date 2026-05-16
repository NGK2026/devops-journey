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
- or use alias (add in ~/.bashrc, or .zshrc in my case)
```sh
╰─❯ alias ssha='eval $(ssh-agent) && ssh-add ~/.ssh/VMs'

╰─❯ ssha
# Agent pid 35824
Enter passphrase for /home/student/.ssh/VMs: 
# Identity added: /home/student/.ssh/VMs (VMs)
```
#### 8. create inventory file (list of ips to work on)
```txt
192.168.0.124
192.168.0.139
192.168.0.3
192.168.0.66
```
#### 9. ping hosts
```sh
# -m (module)
╰─❯ ansible all --key-file ~/.ssh/ansible -i inventory -m ping

# [WARNING]: Host '192.168.0.139' is using the discovered Python interpreter at '/usr/bin/python3.10', but future installation of another Pyth
# on interpreter could cause a different interpreter to be discovered. See https://docs.ansible.com/ansible-core/2.20/reference_appendices/int
# erpreter_discovery.html for more information.
192.168.0.139 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3.10"
    },
    "changed": false,
    "ping": "pong"
}
```
#### 10. create ansible config
- default is at /etc/ansible/ansible.cfg
```sh
# create local ansible.cfg 
[defaults]
inventory = inventory
private_key_file = ~/.ssh/ansible
interpreter_python = /usr/bin/python3 # to silence python interpreter warning above
```
#### 11. retry ping after defining ansible.cfg
```sh
╰─❯ ansible all -m ping
192.168.0.139 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
192.168.0.124 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
192.168.0.3 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
192.168.0.66 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```
#### 12. update systems cache with apt
```sh
# -a (argument) --become (sudo) --ask-become-pass (ask for pass...)
╰─❯ ansible all -m apt -a update_cache=true --become --ask-become-pass
BECOME password: # enter password 

192.168.0.124 | CHANGED => {
    "cache_update_time": 1778921452,
    "cache_updated": true,
    "changed": true
}
192.168.0.139 | CHANGED => {
    "cache_update_time": 1778921452,
    "cache_updated": true,
    "changed": true
}
[ERROR]: Task failed: Timeout (12s) waiting for privilege escalation prompt:
Origin: <adhoc 'apt' task>

{'action': 'apt', 'args': {'update_cache': 'true'}, 'timeout': 0, 'async_val': 0, 'poll': 15}

192.168.0.66 | UNREACHABLE! => {
    "changed": false,
    "msg": "Task failed: Timeout (12s) waiting for privilege escalation prompt:",
    "unreachable": true
}
192.168.0.3 | UNREACHABLE! => {
    "changed": false,
    "msg": "Task failed: Timeout (12s) waiting for privilege escalation prompt:",
    "unreachable": true
}
```
- ubuntu 26.04 has different sudo password prompt than traditional. 
```sh
student@ubuntu2604:~$ sudo apt update
[sudo: authenticate] Password:
# VS
student@ubuntu2204:~$ sudo apt update
[sudo] password for student: 
```
- fix by adding student to NOPASSWD on both 26.04 vms
```sh
sudo visudo

# add at bottom
student ALL=(ALL) NOPASSWD: ALL
```
```sh
# update cache
╰─❯ ansible all -m apt -a update_cache=true --become --ask-become-pass

# upgrade dist!
╰─❯ ansible all -m apt -a upgrade=dist --become -ask-become-pass
```
#### 13. run first playbook (install apache2)
- check file install_apache.yml
```sh
╰─❯ ansible-playbook --ask-become-pass install_apache.yml

╰─❯ ansible-playbook --ask-become-pass install_apache.yml                                                                                                               
BECOME password:                                                                                                                                                             
PLAY [all] *******************************************************************************
                                                       
TASK [Gathering Facts] *******************************************************************************
ok: [192.168.0.124]                                                                                                                                                     
ok: [192.168.0.139]                                                                                                                                                     
ok: [192.168.0.66]                                                                                                                                                      
ok: [192.168.0.3]                                                                                                                                                                  
TASK [install apache2 package] *******************************************************************************
changed: [192.168.0.3]                                                                                                                                                  
changed: [192.168.0.66]                                                                                                                                                 
changed: [192.168.0.139]                                                                                                                                                
changed: [192.168.0.124]                                                                                                                                                                                          
PLAY RECAP *****************************************************************************************************
192.168.0.124              : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0                                                      
192.168.0.139              : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0                                                      
192.168.0.3                : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0                                                      
192.168.0.66               : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0           
```