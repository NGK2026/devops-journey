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
#### install kube-prometheus-stack
```sh
╰─❯ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

╰─❯ helm install prometheus-stack prometheus-community/kube-prometheus-stack

╰─❯ helm list     
NAME            	NAMESPACE	REVISION	UPDATED                                 	STATUS  	CHART                       	APP VERSION
mysql           	default  	1       	2026-05-22 22:24:41.289926032 +0300 EEST	deployed	mysql-1.6.9                 	5.7.30     
nginx-bitnami   	default  	1       	2026-05-22 22:37:02.45329212 +0300 EEST 	deployed	nginx-24.0.2                	1.31.1     
prometheus-stack	default  	1       	2026-05-22 23:30:07.386223089 +0300 EEST	deployed	kube-prometheus-stack-85.2.2	v0.90.1 

╰─❯ kubectl get svc                
NAME                                        TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
alertmanager-operated                       ClusterIP      None             <none>        9093/TCP,9094/TCP,9094/UDP   11m
kubernetes                                  ClusterIP      10.96.0.1        <none>        443/TCP                      23h
mysql                                       ClusterIP      10.98.171.238    <none>        3306/TCP                     77m
nginx-bitnami                               LoadBalancer   10.99.34.96      <pending>     80:32601/TCP,443:30137/TCP   65m
prometheus-operated                         ClusterIP      None             <none>        9090/TCP                     11m
prometheus-stack-grafana                    ClusterIP      10.97.149.190    <none>        80/TCP                       11m
prometheus-stack-kube-prom-alertmanager     ClusterIP      10.102.72.45     <none>        9093/TCP,8080/TCP            11m
prometheus-stack-kube-prom-operator         ClusterIP      10.100.59.149    <none>        443/TCP                      11m
prometheus-stack-kube-prom-prometheus       ClusterIP      10.110.212.113   <none>        9090/TCP,8080/TCP            11m
prometheus-stack-kube-state-metrics         ClusterIP      10.98.97.181     <none>        8080/TCP                     11m
prometheus-stack-prometheus-node-exporter   ClusterIP      10.110.6.102     <none>        9100/TCP                     11m
```
#### edit grafana monitoring
```sh
╰─❯ kubectl edit svc prometheus-stack-grafana
# change type: to NodePort
# add nodePort:30001
```
```yml
  ports:
  - name: http-web
    port: 80
    protocol: TCP 
    targetPort: grafana
    nodePort: 30001
  selector:
    app.kubernetes.io/instance: prometheus-stack
    app.kubernetes.io/name: grafana
  sessionAffinity: None
  type: NodePort
```
```sh
╰─❯ kubectl get svc                          
NAME                                        TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
prometheus-stack-grafana                    NodePort       10.97.149.190    <none>        80:30001/TCP                 19m
```