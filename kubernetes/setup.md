# Content
1- Layers of abstraction
2- Configuration files (deployment/service)
3- Mongodb & Mongo Express cluster
4- Namespace
5- Ingress

## Layers of abstraction
```txt
Deployment manages a ..
ReplicaSet manages a ..
Pod is an abstraction of ..
Container
```
##### 1- install minikube / kubectl
```sh
sudo pacman -S minikube kubectl
```
##### 2- start minikube
```sh
minikube start
``` 
#### 3- create deployment
```sh
╰─❯ kubectl create deployment nginx-depl --image=nginx
deployment.apps/nginx-depl created
```
#### checking logs, fixing DNS resolution, minikube stop/delete
```sh
╰─❯ kubectl create deployment mongo-depl --image=mongo
deployment.apps/mongo-depl created

╰─❯ kubectl get pod   # notice '0/1'                             
NAME                          READY   STATUS             RESTARTS   AGE
mongo-depl-6c557896c-vtdgf    0/1     ImagePullBackOff   0          26s
nginx-depl-74499d8d69-6jpwz   1/1     Running            0          8m53s

╰─❯ kubectl logs mongo-depl-6c557896c-vtdgf                           
Error from server (BadRequest): container "mongo" in pod "mongo-depl-6c557896c-vtdgf" \
is waiting to start: image can't' be pulled
# log means there is no container running

╰─❯ kubectl describe pod mongo-depl-6c557896c-vtdgf
Events:
  Type     Reason     Age                   From               Message
  ----     ------     ----                  ----               -------
  Normal   Scheduled  5m15s                 default-scheduler  Successfully assigned default/mongo-depl-6c557896c-vtdgf to minikube
  Normal   Pulling    110s (x5 over 5m14s)  kubelet            spec.containers{mongo}: Pulling image "mongo"
  Warning  Failed     102s (x5 over 5m6s)   kubelet            spec.containers{mongo}: Failed to pull image "mongo": Error response from daemon: Get "https://registry-1.docker.io/v2/": dial tcp: lookup registry-1.docker.io on 192.168.49.1:53: server misbehaving
  Warning  Failed     102s (x5 over 5m6s)   kubelet            spec.containers{mongo}: Error: ErrImagePull
  Warning  Failed     39s (x15 over 5m6s)   kubelet            spec.containers{mongo}: Error: ImagePullBackOff
  Normal   BackOff    14s (x17 over 5m6s)   kubelet            spec.containers{mongo}: Back-off pulling image "mongo"
# notice Messages columns, minikube cannot connect to server 'Error response from daemon'

# test minikube connection
minikube ssh "ping -c 3 google.com"
ping: google.com: Temporary failure in name resolution
ssh: Process exited with status 2

╰─❯ minikube ssh "sudo systemctl restart systemd-resolved"
Failed to restart systemd-resolved.service: Unit systemd-resolved.service not found.
ssh: Process exited with status 5
# DNS not inherited correctly

# stop, delete
╰─❯ minikube stop
✋  Stopping node "minikube"  ...
🛑  Powering off "minikube" via SSH ...
🛑  1 node stopped.

╰─❯ minikube delete
🔥  Deleting "minikube" in docker ...
🔥  Deleting container "minikube" ...
🔥  Removing /home/student/.minikube/machines/minikube ...
💀  Removed all traces of the "minikube" cluster.

# recreate with explicit DNS flags
╰─❯ minikube start --dns-proxy=true --extra-config=kubelet.resolv-conf=/etc/resolv.conf
😄  minikube v1.38.1 on Arch 
--snip--
🐳  Preparing Kubernetes v1.35.1 on Docker 29.2.1 ...
    ▪ kubelet.resolv-conf=/etc/resolv.conf
🔗  Configuring bridge CNI (Container Networking Interface) ...
--snip--
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default

╰─❯ minikube ssh "ping -c 3 google.com"
PING google.com (142.250.181.110) 56(84) bytes of data.
64 bytes from ncmrsa-ao-in-f14.1e100.net (142.250.181.110): icmp_seq=1 ttl=115 time=40.6 ms
64 bytes from fjr04s08-in-f14.1e100.net (142.250.181.110): icmp_seq=2 ttl=115 time=40.0 ms
64 bytes from ncmrsa-ao-in-f14.1e100.net (142.250.181.110): icmp_seq=3 ttl=115 time=40.4 ms

# retry deployment
╰─❯ kubectl create deployment mongo-depl --image=mongo
deployment.apps/mongo-depl created

╰─❯ kubectl get pod  # notice status                                 
NAME                         READY   STATUS              RESTARTS   AGE
mongo-depl-6c557896c-n9zxt   0/1     ContainerCreating   0          5s

╰─❯ kubectl get pod
NAME                         READY   STATUS    RESTARTS   AGE
mongo-depl-6c557896c-n9zxt   1/1     Running   0          112s

╰─❯ kubectl describe pod mongo-depl-6c557896c-n9zxt # success
Events:
 --snip-- Message
 --snip-- -------
 --snip-- Successfully assigned default/mongo-depl-6c557896c-n9zxt to minikube
 --snip-- spec.containers{mongo}: Successfully pulled image "mongo" in 1m43.249s (1m43.249s including waiting). Image size: 950089143 bytes.
 --snip-- spec.containers{mongo}: Pulling image "mongo"
 --snip-- spec.containers{mongo}: Container created
 --snip-- spec.containers{mongo}: Container started
 --snip-- spec.containers{mongo}: Successfully pulled image "mongo" in 1.319s (1.319s including waiting). Image size: 950089143 bytes.

╰─❯ kubectl logs mongo-depl-6c557896c-n9zxt
--snip-- 
"c":"NETWORK",  "id":23016,   "ctx":"listener","msg":"Waiting for connections"
--snip--
```
#### connect to container's terminal, pod crash
###### -i (interactive) -t (terminal)
```sh
╰─❯ kubectl exec -it mongo-depl-6c557896c-n9zxt -- bin/bash
error: Internal error occurred: unable to upgrade connection: container not found ("mongo")

╰─❯ kubectl get pod                                
NAME                         READY   STATUS             RESTARTS        AGE
mongo-depl-6c557896c-n9zxt   0/1     CrashLoopBackOff   6 (4m44s ago)   15m

# mongodb 5.0+ unstable with many CPUs, try 4.4
kubectl edit deployment mongo-depl
# editor will open, navigate 'spec' > containers > images: mongo
# edit to mongo:4.4, save, close

╰─❯ kubectl get pod                   
NAME                          READY   STATUS    RESTARTS   AGE
mongo-depl-68c7f5ccc5-zmhpv   1/1     Running   0          3m42s

╰─❯ kubectl exec -it mongo-depl-68c7f5ccc5-zmhpv -- bin/bash               
root@mongo-depl-68c7f5ccc5-zmhpv:/# 
```
#### 4- kubectl apply
###### instead of 'kubectl create deployment name image option1 option2'
```sh
# example
# kubectl apply -f config-file.yaml

╰─❯ kubectl apply -f /home/student/projects/git/devops-journey/kubernetes/nginx-deployment.yaml
deployment.apps/nginx-deployment created # notice 'created'

╰─❯ kubectl get pod                                                                             
NAME                                READY   STATUS              RESTARTS   AGE
nginx-depl-569bd7dcf9-q6dpv         1/1     Running             0          17m
nginx-deployment-78948d57cd-hkvg7   0/1     ContainerCreating   0          10s

# edit nginx-deployment.yaml 'replicas: 2' , then:
╰─❯ kubectl apply -f /home/student/projects/git/devops-journey/kubernetes/nginx-deployment.yaml 
deployment.apps/nginx-deployment configured # notice 'configured'

╰─❯ kubectl get pod # 2 pods
NAME                                READY   STATUS    RESTARTS   AGE
nginx-depl-569bd7dcf9-q6dpv         1/1     Running   0          20m
nginx-deployment-78948d57cd-cf2qj   1/1     Running   0          3s
nginx-deployment-78948d57cd-hkvg7   1/1     Running   0          3m16s

╰─❯ kubectl get deployment # '2/2'
NAME               READY   UP-TO-DATE   AVAILABLE   AGE
nginx-depl         1/1     1            1           20m
nginx-deployment   2/2     2            2           3m25s
```
## configuration files (deployment/service)
#### 1- nginx-deployment.yaml
###### can use yaml indentation validator eg: https://www.yamllint.com/
```yaml
apiVersion: apps/v1
kind: Deployment
metadata: # metadata contains labels
  name: nginx-deployment
  labels:
    app: nginx # deployment lable
spec: # of deployment / specs contain selectors
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template: # of pods
    metadata:
      labels:
        app: nginx # connect this pod to same deployment lable
    spec: # blue print of pod
      containers:
      - name: nginx
        image: nginx:1.16
        ports:
        - containerPort: 8080 # should match service target port
```
#### 2- nginx-service.yaml
###### can use yaml indentation validator eg: https://www.yamllint.com/
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
    - protocol: TCP
      port: 80
      targetPort: 8080
