#### 1. Mount Jenkins container && Create Jenkins file
```sh
╰─❯ docker run \     
-p 8080:8080 -p 50000:50000 \
-d -v jenkins_home:/var/jenkins_home \
--name jenkins \
jenkins/jenkins
```
#### 2. Register Dockerhub credentials on Jenkins
1. Manage Jenkins > Credentials > Add Credentials > Username with password
2. Scope: Global
3. Fill Username, Add Dockerhub token as Password
4. Specify desired ID

#### 3. Specify environment variables in Jenkinsfile
1. Image name, image tag
2. Dockerhub credentials 

#### 4. Create build stage in JF
1. docker build tag imagename : imagetag

#### 5. Push to dockerhub with JF
1. docker login using environment credentials user and pass
2. docker push imagename : image tag

#### 6. Deploy using Helm to K8 with JF
1. Use helm upgrade --install to upgrade if existant or install if not
2. specify deployment name
3. chart path
4. set image name and image tag

#### 7. Define post action if success or fail
1. if succeeded print success !!!
2. if failed print Failed !!!

#### 8. create Helm boilerplate chart
1. 
```sh
╰─❯ helm create helm/health-monitor-p2

╰─❯ ls health-monitor-p2               
charts  Chart.yaml  templates  values.yaml
```
2. Modify values.yaml image from defailt nginx to:
```yaml
image:
  repository: ngk2026/devops-journey-p2
  # This sets the pull policy for images.
  pullPolicy: IfNotPresent
  # Overrides the image tag whose default is the chart appVersion.
  tag: "latest"
```
3. modify service type, port and add nodePort
```yaml
service:
  type: NodePort
  port: 5000
  nodePort: 30001
```
#### 9. Test locally
```sh
╰─❯ minikube start

╰─❯ helm install health-monitor-p2 ./health-monitor-p2
NAME: health-monitor-p2
LAST DEPLOYED: Mon May 25 23:05:23 2026
NAMESPACE: default
STATUS: deployed
REVISION: 1
DESCRIPTION: Install complete

╰─❯ helm list
NAME             	NAMESPACE	REVISION	UPDATED                                 	STATUS  	CHART                  	APP VERSION
health-monitor-p2	default  	1       	2026-05-25 23:05:23.957495502 +0300 EEST	deployed	health-monitor-p2-0.1.0	1.16.0  
╰─❯ kubectl get svc
NAME                TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
health-monitor-p2   NodePort    10.107.29.84   <none>        5000:31649/TCP   4m42s
```
#### 10. Create Jenkins Pipeline
1. New Item > Item name: health-monitor-p2 > OK
2. Display Name: health-monitor-p2
3. Branch Sources > Git > Credentials: Select repo credentials
4. Repository HTTPS URL: enter repo url
5. Behaviors > Add: Filter by name (with regular expression) 
6. Regular expression: ^main$
7. Build Configuration > Script Path: projects/2-enterprise_health-monitor/Jenkinsfile
8. RUN:
```sh
+ docker build -t ngk2026/devops-journey-p2:latest .
/var/jenkins_home/workspace/health-monitor-p2_main@tmp/durable-4b912197/script.sh.copy: 1: docker: not found
script returned exit code 127
```
- error: docker: not found
#### 11. Mount host docker into Jenkins container
```sh
╰─❯ docker stop jenkins  

╰─❯ docker rm jenkins  

╰─❯ docker run -p 8080:8080 -p 50000:50000 \
-d \
-v jenkins_home:/var/jenkins_home \
-v /var/run/docker.sock:/var/run/docker.sock \
--name jenkins \
jenkins/jenkins

# access container interactive bash terminal
╰─❯ docker exec -it jenkins bash            
jenkins@63f7ff975006:/$ curl https://get.docker.com | sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 22446  100 22446    0     0   222k      0 --:--:-- --:--:-- --:--:--  223k
# Executing docker install script, commit: 2687d91ddeb3bd6aeae37a90947761efdee87030
+ su -c apt-get -qq update >/dev/null
Password: su: Authentication failure
jenkins@63f7ff975006:/$ exit

# access as root instead
╰─❯ docker exec -u root -it jenkins bash
root@63f7ff975006:/$ curl https://get.docker.com | sh
# add jenkins user to docker group
root@63f7ff975006:/$ usermod -aG docker jenkins
root@63f7ff975006:/$ exit
╰─❯ docker restart jenkins
```
- retry build
```sh
ERROR: permission denied while trying to connect to the docker API at unix:///var/run/docker.sock

script returned exit code 1
```
```sh
# host
# check docker.sock permissions
╰─❯ ls -la /var/run/docker.sock
srw-rw---- 1 root docker 0 May 25 21:39 /var/run/docker.sock

# check GID of docker group
╰─❯ getent group docker
docker:x:947:student

# set jenkins group same GID
╰─❯ docker exec -u root -it jenkins bash
root@63f7ff975006:/$ getent group docker
docker:x:995:jenkins

root@63f7ff975006:/$ groupmod -g 947 docker
root@63f7ff975006:/$ exit
╰─❯ docker restart jenkins
```
#### 12. Retry Build
```sh
ERROR: failed to build: failed to solve: failed to read dockerfile: open Dockerfile: no such file or directory
```
- Set Jenkins build dockerfile location
```yaml
stage("Build Docker image") {

    steps {
        sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ./projects/2-enterprise_health-monitor/"
    }
}
```
- build success
```sh
#9 DONE 1.0s
```
- stage 3 Helm
```sh
/var/jenkins_home/workspace/health-monitor-p2_main@tmp/durable-61ca1327/script.sh.copy: 1: helm: not found
```
#### 13. Install helm and kubectl on jenkins container
```sh
╰─❯ docker exec -u root -it jenkins bash
root@63f7ff975006:/$ curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
helm installed into /usr/local/bin/helm

root@63f7ff975006:/$ curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
root@63f7ff975006:/$ ls
bin  boot  dev	etc  home  kubectl  lib  lib64	media  mnt  opt  proc  root  run  sbin	srv  sys  tmp  usr  var

root@63f7ff975006:/$ chmod +x kubectl
root@63f7ff975006:/$ mv kubectl /usr/local/bin/
root@63f7ff975006:/$ exit

╰─❯ docker exec -it jenkins bash -c "kubectl version --client"
Client Version: v1.36.1
Kustomize Version: v5.8.1

╰─❯ docker exec -it jenkins bash -c "helm version --client"
version.BuildInfo{Version:"v3.21.0", GitCommit:"e0878d41b711792be60777fd65ad23a101e6b85f", GitTreeState:"clean", GoVersion:"go1.25.10"}

# copy kubeconfig into jenkins container, to point to host minikube
╰─❯ docker cp ~/.kube/config jenkins:/var/jenkins_home/.kube/config
Successfully copied 816B (transferred 2.56kB) to jenkins:/var/jenkins_home/.kube/config
```
- set in Jenkinsfile env_var KUBECONFIG to point helm into the right direction

