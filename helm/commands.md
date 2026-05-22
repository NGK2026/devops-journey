#### repos
```sh
╰─❯ helm repo add stable https://charts.helm.sh/stable

╰─❯ helm repo update

╰─❯ helm repo list                                          
NAME   	URL                               
stable              	https://charts.helm.sh/stable                     
bitnami             	https://charts.bitnami.com/bitnami                
prometheus-community	https://prometheus-community.github.io/helm-charts


╰─❯ helm search repo mysql # or eg: bitnami/  # or eg: bitnami/mysql
NAME                                          	CHART VERSION	APP VERSION	DESCRIPTION                                       
bitnami/mysql                                 	14.0.3       	9.4.0      	MySQL is a fast, reliable, scalable, and easy t...
prometheus-community/prometheus-mysql-exporter	2.13.1       	v0.19.0    	A Helm chart for prometheus mysql exporter with...
stable/mysql                                  	1.6.9        	5.7.30     	DEPRECATED - Fast, reliable, scalable, and easy...
stable/mysqldump                              	2.6.2        	2.4.1      	DEPRECATED! - A Helm chart to help backup MySQL...
stable/prometheus-mysql-exporter              	0.7.1        	v0.11.0    	DEPRECATED A Helm chart for prometheus mysql ex...
bitnami/phpmyadmin                            	20.0.0       	5.2.2      	phpMyAdmin is a free software tool written in P...
```
#### kubectl get ..
```sh
╰─❯ helm list

╰─❯ kubectl get po 

╰─❯ kubectl get svc
```