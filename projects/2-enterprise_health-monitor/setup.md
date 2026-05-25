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
root@63f7ff975006:/# curl https://get.docker.com | sh
# add jenkins user to docker group
root@63f7ff975006:/# usermod -aG docker jenkins
root@63f7ff975006:/# exit
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
root@63f7ff975006:/# getent group docker
docker:x:995:jenkins

root@63f7ff975006:/# groupmod -g 947 docker
root@63f7ff975006:/# exit
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
root@63f7ff975006:/# curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
helm installed into /usr/local/bin/helm

root@63f7ff975006:/# curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
root@63f7ff975006:/# ls
bin  boot  dev	etc  home  kubectl  lib  lib64	media  mnt  opt  proc  root  run  sbin	srv  sys  tmp  usr  var

root@63f7ff975006:/# chmod +x kubectl
root@63f7ff975006:/# mv kubectl /usr/local/bin/
root@63f7ff975006:/# exit

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
root@8c6dc78f0a88:/# curl https://get.docker.com | sh
# add jenkins to docker group
root@8c6dc78f0a88:/# usermod -aG docker jenkins
# set GID as host's
root@8c6dc78f0a88:/# groupmod -g 947 docker
# install helm
root@8c6dc78f0a88:/# curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
# install kubernetes
root@8c6dc78f0a88:/# curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
# make executable
root@8c6dc78f0a88:/# chmod +x kubectl
# move to usr bin
root@8c6dc78f0a88:/# mv kubectl /usr/local/bin/
# create kube config location
root@8c6dc78f0a88:/# mkdir -p /var/jenkins_home/.kube
# change perm from root to jenkins
root@8c6dc78f0a88:/# chown -R jenkins:jenkins /var/jenkins_home/.kube

# docker has copy bug from host to container...
# cat host .kube/config, pipe it into container .kube/config
╰─❯ cat ~/.kube/config | docker exec -i jenkins bash -c "cat > /var/jenkins_home/.kube/config"

# cat container .kube/config
root@8c6dc78f0a88:/# cat /var/jenkins_home/.kube/config 
apiVersion: v1
clusters:
- cluster:
    certificate-authority: /home/student/.minikube/ca.crt

---snip---
root@8c6dc78f0a88:/# exit
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
```