```
#### 3- apply
```sh
╰─❯ kubectl apply -f /home/student/projects/git/devops-journey/kubernetes/nginx-deployment.yaml 
deployment.apps/nginx-deployment created

╰─❯ kubectl apply -f /home/student/projects/git/devops-journey/kubernetes/nginx-service.yaml
service/nginx-service created
```
#### 4- verify
```sh
╰─❯ kubectl get pod                                                                         
NAME                                READY   STATUS    RESTARTS   AGE
nginx-deployment-76cb45c5b6-5hntt   1/1     Running   0          2m54s
nginx-deployment-76cb45c5b6-ksrt7   1/1     Running   0          2m54s

╰─❯ kubectl get service 
NAME            TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
kubernetes      ClusterIP   10.96.0.1        <none>        443/TCP   12h
nginx-service   ClusterIP   10.102.164.244   <none>        80/TCP    70s
```
#### 5- check connection success
```sh
╰─❯ kubectl describe service nginx-service         
Name:                     nginx-service
Namespace:                default
Labels:                   <none>
Annotations:              <none>
Selector:                 app=nginx
Type:                     ClusterIP
IP Family Policy:         SingleStack
IP Families:              IPv4
IP:                       10.102.164.244
IPs:                      10.102.164.244
Port:                     <unset>  80/TCP
TargetPort:               8080/TCP
Endpoints:                10.244.0.12:8080,10.244.0.13:8080 # note 
Session Affinity:         None
Internal Traffic Policy:  Cluster
Events:                   <none>
# note Endpoint IPs 10.244.0.13, 10.244.0.12


