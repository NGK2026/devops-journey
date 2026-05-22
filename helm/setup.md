#### Add charts and install mysql & nginx
```sh
╰─❯ minikube start

╰─❯ helm repo add stable https://charts.helm.sh/stable

╰─❯ helm install mysql stable/mysql

╰─❯ helm repo add bitnami https://charts.bitnami.com/bitnami

╰─❯ helm install nginx-bitnami bitnami/nginx

╰─❯ kubectl get po            
NAME                             READY   STATUS    RESTARTS   AGE
mysql-7cdb788b98-22r2z           1/1     Running   0          16m
nginx-bitnami-76db679599-hlltp   1/1     Running   0          3m44s

╰─❯ helm list              
NAME         	NAMESPACE	REVISION	UPDATED                                 	STATUS  	CHART       	APP VERSION
mysql        	default  	1       	2026-05-22 22:24:41.289926032 +0300 EEST	deployed	mysql-1.6.9 	5.7.30     
nginx-bitnami	default  	1       	2026-05-22 22:37:02.45329212 +0300 EEST 	deployed	nginx-24.0.2	1.31.1     

```