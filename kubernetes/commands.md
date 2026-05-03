##### start minikube
```sh
╰─❯ minikube start
``` 

#### status of nodes
```sh
╰─❯ kubectl get nodes
NAME       STATUS   ROLES           AGE    VERSION
minikube   Ready    control-plane   6m9s   v1.35.1
```
#### get services 
###### both kubectl get service or get services work
```sh
╰─❯ kubectl get services
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   5h30m
```
#### create deployment (deployment is abstraction layer over the pods)
```sh
╰─❯ kubectl create deployment nginx-depl --image=nginx
deployment.apps/nginx-depl created

╰─❯ kubectl get deployment
NAME         READY   UP-TO-DATE   AVAILABLE   AGE
nginx-depl   1/1     1            1           73s

╰─❯ kubectl get pod       
NAME                          READY   STATUS    RESTARTS   AGE
nginx-depl-569bd7dcf9-ldnl4   1/1     Running   0          94s
# prefix of deployment 'nginx-depl' - replica set id '569bd7dcf9' - pod id 'ldnl4'
```
#### get replicaset
###### manages replicas of a pod
```sh
╰─❯ kubectl get replicaset
NAME                    DESIRED   CURRENT   READY   AGE
nginx-depl-569bd7dcf9   1         1         1       13h
```
#### edit deployment
```sh
╰─❯ kubectl edit deployment nginx-depl
# editor will open, navigate 'spec' > containers > images: nginx:1
# edit to nginx:1.16, save, close
╰─❯ kubectl get pod
NAME                          READY   STATUS    RESTARTS   AGE
nginx-depl-74499d8d69-6jpwz   1/1     Running   0          37s
# old pod was terminated '569bd7dcf9-ldnl4'
# new pod created containing 'nginx:1.16'

# old replicaset has no pods, new one has.
kubectl get replicaset
NAME                    DESIRED   CURRENT   READY   AGE
nginx-depl-569bd7dcf9   0         0         0       13h
nginx-depl-74499d8d69   1         1         1       4m8s
```

#### checking logs/describe, fixing DNS resolution, minikube stop/delete
```sh
╰─❯ kubectl create deployment mongo-depl --image=mongo
deployment.apps/mongo-depl created

╰─❯ kubectl get pod  # notice status                                 
NAME                         READY   STATUS              RESTARTS   AGE
mongo-depl-6c557896c-n9zxt   0/1     ContainerCreating   0          5s

╰─❯ kubectl get pod
NAME                         READY   STATUS    RESTARTS   AGE
mongo-depl-6c557896c-n9zxt   1/1     Running   0          112s

╰─❯ kubectl describe pod mongo-depl-6c557896c-n9zxt
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
#### connect to container's terminal bin/bash
###### -i (interactive) -t (terminal)
```sh
╰─❯ kubectl get pod                   
NAME                          READY   STATUS    RESTARTS   AGE
mongo-depl-68c7f5ccc5-zmhpv   1/1     Running   0          3m42s

╰─❯ kubectl exec -it mongo-depl-68c7f5ccc5-zmhpv -- bin/bash               
root@mongo-depl-68c7f5ccc5-zmhpv:/# 
```
#### delete deployment/pod
```sh
╰─❯ kubectl delete deployment mongo-depl           
deployment.apps "mongo-depl" deleted from default namespace
```
#### kubectl apply
###### instead of 'kubectl create deployment name image option1 option2'
```sh
╰─❯ kubectl apply -f config-file.yaml
```
#### get pod wide view
###### -o (option) wide (view)
```sh
╰─❯ kubectl get pod -o wide 
NAME                                READY   STATUS    RESTARTS   AGE     IP            NODE       NOMINATED NODE   READINESS GATES
nginx-deployment-76cb45c5b6-5hntt   1/1     Running   0          5m25s   10.244.0.13   minikube   <none>           <none>
nginx-deployment-76cb45c5b6-ksrt7   1/1     Running   0          5m25s   10.244.0.12   minikube   <none>           <none>
```
#### create deployment status .yaml and save output to file
###### can be used to automate creating deployments, after cleaning
```sh
╰─❯ kubectl get deployment nginx-deployment -o yaml > nginx-deployment-result.yaml

# easy find
╰─❯ find / -name "nginx-deployment-result.yaml" 2>/dev/null
```