╰─❯ kubectl get pod -o wide  # option wide to show extra info             
NAME                                READY   STATUS    RESTARTS   AGE     IP            NODE       NOMINATED NODE   READINESS GATES
nginx-deployment-76cb45c5b6-5hntt   1/1     Running   0          5m25s   10.244.0.13   minikube   <none>           <none>
nginx-deployment-76cb45c5b6-ksrt7   1/1     Running   0          5m25s   10.244.0.12   minikube   <none>           <none>
# note IPs 10.244.0.13, 10.244.0.12
```
#### 6- create deployment status .yaml and save output to file
```sh
╰─❯ kubectl get deployment nginx-deployment -o yaml > nginx-deployment-result.yaml

╰─❯ find / -name "nginx-deployment-result.yaml" 2>/dev/null
/home/student/nginx-deployment-result.yaml
# moved to repo kubernetes folder. /kubernetes/nginx-deployment-result.yaml
```
## Mongodb & Mongo Express cluster
#### 1- Create mongo deployment *File was renamed finally to mongo.yaml*
```yaml
apiVersion: apps/v1
kind: Deployment
metadata: 
  name: mongodb-deployment
  labels:
    app: mongo
spec: 
  replicas: 1
  selector:
    matchLabels:
      app: mongo
  template:
    metadata:
      labels:
        app: mongo
    spec:
      containers:
      - name: mongo
        image: monogo:4.4 # works with my cpu
        ports:
        - containerPort: 27017
        env:
        - name: MONGO_INITDB_ROOT_USERNAME
          value: 
        - name: MONGO_INITDB_ROOT_PASSWORD
          value: 