#### 14. Rebuild
```sh
Error: Kubernetes cluster unreachable: invalid configuration: [unable to read client-cert /
```
#### 15. Mount minikube certs into container!
```sh
╰─❯ docker stop jenkins

╰─❯ docker rm jenkins

╰─❯ docker run -p 8080:8080 -p 50000:50000 \
  -d \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /home/student/.minikube:/home/student/.minikube \
  --name jenkins \
  jenkins/jenkins

# log into container, install docker, k8 and helm
╰─❯ docker exec -u root -it jenkins bash   
# install docker
root@8c6dc78f0a88:/$ curl https://get.docker.com | sh
# add jenkins to docker group
root@8c6dc78f0a88:/$ usermod -aG docker jenkins
# set GID as host's
root@8c6dc78f0a88:/$ groupmod -g 947 docker
# install helm
root@8c6dc78f0a88:/$ curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
# install kubernetes
root@8c6dc78f0a88:/$ curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
# make executable
root@8c6dc78f0a88:/$ chmod +x kubectl
# move to usr bin
root@8c6dc78f0a88:/$ mv kubectl /usr/local/bin/
# create kube config location
root@8c6dc78f0a88:/$ mkdir -p /var/jenkins_home/.kube
# change perm from root to jenkins
root@8c6dc78f0a88:/$ chown -R jenkins:jenkins /var/jenkins_home/.kube

# docker has copy bug from host to container...
# cat host .kube/config, pipe it into container .kube/config
╰─❯ cat ~/.kube/config | docker exec -i jenkins bash -c "cat > /var/jenkins_home/.kube/config"

# cat container .kube/config
root@8c6dc78f0a88:/$ cat /var/jenkins_home/.kube/config 
apiVersion: v1
clusters:
- cluster:
    certificate-authority: /home/student/.minikube/ca.crt

---snip---
root@8c6dc78f0a88:/$ exit
╰─❯ docker restart jenkins
```
#### 16. Rebuild jenkins pipeline
- state 3 output:
```sh
# cannot reach host network
Error: Kubernetes cluster unreachable: Get "https://192.168.49.2:8443/version": dial tcp 192.168.49.2:8443: i/o timeout
```
#### 17. Container network
1. check container network
```sh
╰─❯ docker inspect jenkins | grep -A 20 "Networks"
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "DriverOpts": null,
                    "GwPriority": 0,
                    "NetworkID": "a0a8e82454facf238a9d7302d36cc2e7ece749035bac3ec8509a5456e5f2d46c",
                    "EndpointID": "2eadb08f758b4497b60a6a153d0455f269ac917c0fe68493c62b70a145e74922",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "MacAddress": "ea:7d:87:34:30:82",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "DNSNames": null
                }
            }
        }
```
- container 172.17.0.2, host 192.168.49.2 (different networks)
2. run container on host network
```sh
╰─❯ docker stop jenkins
╰─❯ docker rm jenkins
╰─❯ docker run -p 8080:8080 -p 50000:50000 \
  -d \
  --network host \
  -v jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v /home/student/.minikube:/home/student/.minikube \
  --name jenkins \
  jenkins/jenkins
```
3. check documention above.. reinstalling docker, k8 and helm, recopy .kube/config
4. rebuild!
```sh
Error: path "./health-monitor-p2" not found
```
#### 18. fix Jenkinsfile helm chart path
```yaml
stage("Deploy to Kubernetes using Helm") {

    steps {
        sh "helm upgrade --install health-monitor-p2 ./projects/2-enterprise_health-monitor/health-monitor-p2 --set image.repository=${IMAGE_NAME} --set image.tag=${IMAGE_TAG}" 
    }
}
```
- Output: Production Success !!!

