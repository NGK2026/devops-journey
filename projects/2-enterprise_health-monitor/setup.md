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

