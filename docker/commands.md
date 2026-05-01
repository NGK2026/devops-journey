#### pull image from hub.docker.com (pulls latest version)
```sh 
╰─❯ docker pull redis
```
#### pull specific image version
```sh
╰─❯ docker pull redis:8.4.2
```
#### pull and run in 1 command
###### version is optional like previous commands
```sh
╰─❯ docker run nameOfNewImage:version
```
#### view current images on disk
```sh
╰─❯ docker images

IMAGE              ID             DISK USAGE   CONTENT SIZE   EXTRA
archlinux:latest   5ba8bb318666        560MB          138MB        
redis:8.4.2        3c4df018ee3c        202MB         54.5MB        
redis:8.6.2        832d7785830f        204MB         55.3MB        
redis:latest       832d7785830f        204MB         55.3MB        

```
#### run image -i (interactive) -t (terminal)
```sh
╰─❯ docker run -it archlinux

[root@38ff111ce364 /]# 
```
#### run image in -d (detached) mode
###### runs in the background, outputs only id of container
```sh
╰─❯ docker run -d redis     
cbe9bb0b4ab08ef8c07c45efbde881625ef46cca108db3e0948c9de5f16cb489
                                           
╰─❯ 
```
#### run image with specified name
```sh
╰─❯ docker run -d --name arch-latest archlinux

╰─❯ docker ps
CONTAINER ID   IMAGE         COMMAND                  CREATED         STATUS         PORTS                                         NAMES
d57ab89b5816   archlinux     "/usr/bin/bash"          9 seconds ago   Up 8 seconds                                                 arch-latest

```
#### view docker running process (notice id of -d container)
###### if not specify a name using the --name flag when starting a container, Docker automatically generates one.
```sh
╰─❯ docker ps

CONTAINER ID   IMAGE       COMMAND                  CREATED          STATUS         PORTS      NAMES
cbe9bb0b4ab0   redis       "docker-entrypoint.s…"   10 seconds ago   Up 9 seconds   6379/tcp   hardcore_chandrasekhar
38ff111ce364   archlinux   "/usr/bin/bash"          9 minutes ago    Up 9 minutes              flamboyant_mcnulty
```
#### view docker processes including those that have exited -a (all)
```sh
╰─❯ docker ps -a

CONTAINER ID   IMAGE              COMMAND                  CREATED          STATUS                      PORTS      NAMES
cbe9bb0b4ab0   redis              "docker-entrypoint.s…"   17 seconds ago   Up 16 seconds               6379/tcp   hardcore_chandrasekhar
042344813f99   redis              "docker-entrypoint.s…"   4 minutes ago    Exited (0) 2 minutes ago               relaxed_pike
38ff111ce364   archlinux          "/usr/bin/bash"          9 minutes ago    Up 9 minutes                           flamboyant_mcnulty
369968f55bb4   archlinux:latest   "/usr/bin/bash"          14 minutes ago   Exited (0) 14 minutes ago              pensive_gauss
c1fde604caca   archlinux          "/usr/bin/bash"          14 minutes ago   Exited (0) 14 minutes ago              upbeat_babbage
```
#### restart container - use container ID (stop / start)
```sh
╰─❯ docker stop cbe9bb0b4ab0
cbe9bb0b4ab0

╰─❯ docker ps
CONTAINER ID   IMAGE       COMMAND           CREATED          STATUS          PORTS     NAMES
38ff111ce364   archlinux   "/usr/bin/bash"   14 minutes ago   Up 14 minutes             flamboyant_mcnulty

╰─❯ docker start cbe9bb0b4ab0
cbe9bb0b4ab0

╰─❯ docker ps
CONTAINER ID   IMAGE       COMMAND                  CREATED          STATUS          PORTS      NAMES
cbe9bb0b4ab0   redis       "docker-entrypoint.s…"   6 minutes ago    Up 2 seconds    6379/tcp   hardcore_chandrasekhar
38ff111ce364   archlinux   "/usr/bin/bash"          16 minutes ago   Up 16 minutes              flamboyant_mcnulty
```
#### bind different host port to container port
###### if running multiple containers with same port
```sh
╰─❯ docker ps
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS          PORTS      NAMES
aa0be3d8cf9d   redis:8.4.2   "docker-entrypoint.s…"   4 seconds ago    Up 3 seconds    6379/tcp   silly_wescoff
cbe9bb0b4ab0   redis         "docker-entrypoint.s…"   14 minutes ago   Up 7 minutes    6379/tcp   hardcore_chandrasekhar

╰─❯ docker stop aa0be3d8cf9d
aa0be3d8cf9d

# -p'hostport':'container default port', can add -d to run detached
# enables both ipv4 and ipv6
# ipv4 external network, use: 0.0.0.0:6000:6379 .. for ipv4 local access only, use: 127.0.0.1:6000:6379 
╰─❯ docker run -d -p6000:6379 redis:8.4.2

╰─❯ docker ps
1a482cbac104   redis:8.4.2   "docker-entrypoint.s…"   2 seconds ago    Up 2 seconds    0.0.0.0:6000->6379/tcp, [::]:6000->6379/tcp   jolly_bose
cbe9bb0b4ab0   redis         "docker-entrypoint.s…"   22 minutes ago   Up 16 minutes   6379/tcp                                      hardcore_chandrasekhar
```
#### stop all containers
##### ps -q returns numeric IDs. $(...) passes output to initial command
```sh
╰─❯ docker stop $(docker ps -q)
1a482cbac104
cbe9bb0b4ab0
```
# Troubleshooting
#### check logs
```sh
╰─❯ docker logs containerID
# or
╰─❯ docker logs containerName
```
#### get terminal of detached container
###### -i (interactive) -t (terminal)
```sh
╰─❯ docker ps                                 
CONTAINER ID   IMAGE         COMMAND                  CREATED          STATUS          PORTS           NAMES
7cfdb17fc5bd   archlinux     "/usr/bin/bash"          43 seconds ago   Up 42 seconds                   arch-late

# use container ID
╰─❯ docker exec -it 7cfdb17fc5bd /bin/bash
[root@7cfdb17fc5bd /]# 

# or use name
╰─❯ docker exec -it arch-late /bin/bash
```