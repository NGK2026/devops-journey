#### 1. Create Jenkins file

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
3. Branch Sources > GitHub > Credentials: Select repo credentials
4. Repository HTTPS URL: enter repo url
5. Behaviors > Add: Filter by name (with regular expression) 
6. Regular expression: ^main$
7. Build Configuration > Script Path: projects/2-enterprise_health-monitor/Jenkinsfile