#### 18. Proof!
```sh
╰─❯ helm list
NAME             	NAMESPACE	REVISION	UPDATED                                	STATUS  	CHART                  	APP VERSION
health-monitor-p2	default  	1       	2026-05-25 22:13:45.362763613 +0000 UTC	deployed	health-monitor-p2-0.1.0	1.16.0     

╰─❯ kubectl get po   
NAME                                 READY   STATUS    RESTARTS     AGE
health-monitor-p2-78f44b8f5d-fdmms   0/1     Running   1 (4s ago)   64s

╰─❯ kubectl get po                                 
NAME                                 READY   STATUS             RESTARTS      AGE
health-monitor-p2-78f44b8f5d-fdmms   0/1     CrashLoopBackOff   5 (40s ago)   6m40s
```
- 5 restarts up till now, check logs
```sh
╰─❯ kubectl logs health-monitor-p2-78f44b8f5d-fdmms
 * Serving Flask app 'app'
--snip--
10.244.0.1 - - [25/May/2026 22:21:25] "GET / HTTP/1.1" 404 -
```
#### 19. Flask app.py enpoint at /metrics, fix helm values.yaml
- liveness/rediness probe paths
```yaml
livenessProbe:
  httpGet:
    path: /metrics
    port: http
readinessProbe:
  httpGet:
    path: /metrics
    port: http
```
#### 20. Ansible setup
1. create ssh key
```sh
╰─❯ ssh-keygen -t ed25519 -C "devops-p2"
╰─❯ ssh-keygen -t ed25519 -C "ansible-p2" 
```
2. migrate public keys to each VM
```sh
╰─❯ ssh-copy-id -i ~/.ssh/devops-p2.pub 192.168.0.38  # arch
╰─❯ ssh-copy-id -i ~/.ssh/ansible-p2.pub 192.168.0.38

╰─❯ ssh-copy-id -i ~/.ssh/devops-p2.pub 192.168.0.171 # centos
╰─❯ ssh-copy-id -i ~/.ssh/ansible-p2.pub 192.168.0.171

╰─❯ ssh-copy-id -i ~/.ssh/devops-p2.pub 192.168.0.124 # ubuntu 22.04
╰─❯ ssh-copy-id -i ~/.ssh/ansible-p2.pub 192.168.0.124

╰─❯ ssh-copy-id -i ~/.ssh/devops-p2.pub 192.168.0.3   # ubuntu 26.04
╰─❯ ssh-copy-id -i ~/.ssh/ansible-p2.pub 192.168.0.3
```
3. create inventory
4. create ansible.cfg
5. create playbook vm_setup.yml
6. update packages on all vms
7. create root user void and update ansible.cfg
8. install docker
- specify ubuntu versions
```sh
╰─❯ ansible all -m gather_facts --limit 192.168.0.124 | grep ansible_distribution_major_version
        "ansible_distribution_major_version": "22",

╰─❯ ansible all -m gather_facts --limit 192.168.0.3 | grep ansible_distribution_major_version
        "ansible_distribution_major_version": "26",
```
- centos requires add docker repo
- https://docs.ansible.com/projects/ansible/latest/collections/ansible/builtin/get_url_module.html
- https://docs.docker.com/engine/install/centos/
```yaml
# CENTOS
# ADD REPO
  - name: add docker repo (centos)
    ansible.builtin.get_url:
      url: https://download.docker.com/linux/centos/docker-ce.repo
      dest: /etc/yum.repos.d/docker-ce.repo
      mode: '0440'
    when: 
    - ansible_facts['distribution'] == "CentOS"  
# INSTALL DOCKER
  - name: install docker from docker repo
    dnf:
      name:
        - docker-ce
        - docker-ce-cli
        - containerd.io
        - docker-buildx-plugin
        - docker-compose-plugin
    when: 
      - ansible_facts['distribution'] == "CentOS"
```
#### 21. start/enable docker service
```yaml
  - name: start service
    tags: 
    service:
      name: 
      state: started
      enabled: true
```
- ubuntu 22 docker service not available
```sh
student@ubuntu2204:~$ sudo apt install docker
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
docker is already the newest version (1.5-2).
0 upgraded, 0 newly installed, 0 to remove and 13 not upgraded.
```
- must install docker engine from docker official
https://docs.docker.com/engine/install/ubuntu/