```
#### 2- create secret.yaml
###### will reference this file's values in deployment yaml later
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mongo-secret
type: Opaque # default type (key-value)
data: # encode it in base64
  mongo-root-username: YWRtaW4= # see below how
  mongo-root-password: cGFzc3dvcmQ= # see below how
```
###### encode to base64
```sh
╰─❯ echo -n 'admin' | base64                                                    
YWRtaW4=
╰─❯ echo -n 'password' | base64
cGFzc3dvcmQ=
```
#### 3- apply the secret to kubectl
```sh
╰─❯ kubectl apply -f /home/student/projects/git/devops-journey/kubernetes/mongo-secret.yaml  
secret/mongo-secret created

╰─❯ kubectl get secret                                                                     
NAME           TYPE     DATA   AGE
mongo-secret   Opaque   2      11s
```
#### 4- update mongo deployment yaml env block with
```yaml
env:
- name: MONGO_INITDB_ROOT_USERNAME
  valueFrom:
    secretKeyRef:
      name: mongo-secret
      key: mongo-root-username 
- name: MONGO_INITDB_ROOT_PASSWORD
  valueFrom:
    secretKeyRef:
      name: mongo-secret
      key: mongo-root-password
```
#### 5- apply and check
```sh
╰─❯ kubectl apply -f /home/student/projects/git/devops-journey/kubernetes/mongo-deployment.yaml
deployment.apps/mongo-deployment created

╰─❯ kubectl get all                                                                            
NAME                                    READY   STATUS    RESTARTS   AGE
pod/mongo-deployment-576f9d7d46-prptb   1/1     Running   0          7s

NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   13h

NAME                               READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/mongo-deployment   1/1     1            1           7s

NAME                                          DESIRED   CURRENT   READY   AGE
replicaset.apps/mongo-deployment-576f9d7d46   1         1         1       7s
```
#### 6- create service
###### add the '---' in .yaml to indicate document separation
###### allowing both deployment and service in 1 same file
```yaml
apiVersion: apps/v1
kind: Deployment
metadata: 
  name: mongo-deployment
  labels:
    app: mongo
spec: 
 --snip--
              key: mongo-root-password
---  # syntax for document separation in yaml
apiVersion: v1
kind: Service
metadata:
  name: mongo-service
spec:
  selector:
    app: mongo
  ports:
    - protocol: TCP
      port: 27017
      targetPort: 27017
```
#### 7- apply service and confirm functionality
```sh
╰─❯ kubectl apply -f /home/student/projects/git/devops-journey/kubernetes/mongo-D_S.yaml       
deployment.apps/mongo-deployment unchanged
service/mongo-service created

╰─❯ kubectl get service                                                                 
NAME            TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)     AGE
kubernetes      ClusterIP   10.96.0.1        <none>        443/TCP     15h
mongo-service   ClusterIP   10.109.141.119   <none>        27017/TCP   31s

╰─❯ kubectl describe service mongo-service                 
Name:                     mongo-service
Namespace:                default
Labels:                   <none>
Annotations:              <none>
Selector:                 app=mongo
Type:                     ClusterIP
IP Family Policy:         SingleStack
IP Families:              IPv4
IP:                       10.109.141.119
IPs:                      10.109.141.119
Port:                     <unset>  27017/TCP
TargetPort:               27017/TCP
Endpoints:                10.244.0.20:27017
Session Affinity:         None
Internal Traffic Policy:  Cluster
Events:                   <none>

╰─❯ kubectl get pod -o wide               
NAME                                READY   STATUS    RESTARTS       AGE    IP            NODE       NOMINATED NODE   READINESS GATES
mongo-deployment-576f9d7d46-prptb   1/1     Running   1 (103m ago)   113m   10.244.0.20   minikube   <none>           <none>

# Endpoints and IP match!
```
#### 8- mongo express deploy, update secrets, config map
###### mongo-express.yaml key differences
```yaml
apiVersion: apps/v1
kind: Deployment
--snip--
        env:
        - name: ME_CONFIG_MONGODB_SERVER
          valueFrom:
            configMapKeyRef:
              name: mongo-configmap
              key: database_url
        - name: ME_CONFIG_MONGODB_ADMINUSERNAME
          valueFrom:
            secretKeyRef:
              name: mongo-secret
              key: mongo-root-username 
        - name: ME_CONFIG_MONGODB_ADMINPASSWORD
          valueFrom:
            secretKeyRef:
              name: mongo-secret
              key: mongo-root-password
        - name: ME_CONFIG_BASICAUTH_USERNAME
          valueFrom:
            secretKeyRef:
              name: mongo-secret
              key: mongo-user-username
        - name: ME_CONFIG_BASICAUTH_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mongo-secret
              key: mongo-user-password
```
###### mongo-secret.yaml updated block
```yaml
type: Opaque # default type (key-value)
data: # encode it in base64
  mongo-root-username: YWRtaW4=
  mongo-root-password: cGFzc3dvcmQ=
  mongo-user-username: YWRtaW4=
  mongo-user-password: cGFzc3dvcmQ=
```
###### mongo-configmap.yaml
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: mongo-configmap
data:
  database_url: mongo-service
