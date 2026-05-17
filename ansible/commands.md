#### Generate SSH key /w comment and passphrase
```sh
╰─❯ ssh-keygen -t ed25519 -C "default"
# Enter passphrase: ******
```
#### copy key to server
```sh
# -i (input file), to example IP
╰─❯ ssh-copy-id -i ~/.ssh/id_ed25519.pub 172.16.250.133
```
#### Create Ansible key
1. ssh-keygen with different comment
2. save key with different name than the previous (id_25519)
3. skip passphrase for convenience
#### ping hosts
```sh
# -m (module)
╰─❯ ansible all --key-file ~/.ssh/ansible -i inventory -m ping
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
#### list hosts
```sh
╰─❯ ansible all --list-hosts
  hosts (4):
    192.168.0.124
    192.168.0.139
    192.168.0.3
    192.168.0.66
```
#### gather_facts (can limit to any number of hosts)
```sh
╰─❯ ansible all -m gather_facts --limit 192.168.0.124
```
#### install apt pkg vim-nox
```sh
╰─❯ ansible all -m apt -a name=vim-nox --become --ask-become-pass

student@ubuntu2204:~$ apt search vim-nox
# vim-nox/jammy-updates,jammy-security,now 2:8.2.3995-1ubuntu2.29 amd64 [installed]

student@ubuntu2604:~$ apt search vim-nox
# vim-nox/resolute-updates,resolute-security,now 2:9.1.2141-1ubuntu4.1 amd64 [installed]
```
#### upgrade a specific upgradable package (ex: snapd)
```sh
╰─❯ ansible all -m apt -a "name=snapd state=latest" --become --ask-become-pass
```
#### upgrade all (upgrade dist)
```sh
╰─❯ ansible all -m apt -a update_cache=true --become --ask-become-pass

╰─❯ ansible all -m apt -a upgrade=dist --become -ask-become-pass
```
#### run playbook
```sh
╰─❯ ansible-playbook --ask-become-pass install_apache.yml
```
#### Ansible common facts targetting
```sh
╰─❯ ansible all -m gather_facts --limit 192.168.0.3 | grep ansible_distribution
        "ansible_distribution": "Ubuntu",
        "ansible_distribution_file_parsed": true,
        "ansible_distribution_file_path": "/etc/os-release",
        "ansible_distribution_file_variety": "Debian",
        "ansible_distribution_major_version": "26",
        "ansible_distribution_release": "resolute",
        "ansible_distribution_version": "26.04",
```
#### check available tags with ansible-playbook
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
#### run archlinux tagged, specific tag
```sh
╰─❯ ansible-playbook --tags archlinux --ask-become-pass site_v2.yml
```