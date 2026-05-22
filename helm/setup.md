#### Add charts and install mysql & nginx
```sh
╰─❯ minikube start

╰─❯ helm repo add stable https://charts.helm.sh/stable

╰─❯ helm install mysql stable/mysql

╰─❯ helm repo add bitnami https://charts.bitnami.com/bitnami

╰─❯ helm install my-release bitnami/nginx

╰─❯ kubectl get po            
NAME                             READY   STATUS    RESTARTS   AGE
mysql-7cdb788b98-22r2z           1/1     Running   0          16m
nginx-bitnami-76db679599-hlltp   1/1     Running   0          3m44s

```