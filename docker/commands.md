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
#### run image -i (interactive) -t (terminal)
```sh
docker run -it archlinux

[root@38ff111ce364 /]# 
```
#### view docker running process
###### if not specify a name using the --name flag when starting a container, Docker automatically generates one.
```sh
docker ps

CONTAINER ID   IMAGE       COMMAND           CREATED              STATUS              PORTS     NAMES
38ff111ce364   archlinux   "/usr/bin/bash"   About a minute ago   Up About a minute             flamboyant_mcnulty

```
#### view docker processes including those that have exited -a (all)
```sh
docker ps -a

CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS                      PORTS      NAMES
042344813f99   redis              "docker-entrypoint.s…"   9 seconds ago    Up 9 seconds                6379/tcp   relaxed_pike
38ff111ce364   archlinux          "/usr/bin/bash"          5 minutes ago    Up 5 minutes                           flamboyant_mcnulty
369968f55bb4   archlinux:latest   "/usr/bin/bash"          10 minutes ago   Exited (0) 10 minutes ago              pensive_gauss
c1fde604caca   archlinux          "/usr/bin/bash"          10 minutes ago   Exited (0) 10 minutes ago              upbeat_babbage


```