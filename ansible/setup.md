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
                                                                                                            
BECOME password:                                                                                                                                                             
PLAY [all] ********************************************************************
                                                       
TASK [Gathering Facts] ********************************************************
ok: [192.168.0.124]                                                                                                                                                     
ok: [192.168.0.139]                                                                                                                                                     
ok: [192.168.0.66]                                                                                                                                                      
ok: [192.168.0.3]                                                                                                                                                                  
TASK [install apache2 package] ************************************************
changed: [192.168.0.3]                                                                                                                                                  
changed: [192.168.0.66]                                                                                                                                                 
changed: [192.168.0.139]                                                                                                                                                
changed: [192.168.0.124]                                                                                                                                                                                          
PLAY RECAP ********************************************************************
192.168.0.124              : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0                                                      
192.168.0.139              : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0                                                      
192.168.0.3                : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0                                                      
192.168.0.66               : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0           
```
#### 14. upgrade apt index, add/update {apache, php} (install_apache_v2.yml)
```sh
╰─❯ ansible-playbook --ask-become-pass install_apache_v2.yml

BECOME password: 

PLAY [all] ******************************************************************

TASK [Gathering Facts] ******************************************************
ok: [192.168.0.124]
--snip

TASK [update repository index] ***********************************************
changed: [192.168.0.3]
--snip

TASK [install apache2 package] ***********************************************
ok: [192.168.0.66]
--snip

TASK [add php support for apache] ********************************************
changed: [192.168.0.139]
--snip

PLAY RECAP *******************************************************************
192.168.0.124              : ok=4    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
--snip
```
#### 15. remove (absent) apache & php (remove_apache.yml)
```sh
╰─❯ ansible-playbook --ask-become-pass remove_apache.yml
```
#### 16. install Centos VM, create install-apache_v3.yml to seperate ubuntu from centos
```sh
╰─❯ ansible-playbook --ask-become-pass remove_apache_v3.yml

PLAY RECAP ***********************************************************
192.168.0.124              : ok=4    changed=1    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0   
192.168.0.139              : ok=4    changed=1    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0   
192.168.0.171              : ok=4    changed=2    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0   
192.168.0.3                : ok=4    changed=1    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0   
192.168.0.66               : ok=4    changed=1    unreachable=0    failed=0    skipped=3    rescued=0    ignored=0   
```
- ssh into centos, allow service and allow firewall
```sh
[student@centos ~]$ sudo systemctl start httpd
[student@centos ~]$ sudo systemctl enable httpd
[student@centos ~]$ sudo firewall-cmd --permanent --add-service=http
[student@centos ~]$ sudo firewall-cmd --reload
```
#### 17. trim install_apache_v3.yml into v4, use variables to reduce to 1 play
```yml
  - name: update index and install apache and php
    package:
      name:
        - "{{ apache_package }}"
        - "{{ php_package }}"
      state: latest
      update_cache: true
```
- inventory: declare variables for each host ip
```txt
192.168.0.124 apache_package=apache2 php_package=libapache2-mod-php
192.168.0.139 apache_package=apache2 php_package=libapache2-mod-php
192.168.0.3 apache_package=apache2 php_package=libapache2-mod-php
192.168.0.66 apache_package=apache2 php_package=libapache2-mod-php
192.168.0.171 apache_package=httpd php_package=php
192.168.0.38 apache_package=apache php_package=php
```
#### 18. set groups in the inventory
```txt
[web_servers]
192.168.0.124 # ubuntu 22 v1
192.168.0.139 # ubuntu 22 v2
192.168.0.171 # centos

[db_servers]
192.168.0.3 # ubuntu 26 v1
192.168.0.66 # ubuntu 26 v2

[file_servers]
192.168.0.38 # archlinux
```
- using playbook site_v1.yml, the playbook will only modify according to host availability in the inventory groups
#### 19. using tags
site_v2.yml
```yaml
# ex:
  - name: install updates (centos)
    tags: always # always run reguardless
    dnf:
--snip--
  - name: install apache (centos)
    tags: apache,httpd,centos
    dnf:
      --snip
