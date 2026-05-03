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
