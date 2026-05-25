#### Pull / run jenkins container
```sh
╰─❯ docker pull jenkins/jenkins

╰─❯ docker run \     
-p 8080:8080 -p 50000:50000 \
-d -v jenkins_home:/var/jenkins_home \
--name jenkins \
jenkins/jenkins

╰─❯ docker ps   
CONTAINER ID   IMAGE             COMMAND                  CREATED         STATUS         PORTS                                                                                          NAMES
668f3fe5147d   jenkins/jenkins   "/usr/bin/tini -- /u…"   5 seconds ago   Up 4 seconds   0.0.0.0:8080->8080/tcp, [::]:8080->8080/tcp, 0.0.0.0:50000->50000/tcp, [::]:50000->50000/tcp   jenkins

╰─❯ docker logs 668f3fe5147d
[LF]> Jenkins initial setup is required. An admin user has been created and a password generated.
[LF]> Please use the following password to proceed to installation:
[LF]> 
[LF]> d4a7ac7b4ae74de5a5f206d971011379
[LF]> 
[LF]> This may also be found at: /var/jenkins_home/secrets/initialAdminPassword
```
1. Navigate to localhost:8080 and enter the above password
2. Select install suggested plugins
3. Enter first admin creds
4. Instance configuration localhost as is
5. Start using Jenkins
#### Credentials
6. Navigate top right cog (Manage Jenkins) > Credentials
7. Select Username with password
8. Scope Global



6. New Item > Enter: my-test-pipeline & Select: Multibranch Pipeline > configure project
7. Branch Source: Git , Enter Project Repository (HTTPS)
8. Behaviors Add > Filter by name (with regex)