```
- check available tags with ansible-playbook
```sh
╰─❯ ansible-playbook --list-tags site_v2.yml

playbook: site_v2.yml

  play #1 (all): all    TAGS: []
      TASK TAGS: [always]

  play #2 (web_servers): web_servers    TAGS: []
      TASK TAGS: [apache, apache2, archlinux, centos, httpd, php, ubuntu]

  play #3 (db_servers): db_servers      TAGS: []
      TASK TAGS: [centos, db, mariadb, ubuntu]

  play #4 (file_servers): file_servers  TAGS: []
      TASK TAGS: [samba]
```
- run archlinux tagged
```sh
╰─❯ ansible-playbook --tags archlinux --ask-become-pass site_v2.yml
# Multiple tags
╰─❯ ansible-playbook --tags "apache,db" --ask-become-pass site_v2.yml
```
#### 20. copy files
site_v2.yml
```yaml
    # self explanatory
  - name: copy default html file for site
    tags: apache,apache2,httpd
    copy:
      src: default_site.html
      dest: /var/www/html/index.html
      owner: root
      group: root
      mode: 0644
```
```sh
╰─❯ ansible-playbook --ask-become-pass site_v2.yml
```
#### 21. setup workstation (will use vm instead) /w terraform
site_v2.yml
```yml
- hosts: workstations
  become: true
  tasks:

  - name: install unzip
    package:
      name: unzip

  - name: install terraform
    unarchive:
      src: https://releases.hashicorp.com/terraform/1.15.3/terraform_1.15.3_linux_amd64.zip
      dest: /usr/local/bin
      remote_src: yes
      mode: 0755
      owner: root
      group: root
```
```sh
╰─❯ ansible-playbook --ask-become-pass site_v2.yml
```
#### 22. enable/start services
site_v3.yml
```yml
  - name: start httpd (centos)
    tags: apache,centos,httpd
    service:
      name: httpd
      state: started
      enabled: true
    when: ansible_facts['distribution'] == "CentOS"

# also firewalld
  - name: enable firewalld service httpd
    tags: apache,centos,httpd
    ansible.posix.firewalld:
      service: http
      state: enabled
      permanent: true
      immediate: true
    when: ansible_facts['distribution'] == "CentOS"
```
#### 23. edit/change a line in a file and restart service to take effect
site_v3.yml
```yml
  - name: edit line in file (change email addr for admin)
    tags: apache,centos,httpd
    lineinfile:
      path: /etc/httpd/conf/httpd.conf
      regexp: '^ServerAdmin'
      line: ServerAdmin someone@somewhere.net
    when: ansible_facts['distribution'] == "CentOS"
    register: httpd # remember
  
  - name: restart httpd (centos)
    tags: apache,centos,httpd
    service:
      name: httpd
      state: restarted
    when: httpd.changed # remember, did it change?
```
#### 24. create user, add ssh key, give sudo priv
site_v4.yml
```yml
- hosts: all
  become: true
  tasks:

  - name: create void user
    tags: always
    user:
      name: void
      groups: root
  
  - name: add ssh key for void
    tags: always
    authorized_key:
      user: void
      key: "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINZV/VjSdJNEj5jcdZFz+fq6Nmticv2of6SgNNxlr+Xx ansible"

  - name: add sudoers file for void
    tags: always
    copy:
      src: sudoer_void
      dest: /etc/sudoers.d/void
      owner: root
      group: root
      mode: 0440
```
#### 25. create roles
- create their places in the playbook site_v6.yml
```yml
- hosts: all
  become: true
  roles:
    - base

- hosts: workstations
  become: true
  roles:
    - workstations

- hosts: web_servers
  become: true
  roles:
    - web_servers

- hosts: db_servers
  become: true
  roles:
    - db_servers

- hosts: file_servers
  become: true
  roles:
    - db_servers
```
- create dirs roles/ { ... } /tasts
```sh
╭─ ~/projects/git/devops-journey/ansible/roles/
╰─❯ mkdir -p {base,db_servers,file_servers,web_servers,workstations}/tasks 
```