```
#### 9- apply
```sh
╰─❯ kubectl apply -f /home/student/projects/git/devops-journey/kubernetes/mongo-secret.yaml 
secret/mongo-secret configured

╰─❯ kubectl apply -f /home/student/projects/git/devops-journey/kubernetes/mongo-configmap.yaml 
configmap/mongo-configmap created

╰─❯ kubectl apply -f /home/student/projects/git/devops-journey/kubernetes/mongo-express.yaml  
deployment.apps/mongo-express created

╰─❯ kubectl get pod
NAME                                READY   STATUS    RESTARTS       AGE
mongo-deployment-576f9d7d46-prptb   1/1     Running   1 (122m ago)   132m
mongo-express-79787d5b46-vsljx      1/1     Running   0              40s
```
#### 10- create express service, assign external ip with minikube
###### mongo-express.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata: 
  name: mongo-express
--snip--

---
apiVersion: v1
kind: Service
metadata:
  name: mongo-express-service
spec:
  selector:
    app: mongo-express
  type: LoadBalancer   # enable external service
  ports:
    - protocol: TCP
      port: 8081
      targetPort: 8081
      nodePort: 30000   # open port for external ip
```
```sh
╰─❯ kubectl apply -f /home/student/projects/git/devops-journey/kubernetes/mongo-express.yaml
deployment.apps/mongo-express unchanged
service/mongo-express-service created

╰─❯ kubectl get service                                                                     
NAME                    TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
kubernetes              ClusterIP      10.96.0.1        <none>        443/TCP          16h
mongo-express-service   LoadBalancer   10.109.153.154   <pending>     8081:30000/TCP   13s
mongo-service           ClusterIP      10.109.141.119   <none>        27017/TCP        30m

# External IP pending, get minikube to assign one

╰─❯ minikube service mongo-express-service                                             
┌───────────┬───────────────────────┬─────────────┬───────────────────────────┐
│ NAMESPACE │         NAME          │ TARGET PORT │            URL            │
├───────────┼───────────────────────┼─────────────┼───────────────────────────┤
│ default   │ mongo-express-service │ 8081        │ http://192.168.49.2:30000 │
└───────────┴───────────────────────┴─────────────┴───────────────────────────┘
🎉  Opening service default/mongo-express-service in default browser...
# browser opens with mongo express

# workflow:
# express external service > express pod > mongo internal service > mongo pod
```
## Namespace
#### Create eg: configMap in non-default Namespace
```sh
╰─❯ kubectl apply -f mysql.configmap.yaml --namespace=my-namespace
```
#### or Assign in configmap.yaml instead of useing flag
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: mongo-configmap
  namespace: my-namespace
