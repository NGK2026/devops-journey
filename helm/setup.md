## Table of Contents (for setup.md)

- [Add charts and install mysql & nginx](#add-charts-and-install-mysql--nginx)
- [install kube-prometheus-stack](#install-kube-prometheus-stack)
- [edit grafana monitoring](#edit-grafana-monitoring)
- [change graphana user/pass](#change-graphana-userpass)
- [set up the service values automatically](#set-up the-service-values-automatically)
- [configure own cluster](#configure-own-cluster)
- [generate yaml then add to cluster](#generate-yaml-then-add-to-cluster)

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

╰─❯ minikube ip     
192.168.49.2

# visit 192.168.49.2:30001
```
#### change graphana user/pass
- check values
```sh
╰─❯ helm show values prometheus-community/kube-prometheus-stack > values.yaml
# or
╰─❯ helm show values prometheus-community/kube-prometheus-stack | grep -i password
# adminPassword: strongpassword
--snip

╰─❯ helm upgrade prometheus-stack prometheus-community/kube-prometheus-stack --set grafana.adminPassword=admin
level=WARN msg="upgrade failed" name=prometheus-stack error="conflict occurred while applying object default/prometheus-stack-grafana /v1, Kind=Service: Apply failed with 1 conflict: conflict with \"kubectl-edit\" using v1: .spec.type"
Error: UPGRADE FAILED: conflict occurred while applying object default/prometheus-stack-grafana /v1,
Kind=Service: Apply failed with 1 conflict: conflict with "kubectl-edit" using v1: .spec.type

# .spec.type is the service we edited
╰─❯ kubectl delete svc prometheus-stack-grafana

╰─❯ helm upgrade prometheus-stack prometheus-community/kube-prometheus-stack --set grafana.adminPassword=admin

# re-edit service port type and number as above
kubectl edit svc prometheus-stack-grafana

╰─❯ kubectl get svc
NAME                                        TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
prometheus-stack-grafana                    NodePort       10.109.154.126   <none>        80:30001/TCP                 3m48s
```
#### set up the service values automatically
```sh
# first delete the configured service and regenerate with desired password
╰─❯ kubectl delete svc prometheus-stack-grafana

╰─❯ helm upgrade prometheus-stack prometheus-community/kube-prometheus-stack --set grafana.adminPassword=admin

╰─❯ kubectl get svc # back to cluster ip and port not 30001
NAME                                        TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
prometheus-stack-grafana                    ClusterIP      10.100.59.230    <none>        80/TCP                       8s
```
- edit service.yaml we created with parameters and values we want
```yaml
  adminUser: admin
  # adminPassword: strongpassword
#  -- snip
  service:
    portName: http-web
    ipFamilies: []
    ipFamilyPolicy: ""
```
- to 
```yaml
  adminUser: admin
  adminPassword: admin
# snip--
  service:
    portName: http-web
    ipFamilies: []
    ipFamilyPolicy: ""
    type: NodePort
    nodePort: 30001
```
- then apply with
```sh
╰─❯ helm upgrade prometheus-stack prometheus-community/kube-prometheus-stack --values=values.yaml     
# OR #
╰─❯ helm upgrade prometheus-stack prometheus-community/kube-prometheus-stack \                                 
--set grafana.adminPassword=admin \
--set grafana.service.type=NodePort \ 
--set grafana.service.nodePort=30001

╰─❯ kubectl get svc                                                                              
NAME                                        TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
prometheus-stack-grafana                    NodePort       10.102.145.164   <none>        80:30001/TCP                 9s
```
#### configure own cluster
```sh
╰─❯ mkdir my-cluster-config && cd my-cluster-config

# pull
╰─❯ helm pull prometheus-community/kube-prometheus-stack --untar=true
╰─❯ helm pull stable/mysql --untar=true

# create myvalues.yaml in ./kube-prometheus-stack/
# password = admin
# type: nodeport, nodeport 30001

# install with myvalues.yaml from local folder
╭─ ~/projects/git/devops-journey/helm/my-cluster-config                                           󱃾 minikube
╰─❯ helm install prometheus-stack ./kube-prometheus-stack --values=./kube-prometheus-stack/myvalues.yaml

╰─❯ helm install mysql ./mysql 

# or install first then upgrade after
╰─❯ helm install prometheus-stack ./kube-prometheus-stack
╰─❯ cd kube-prometheus-stack
# . for here
╰─❯ helm upgrade prometheus-stack --values=myvalues.yaml .

# list
╰─❯ helm list                   
NAME            	NAMESPACE	REVISION	UPDATED                                 	STATUS  	CHART                       	APP VERSION
mysql           	default  	1       	2026-05-24 15:27:26.472445765 +0300 EEST	deployed	mysql-1.6.9                 	5.7.30     
prometheus-stack	default  	1       	2026-05-24 15:26:21.446303164 +0300 EEST	deployed	kube-prometheus-stack-85.2.2	v0.90.1    
```
#### generate yaml then add to cluster
- helm template
```sh
╰─❯ helm template prometheus-stack ./kube-prometheus-stack/ \
  --values=./kube-prometheus-stack/myvalues.yaml > prometheus-stack.yaml

╰─❯ kubectl apply -f prometheus-stack.yaml 

╭─ ~/projects/git/devops-journey/helm/my-cluster-config
╰─❯ kubectl get po                        
NAME                                                     READY   STATUS      RESTARTS   AGE
alertmanager-prometheus-stack-kube-prom-alertmanager-0   2/2     Running     0          36s
prometheus-prometheus-stack-kube-prom-prometheus-0       2/2     Running     0          36s
prometheus-stack-grafana-5998fbdc85-qx2kl                3/3     Running     0          37s
prometheus-stack-kube-prom-admission-create-lljmr        0/1     Completed   0          26s
prometheus-stack-kube-prom-admission-patch-x4tpj         0/1     Completed   0          26s
prometheus-stack-kube-prom-operator-787b669484-rmdgc     1/1     Running     0          37s
prometheus-stack-kube-state-metrics-7b9d949668-vpt7c     1/1     Running     0          37s
prometheus-stack-prometheus-node-exporter-wmr7k          1/1     Running     0          37s

╭─ ~/projects/git/devops-journey/helm/my-cluster-config 
╰─❯ kubectl get svc    
NAME                                        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
alertmanager-operated                       ClusterIP   None             <none>        9093/TCP,9094/TCP,9094/UDP   55s
kubernetes                                  ClusterIP   10.96.0.1        <none>        443/TCP                      2d15h
prometheus-operated                         ClusterIP   None             <none>        9090/TCP                     55s
prometheus-stack-grafana                    NodePort    10.102.34.112    <none>        80:30001/TCP                 56s
prometheus-stack-kube-prom-alertmanager     ClusterIP   10.105.147.239   <none>        9093/TCP,8080/TCP            56s
prometheus-stack-kube-prom-operator         ClusterIP   10.100.176.141   <none>        443/TCP                      56s
prometheus-stack-kube-prom-prometheus       ClusterIP   10.98.237.40     <none>        9090/TCP,8080/TCP            56s
prometheus-stack-kube-state-metrics         ClusterIP   10.107.127.66    <none>        8080/TCP                     56s
prometheus-stack-prometheus-node-exporter   ClusterIP   10.111.56.152    <none>        9100/TCP                     56s
```