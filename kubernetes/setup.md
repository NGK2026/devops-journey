### Layers of abstraction
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