data:
  database_url: mongo-service
```
###### to view it, must specify namespace in kubectl get configmap -n
```sh
╰─❯ kubectl get configmap -n my-namespace
```
#### change active namespace
###### to remove need to specify namespace each time (change from default to specific)
###### use kubens
```sh
# install, fzf (fuzzy finder) is optional
╰─❯ sudo pacman -Sy kubens fzf

╰─❯ kubens my-namespace
✔ Active namespace is "my-namespace".

# now can execute commands without specifying 'my-namespace' 
```
## Ingress
#### ingress.yaml
###### http, not https
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp-ingress
spec:
  rules:
  - host: myapp.com
    http:
      paths:
      - path: /
        backend:
          service:
            name: myapp-internal-service # another internal service
            port:
              number: 8080
```
###### Workflow: ingress controller pod > my-app ingress > my-app service > my-app pod
#### 1- install ingress controller in minikube
###### uses Nginx implementation, list of different implementations:
- https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/
```sh
╰─❯ minikube addons enable ingress        
💡  ingress is an addon maintained by Kubernetes. For any concerns contact minikube on GitHub.
You can view the list of minikube maintainers at: https://github.com/kubernetes/minikube/blob/master/OWNERS
    ▪ Using image registry.k8s.io/ingress-nginx/controller:v1.14.3
    ▪ Using image registry.k8s.io/ingress-nginx/kube-webhook-certgen:v1.6.7
    ▪ Using image registry.k8s.io/ingress-nginx/kube-webhook-certgen:v1.6.7
🔎  Verifying ingress addon...
🌟  The 'ingress' addon is enabled

╰─❯ kubectl get namespace         
NAME              STATUS   AGE
default           Active   17h
ingress-nginx     Active   5m16s
kube-node-lease   Active   17h
kube-public       Active   17h
kube-system       Active   17h


╰─❯ kubens ingress-nginx
✔ Active namespace is "ingress-nginx".

╰─❯ kubectl get pod
NAME                                        READY   STATUS      RESTARTS   AGE
ingress-nginx-admission-create-r4jcw        0/1     Completed   0          4m10s
ingress-nginx-admission-patch-rr5kb         0/1     Completed   1          4m10s
ingress-nginx-controller-596f8778bc-lzp49   1/1     Running     0          4m10s
```
#### 2- create ingress rule
###### first must activate 'kubernetes dashboard' through minikube
```sh
╰─❯ minikube addons enable dashboard
💡  dashboard is an addon maintained by Kubernetes. For any concerns contact minikube on GitHub.
You can view the list of minikube maintainers at: https://github.com/kubernetes/minikube/blob/master/OWNERS
    ▪ Using image docker.io/kubernetesui/metrics-scraper:v1.0.8
    ▪ Using image docker.io/kubernetesui/dashboard:v2.7.0
💡  Some dashboard features require the metrics-server addon. To enable all features please run:

	minikube addons enable metrics-server

🌟  The 'dashboard' addon is enabled

╰─❯ kubectl get ns
NAME                   STATUS   AGE
default                Active   17h
ingress-nginx          Active   13m
kube-node-lease        Active   17h
kube-public            Active   17h
kube-system            Active   17h
kubernetes-dashboard   Active   33s

╰─❯ kubectl get all -n kubernetes-dashboard
NAME                                             READY   STATUS    RESTARTS   AGE
pod/dashboard-metrics-scraper-5565989548-ksn9l   1/1     Running   0          74s
pod/kubernetes-dashboard-b84665fb8-xvg9t         1/1     Running   0          74s

NAME                                TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/dashboard-metrics-scraper   ClusterIP   10.105.219.113   <none>        8000/TCP   74s
service/kubernetes-dashboard        ClusterIP   10.104.70.7      <none>        80/TCP     74s

NAME                                        READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/dashboard-metrics-scraper   1/1     1            1           74s
deployment.apps/kubernetes-dashboard        1/1     1            1           74s

NAME                                                   DESIRED   CURRENT   READY   AGE
replicaset.apps/dashboard-metrics-scraper-5565989548   1         1         1       74s
replicaset.apps/kubernetes-dashboard-b84665fb8         1         1         1       74s

# kubernetes-dashboard is internal (because Type is ClusterIP)
```
###### create rule
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: dashboard-ingress
  namespace: kubernetes-dashboard
