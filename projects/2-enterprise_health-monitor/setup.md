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