#### 22. docker official ubuntu
```sh
# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update
```
-yaml
```yaml
  - name: add docker GPG (ubuntu 22)
    ansible.builtin.get_url:
      url: https://download.docker.com/linux/ubuntu/gpg
      dest: /etc/apt/keyrings/docker.asc
      mode: '0644'
    when:
      - ansible_facts['distribution'] == "Ubuntu"
      - ansible_facts['distribution_major_version'] == "22"

  - name: add docker repo (ubuntu 22)
    ansible.builtin.apt_repository:
      repo: "deb [arch={{ ansible_dependency_architecture }} signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu {{ ansible_distribution_release }} stable"
      state: present
    when:
      - ansible_facts['distribution'] == "Ubuntu"
      - ansible_facts['distribution_major_version'] == "22"

  - name: install docker (ubuntu 22)
    apt:
      name:
        - docker-ce
        - docker-ce-cli
        - containerd.io
        - docker-buildx-plugin
        - docker-compose-plugin
      state: latest
    when:
      - ansible_facts['distribution'] == "Ubuntu"
      - ansible_facts['distribution_major_version'] == "22"
```
- run playbook
```sh
fatal: [192.168.0.124]: FAILED! => {"changed": false, "msg": "Task failed: Finalization of task args for 'ansible.builtin.apt_repository' failed: Error while resolving value for 'repo': 'ansible_dependency_architecture' is undefined"}
```
- 'ansible_dependency_architecture' is undefined", meaning:
- ansible dependency architecture = x86_64
- Ubuntu expects amd64
```yaml
# use j2
- name: add docker repo (ubuntu 22)
    ansible.builtin.apt_repository:
      repo: "deb [arch={{ 'amd64' if ansible_architecture == 'x86_64' else 'arm64' }} signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu {{ ansible_distribution_release }} stable"
      filename: docker
      state: present
    when:
      - ansible_facts['distribution'] == "Ubuntu"
      - ansible_facts['distribution_major_version'] == "22"
```
- ansible-playbook
```sh
 W:GPG error: https://download.docker.com/linux/ubuntu jammy InRelease: Unknown error executing apt-key, E:The repository 'https://download.docker.com/linux/ubuntu jammy InRelease' is not signed."
```
#### 23. fix "Unknown error executing apt-key"
- install dependancy binary tools first! then add GPG
```yaml
- name: install repository prerequisites (Ubuntu 22)
    apt:
      name:
        - gnupg
        - software-properties-common
        - ca-certificates
        - curl
      state: present
      update_cache: true
    when:
      - ansible_facts['distribution'] == "Ubuntu"
      - ansible_facts['distribution_major_version'] == "22"

  - name: add docker GPG (ubuntu 22)
    ansible.builtin.get_url:
      url: https://download.docker.com/linux/ubuntu/gpg
      dest: /etc/apt/keyrings/docker.asc
      mode: '0644'
    when:
      - ansible_facts['distribution'] == "Ubuntu"
      - ansible_facts['distribution_major_version'] == "22"
```
- run ansible-playbook! = same error.
#### 24. Use apt install docker.io instead of the current circus! of gpg, repo and bleeding edge docker!
```yaml
# UBUNTU 22
  - name: install docker (ubuntu 22)
    apt:
      name:
        - docker.io
      state: latest
    when:
      - ansible_facts['distribution'] == "Ubuntu"
      - ansible_facts['distribution_major_version'] == "22"
```
- Success :)

