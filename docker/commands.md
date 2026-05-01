#### pull image from hub.docker.com (pulls latest version)
```sh 
docker pull redis
```
#### pull specific image version
```sh
docker pull redis:8.4.2
```
#### view current images on disk
```sh
docker images

IMAGE              ID             DISK USAGE   CONTENT SIZE   EXTRA
archlinux:latest   5ba8bb318666        560MB          138MB        
redis:8.4.2        3c4df018ee3c        202MB         54.5MB        
redis:8.6.2        832d7785830f        204MB         55.3MB        
redis:latest       832d7785830f        204MB         55.3MB        

```
#### view docker running process
```sh
docker ps
```
#### view docker processes including those that have exited
```sh
docker ps -a

CONTAINER ID   IMAGE              COMMAND           CREATED              STATUS                          PORTS     NAMES
369968f55bb4   archlinux:latest   "/usr/bin/bash"   About a minute ago   Exited (0) About a minute ago             pensive_gauss
c1fde604caca   archlinux          "/usr/bin/bash"   2 minutes ago        Exited (0) 2 minutes ago                  upbeat_babbage
```