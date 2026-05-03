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