#### 25. Back to enable/start docker service
```yaml
  - name: start service
    tags: 
    service:
      name: 
      state: started
      enabled: true
```

#### 26. pull and run docker containers in VMS
- https://docs.ansible.com/projects/ansible/latest/collections/community/docker/docker_container_module.html
```yaml
- name: Start Jenkins container
  community.docker.docker_container:
    name: jenkins
    image: jenkins/jenkins
    state: started
    restart_policy: always
    network_mode: host
    volumes:
      - jenkins_home:/var/jenkins_home
      - /var/run/docker.sock:/var/run/docker.sock
      - /home/student/.minikube:/home/student/.minikube
    ports:
      - "8080:8080"
      - "50000:50000"
```
- ERROR ARCH:
```sh
fatal: [192.168.0.38]: FAILED! => {"changed": false, "msg": "Failed to import the required Python library (requests) on archlinux's Python /usr/bin/python3. Please read the module documentation and install it in the appropriate location. If the required library is installed, but Ansible is using the wrong Python interpreter, please consult the documentation on ansible_python_interpreter"}
```
- ERROR CENTOS:
```sh
fatal: [192.168.0.171]: FAILED! => {"changed": false, "msg": "Failed to import the required Python library (requests) on centos's Python /usr/bin/python3. Please read the module documentation and install it in the appropriate location. If the required library is installed, but Ansible is using the wrong Python interpreter, please consult the documentation on ansible_python_interpreter"}
```
- FIX, install python request library
```yaml
# INSTALL PYTHON REQUEST REQ ARCH
  - name: install python requests (arch)
    community.general.pacman:
      name: python-requests
      state: present
    when: ansible_facts['distribution'] == "Archlinux"
# INSTALL PYTHON REQUEST REQ CENTOS
  - name: install python requests (centos)
    ansible.builtin.dnf:
      name: python3-requests
      state: present
    when: ansible_facts['distribution'] == "CentOS"
```
- Success!

#### 27. create host_vars
```sh
mkdir host_vars && cd host_vars
touch 192.168.0.3.yml 192.168.0.38.yml 192.168.0.124.yml 192.168.0.171.yml
```
- create variables

#### 28. create bash script to install kubernetes on ubuntu and centos
1. place it in ./files/
2. move it with ansible to ubuntu and centos
3. run script with ansible
4. install kubernetes on arch vm as well