spec:
  rules:
  - host: dashboard.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: kubernetes-dashboard
            port: 
              number: 80
# forwards all requests directed to dashboard.com to kubernetes-dashboard service
```
###### apply
```sh
╰─❯ kubectl apply -f /home/student/projects/git/devops-journey/kubernetes/dashboard-ingress.yaml
ingress.networking.k8s.io/dashboard-ingress created

╰─❯ kubectl get ingress -n kubernetes-dashboard                                                 
NAME                CLASS   HOSTS           ADDRESS        PORTS   AGE
dashboard-ingress   nginx   dashboard.com   192.168.49.2   80      68s

# Addr 192.168.49.2
```
###### to access external ip locally, must add ext ip to /etc/hosts
```sh
minikube ip 
192.168.49.2 # same as above

# add 192.168.49.2 dashboard.com to /etc/hosts
sudo vim /etc/hosts
# or
echo "192.168.49.2 dashboard.com" | sudo tee -a /etc/hosts
```
###### navigate to dashboard.com  ! kubernetes dashboard visible  !
#### 3- default backend - check 'Default backend:  <default>'
```sh
╰─❯ kubectl describe ingress dashboard-ingress -n kubernetes-dashboard
Name:             dashboard-ingress
Labels:           <none>
Namespace:        kubernetes-dashboard
Address:          192.168.49.2
Ingress Class:    nginx
Default backend:  <default>
Rules:
  Host           Path  Backends
  ----           ----  --------
  dashboard.com  
                 /   kubernetes-dashboard:80 (10.244.0.25:9090)
Annotations:     <none>
Events:
  Type    Reason  Age                From                      Message
  ----    ------  ----               ----                      -------
  Normal  Sync    10m (x2 over 11m)  nginx-ingress-controller  Scheduled for sync
```
###### create internal service instead of <default>
```yaml
apiVersion: v1
kind: Service
metadata:
  name: default-http-backend
spec:
  selector:
    app: default-response-app
  ports:
  - protocol: TCP
    port: 80
    targetPort: 8080
```
#### example of using multiple paths
```yaml
spec:
  rules:
  - host: example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: dashboard
            port: 
              number: 80
      - path: /analytics
        pathType: Prefix
        backend:
          service:
            name: analytics-service
            port: 
              number: 3000
      - path: /shopping
        pathType: Prefix
        backend:
          service:
            name: shopping-service
            port: 
              number: 8080
```
#### example of using sub-domains
```yaml
spec:
  rules:
  - host: example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: dashboard
            port: 
              number: 80
  - host: analytics.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: analytics-service
            port: 
              number: 3000
  - host: shopping.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: shopping.service
            port: 
              number: 8080
```
#### example of using HTTPS
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: tls-example-ingress
spec:
  tls:
  - hosts: 
    - example.com
    secretName: example-secret-tls # ref of secret created in cluster that has cert.
  rules:
  -host: example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: example-internal-service
            port: 
              number: 8080
```
###### tls secret yaml - must be on same namespace of ingress
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: example-secret-tls
  namespace: default
data:
  tls.crt: base64 encoded cert
  tls.key: base64 encoded key
type: kubernetes.io/tls
```
###### creating crt and key, -w 0 (wrap, to be on 1 continuous line)
```sh
╰─❯ echo server.crt | base64 -w 0
c2VydmVyLmNydAo=%                                                                                                                             
╰─❯ echo server.key | base64 -w 0                        
c2VydmVyLmtleQo=%                   
```
