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
CONTAINER ID   IMAGE         COMMAND                  CREATED         STATUS         PORTS            NAMES
d57ab89b5816   archlinux     "/usr/bin/bash"          9 seconds ago   Up 8 seconds                    arch-latest

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
## Troubleshooting
#### check logs
```sh
╰─❯ docker logs containerID
# or
╰─❯ docker logs containerName
# steam logs (live update, can insert chars or draw lines) or check --tail 5 (last 5 lines)
╰─❯ docker logs containerName -f
╰─❯ docker logs containerName --tail 5
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
#### Docker run vs Docker start
###### run (images) / start (container)
# tutorial project steps
#### 1- check docker network
```sh
╰─❯ docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
09c6d3a5fd8a   bridge    bridge    local
4b315e8a77f9   host      host      local
074ccbc89ac8   none      null      local
```
#### 2- create docker network
```sh
╰─❯ docker network create mongo-network
cef5fce4aecb8e50e9ec0b67c85adfa3760c713494fe8bcf396f98f576c11a90
╰─❯ docker network ls
NETWORK ID     NAME            DRIVER    SCOPE
09c6d3a5fd8a   bridge          bridge    local
4b315e8a77f9   host            host      local
cef5fce4aecb   mongo-network   bridge    local
074ccbc89ac8   none            null      local
```
#### find out exposed port of image
###### grep -A 5 (-A contect after the match) (5 number of trailing lines to show)
```sh
╰─❯ docker inspect mongo | grep -A 2 "ExposedPorts"
            "ExposedPorts": {
                "27017/tcp": {}
╰─❯ docker inspect mongo-express | grep -A 2 "ExposedPorts"
            "ExposedPorts": {
                "8081/tcp": {}
```
#### 3- run mongo image with init user and pass over ride, network, name, detached
- https://hub.docker.com/_/mongo#mongo_initdb_root_username-mongo_initdb_root_password
```sh
╰─❯ docker run -d --network mongo-network --name mongo \
    -e MONGO_INITDB_ROOT_USERNAME=admin \
    -e MONGO_INITDB_ROOT_PASSWORD=password \
    -p 27017:27017 \
    mongo
```
#### 4- run mongo express with admin user, admin pass, network, name, server name
- https://hub.docker.com/_/mongo-express#configuration
```sh
╰─❯ docker run -d --network mongo-network --name mongo-express \
    -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
    -e ME_CONFIG_MONGODB_ADMINPASSWORD=password \
    -e ME_CONFIG_MONGODB_SERVER=mongo \
    -p 8081:8081 \
    mongo-express
```
#### remove docker containers
```sh
╰─❯ docker rm -f mongodb mongo-express
mongodb
mongo-express
```
#### WARNING Memory overcommit must be enabled!
```sh
╰─❯ docker logs 413c4c551036         
Starting Redis Server
1:C 01 May 2026 14:21:53.023  WARNING Memory overcommit must be enabled! 
Without it, a background save or replication may fail under low 
memory condition. Being disabled, it can also 
cause failures without low memory condition, 
see https://github.com/jemalloc/jemalloc/issues/1328. To fix this issue 
add 'vm.overcommit_memory = 1' to /etc/sysctl.conf and then reboot or run the 
command 'sysctl vm.overcommit_memory=1' for this to take effect.
```
###### the fix
```sh
╰─❯ sudo sysctl vm.overcommit_memory=1
vm.overcommit_memory = 1

# prevent setting to revert after reboot
╰─❯ echo "vm.overcommit_memory = 1" | sudo tee /etc/sysctl.d/99-docker-mem.conf
vm.overcommit_memory = 1
```
###### explanation
```txt
The Problem: Databases often "reserve" large blocks of memory. 
Without overcommit, the kernel panics and kills the 
process (OOM/Segfault) to prevent the whole system from freezing.

The Fix: Setting this to 1 tells the kernel: "Trust the applications; 
let them allocate what they ask for, and only intervene if we 
actually run out of physical space."
```
###### not fixed, mongo shuts down after a few seconds
```txt
issue was indeed the AVX/Microarchitecture requirements 
introduced in MongoDB 5.0+. Since Arch Linux uses a very 
recent kernel and libraries, it doesn't "mask" these hardware-software 
mismatches like some older LTS kernels do, leading to that 
immediate 139 segmentation fault.
```
#### 5- use mongo:4.4 and reuse mongo-express
```sh
╰─❯ docker run -d --network mongo-network --name mongo \
    -e MONGO_INITDB_ROOT_USERNAME=admin \
    -e MONGO_INITDB_ROOT_PASSWORD=password \
    -p 27017:27017 \
    mongo:4.4

# BASICAUTH for web login
╰─❯ docker run -d --network mongo-network --name mongo-express \
    -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
    -e ME_CONFIG_MONGODB_ADMINPASSWORD=password \
    -e ME_CONFIG_MONGODB_SERVER=mongo \
    -e ME_CONFIG_BASICAUTH_USERNAME=admin \
    -e ME_CONFIG_BASICAUTH_PASSWORD=password \
    -p 8081:8081 \
    mongo-express

# navigate to http://localhost:8081/ (username=admin password=password)
```
#### -6 Use docker-compose to run a .yaml file
```sh
# creates network automatically
╰─❯ docker-compose -f mongo.yaml up -d
[+] up 3/3
 ✔ Network app_default           Created                                                                                                           
 ✔ Container app-mongo-1         Created                                                                                                           
 ✔ Container app-mongo-express-1 Created                                                                                                           
Attaching to mongo-1, mongo-express-1
--snip--
# mongo-1 -snip- "NETWORK",-snip- "ctx":"listener","msg":"Connection accepted"-snip-
--snip--
mongo-express-1  | Mongo Express server listening at http://0.0.0.0:8081
mongo-express-1  | Server is open to allow connections from anyone (0.0.0.0)

╰─❯ docker ps           
CONTAINER ID   IMAGE           COMMAND                  CREATED         STATUS         PORTS                                             NAMES
1cb0c8b4074b   mongo:4.4       "docker-entrypoint.s…"   3 minutes ago   Up 3 minutes   0.0.0.0:27017->27017/tcp, [::]:27017->27017/tcp   app-mongo-1
6cf569d4a890   mongo-express   "/sbin/tini -- /dock…"   3 minutes ago   Up 3 minutes   0.0.0.0:8081->8081/tcp, [::]:8081->8081/tcp       app-mongo-express-1
```
#### -7 use docker-compose to stop containers
```sh
# also removes the created network
╰─❯ docker-compose -f mongo.yaml down
[+] down 3/3
 ✔ Container app-mongo-express-1 Removed         
 ✔ Container app-mongo-1         Removed      
 ✔ Network app_default           Removed     
```