#### 29. init ubuntu 22 as kubeadm master
```sh
# test
student@ubuntu2204:~$ sudo kubeadm init --apiserver-advertise-address=192.168.0.124 --pod-network-cidr=10.244.0.0/16
Your Kubernetes control-plane has initialized successfully!
```
1. create playbook task
2. create CNI plugin install script and deliver it with playbook
3. after install, create a file at /etc/kubernetes/ to use as arg: creates 

#### 30. connect other VMs to cluster using token
1. send tokens to other vms
2. success:
```sh
student@ubuntu2204:~$ kubectl get nodes
NAME         STATUS     ROLES           AGE   VERSION
ubuntu2204   Ready      control-plane   30m   v1.36.1
ubuntu2604   Ready      <none>          27m   v1.36.1
```
3. archlinux and centos erros:
```sh
 "command failed" err="failed to run Kubelet: running with swap on is not s
upported, please disable swap or set --fail-swap-on flag to false"
```
4. disable swap on both VMs
```sh
sudo systemctl stop systemd-zram-setup@zram0.service 2>/dev/null || true
sudo systemctl disable systemd-zram-setup@zram0.service 2>/dev/null || true
sudo systemctl mask systemd-zram-setup@zram0.service 2>/dev/null || true
sudo swapoff -a
```
5. reset kubeadm and clean leftover files
```sh
sudo kubeadm reset -f
sudo rm -rf /etc/kubernetes/kubelet.conf /etc/kubernetes/pki/ /var/lib/kubelet/*
```
6. re-run kubeadm join
```sh
student@ubuntu2204:~$ kubectl get nodes
NAME         STATUS     ROLES           AGE     VERSION
archlinux    NotReady   <none>          4m17s   v1.36.1
centos       NotReady   <none>          3m2s    v1.36.1
ubuntu2204   Ready      control-plane   33m     v1.36.1
ubuntu2604   Ready      <none>          30m     v1.36.1

[student@archlinux ~]$ journalctl -xeu kubelet
": open /run/systemd/resolve/resolv.conf: no such file or directory\"
```
7. create missing symlink dir, for both archlinux and centos
```sh
sudo mkdir -p /run/systemd/resolve
sudo ln -sf /etc/resolv.conf /run/systemd/resolve/resolv.conf
# then restart kubelet service
sudo systemctl restart kubelet
```
8. success
```sh
student@ubuntu2204:~$ kubectl get nodes -o wide
NAME         STATUS   ROLES           AGE   VERSION   INTERNAL-IP     EXTERNAL-IP   OS-IMAGE                      KERNEL-VERSION                   CONTAINER-RUNTIME
archlinux    Ready    <none>          11m   v1.36.1   192.168.0.38    <none>        Arch Linux                    7.0.8-arch1-1 (amd64)            containerd://2.3.1
centos       Ready    <none>          10m   v1.36.1   192.168.0.171   <none>        CentOS Stream 10 (Coughlan)   6.12.0-227.el10.x86_64 (amd64)   containerd://2.2.4
ubuntu2204   Ready    control-plane   40m   v1.36.1   192.168.0.124   <none>        Ubuntu 22.04.5 LTS            5.15.0-179-generic (amd64)       containerd://2.2.1
ubuntu2604   Ready    <none>          37m   v1.36.1   192.168.0.3     <none>        Ubuntu 26.04 LTS              7.0.0-15-generic (amd64)         containerd://2.2.2
```
#### 31. accecss nodes from host archlinux
- on ubuntu 22 /etc/kubernetes/admin.conf change perm to 644
```sh
╰─❯ mkdir -p ~/.kube
╰─❯ scp student@192.168.0.124:/etc/kubernetes/admin.conf ~/.kube/config
╰─❯ kubectl get nodes
NAME         STATUS   ROLES           AGE   VERSION
archlinux    Ready    <none>          20m   v1.36.1
centos       Ready    <none>          19m   v1.36.1
ubuntu2204   Ready    control-plane   49m   v1.36.1
ubuntu2604   Ready    <none>          46m   v1.36.1
```
- deploy app to cluster
```sh
╰─❯ helm upgrade --install health-monitor-p2 ./health-monitor-p2 --set image.repository=ngk2026/devops-journey-p2 --set image.tag=latest
╰─❯ kubectl get pods -o wide
NAME                                 READY   STATUS    RESTARTS   AGE   IP           NODE        NOMINATED NODE   READINESS GATES
health-monitor-p2-6b5576c469-kn97g   1/1     Running   0          73s   10.244.2.2   archlinux   <none>           <none>
```
- check values.yaml replica count
```sh
╰─❯ cat health-monitor-p2/values.yaml | grep replica
replicaCount: 1
```
- edit it to 4, then helm upgrade
```sh
╰─❯ helm upgrade --install health-monitor-p2 ./health-monitor-p2 --set image.repository=ngk2026/devops-journey-p2 --set image.tag=latest
╰─❯ kubectl get pods -o wide
╰─❯ kubectl get pods -o wide
NAME                                 READY   STATUS              RESTARTS        AGE     IP           NODE        NOMINATED NODE   READINESS GATES
health-monitor-p2-6b5576c469-26tjh   0/1     ContainerCreating   0               3m11s   <none>       centos      <none>           <none>
health-monitor-p2-6b5576c469-kn97g   1/1     Running             3 (2m42s ago)   11m     10.244.2.2   archlinux   <none>           <none>
health-monitor-p2-6b5576c469-p5v8p   1/1     Running             1 (3m34s ago)   3m11s   10.244.2.3   archlinux   <none>           <none>
health-monitor-p2-6b5576c469-r25qk   0/1     ContainerCreating   0               3m11s   <none>       centos      <none>           <none>
```
- troubleshoot
```sh
╰─❯ kubectl describe pod health-monitor-p2-6b5576c469-26tjh | tail -20
  Warning  FailedCreatePodSandBox  3m22s               kubelet            Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "b69db2174e00fe82d6c94591c5976f4a623639e62f1134f29309c33caa3b7f4b": plugin type="flannel" failed (add): failed to load flannel 'subnet.env' file: open /run/flannel/subnet.env: no such file or directory. Check the flannel pod log for this node.

╰─❯ kubectl logs health-monitor-p2-6b5576c469-kn97g
Error from server: Get "https://192.168.0.38:10250/containerLogs/default/health-monitor-p2-6b5576c469-kn97g/health-monitor-p2": dial tcp 192.168.0.38:10250: connect: no route to host
```
- flannel...
```sh
╰─❯ kubectl get pods -n kube-flannel -o wide
NAME                    READY   STATUS             RESTARTS         AGE   IP              NODE         NOMINATED NODE   READINESS GATES
kube-flannel-ds-6zfzt   0/1     CrashLoopBackOff   28 (5m23s ago)   62m   192.168.0.3     ubuntu2604   <none>           <none>
kube-flannel-ds-h5z6m   0/1     CrashLoopBackOff   17 (2m15s ago)   64m   192.168.0.124   ubuntu2204   <none>           <none>
kube-flannel-ds-jqgsr   1/1     Running            0                36m   192.168.0.38    archlinux    <none>           <none>
kube-flannel-ds-l5l9h   0/1     CrashLoopBackOff   9 (7m17s ago)    35m   192.168.0.171   centos       <none>           <none>
```
- master control plane flannel logs
```sh
student@ubuntu2204:~$ kubectl logs kube-flannel-ds-h5z6m -n kube-flannel
E0526 23:05:37.260316       1 main.go:289] Failed to check br_netfilter: stat /proc/sys/net/bridge/bridge-nf-call-iptables: no such file or directory
```
#### 32. br_netfilter fix
```sh
sudo modprobe br_netfilter
echo "br_netfilter" | sudo tee /etc/modules-load.d/br_netfilter.conf
sudo sysctl -w net.bridge.bridge-nf-call-iptables=1
echo "net.bridge.bridge-nf-call-iptables=1" | sudo tee /etc/sysctl.d/99-kubernetes.conf
sudo sysctl --system
```
- then restart flannel on control plane
```sh
kubectl rollout restart daemonset kube-flannel-ds -n kube-flannel

╰─❯ kubectl get pods -n kube-flannel -o wide
NAME                    READY   STATUS    RESTARTS   AGE   IP              NODE         NOMINATED NODE   READINESS GATES
kube-flannel-ds-5n9rd   1/1     Running   0          10m   192.168.0.171   centos       <none>           <none>
kube-flannel-ds-kv475   1/1     Running   0          10m   192.168.0.124   ubuntu2204   <none>           <none>
kube-flannel-ds-ndlnm   1/1     Running   0          10m   192.168.0.3     ubuntu2604   <none>           <none>
kube-flannel-ds-vksvv   1/1     Running   0          10m   192.168.0.38    archlinux    <none>           <none>
```
#### 33. troubleshoot health-monitor-p2
```sh
╰─❯ kubectl logs health-monitor-p2-6b5576c469-26tjh
Error from server: Get "https://192.168.0.171:10250/containerLogs/default/health-monitor-p2-6b5576c469-26tjh/health-monitor-p2": dial tcp 192.168.0.171:10250: connect: no route to host
```
- firewall unblock 10250
```
[student@archlinux ~]$ systemctl list-unit-files --type=service | grep -E 'firewall|ufw|iptables|nftables'
firewalld.service                            enabled         disabled

[student@centos ~]$ systemctl list-unit-files --type=service | grep -E 'firewall|ufw|iptables|nftables'
firewalld.service                            enabled         enabled

student@ubuntu2204:~$ systemctl list-unit-files --type=service | grep -E 'firewall|ufw|iptables|nftables'
ufw.service                                enabled         enabled

student@ubuntu2604:~$ systemctl list-unit-files --type=service | grep -E 'firewall|ufw|iptables|nftables'
ufw.service                                  enabled         enabled
```
- use firewall ./files/  scripts respectively
```sh
╰─❯ kubectl logs health-monitor-p2-6b5576c469-26tjh
 * Serving Flask app 'app'
--snip
10.244.3.1 - - [26/May/2026 23:37:06] "GET /metrics HTTP/1.1" 200 -
10.244.3.1 - - [26/May/2026 23:37:07] "GET /metrics HTTP/1.1" 200 -

╰─❯ kubectl get pods -o wide
NAME                                 READY   STATUS    RESTARTS         AGE   IP           NODE        NOMINATED NODE   READINESS GATES
health-monitor-p2-6b5576c469-26tjh   0/1     Running   11 (3m43s ago)   41m   10.244.3.3   centos      <none>           <none>
health-monitor-p2-6b5576c469-kn97g   1/1     Running   14 (3m52s ago)   49m   10.244.2.2   archlinux   <none>           <none>
health-monitor-p2-6b5576c469-p5v8p   1/1     Running   13 (6m13s ago)   41m   10.244.2.3   archlinux   <none>           <none>
health-monitor-p2-6b5576c469-r25qk   0/1     Running   10 (9m23s ago)   41m   10.244.3.2   centos      <none>           <none>
```
- centos is heavy, add delay and failure threshold in values.yaml
```yaml
livenessProbe:
  httpGet:
    path: /metrics
    port: http
  initialDelaySeconds: 30
  failureThreshold: 10
  periodSeconds: 10
readinessProbe:
  httpGet:
    path: /metrics
    port: http
  initialDelaySeconds: 30
  failureThreshold: 10
  periodSeconds: 10
```
- helm upgrade
```sh
╰─❯ helm upgrade --install health-monitor-p2 ./health-monitor-p2 --set image.repository=ngk2026/devops-journey-p2 --set image.tag=latest
╰─❯ kubectl get pods -o wide -w
NAME                                READY   STATUS    RESTARTS   AGE   IP            NODE         NOMINATED NODE   READINESS GATES
health-monitor-p2-9df7d9d79-chmxl   1/1     Running   0          5s    10.244.3.12   centos       <none>           <none>
health-monitor-p2-9df7d9d79-k4c8x   1/1     Running   0          5s    10.244.1.5    ubuntu2604   <none>           <none>
health-monitor-p2-9df7d9d79-kkpwx   1/1     Running   0          5s    10.244.2.17   archlinux    <none>           <none>

```
