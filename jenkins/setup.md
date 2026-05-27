## Table of Contents (for setup.md)

- [Pull / run jenkins container](#pull--run-jenkins-container)
- [new pipeline](#new-pipeline)
- [Github token](#github-token)
- [Credentials](#credentials)
- [Back to pipeline configuration](#back-to-pipeline-configuration)
- [Target devops-journey/jenkins repo](#target-devops-journeyjenkins-repo)
- [Create Jenkinsfile in jenkins repo](#create-jenkinsfile-in-jenkins-repo)
- [test/execute jenkinsfile changes without commit, using Replay](#testexecute-jenkinsfile-changes-without-commit-using-replay)
- [restart from stage](#restart-from-stage)
- [set multibranch pipeline scan trigger (when using localhost)](#set-multibranch-pipeline-scan-trigger-when-using-localhost)

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
#### new pipeline
6. New Item > Enter: my-pipeline-github & Select: Multibranch Pipeline > configure project
7. Branch Source: Git , Enter Project Repository (HTTPS)
8. Behaviors Add > Filter by name (with regex)
#### Github token
9. Settings > Developer settings > Personal access tokens > Tokens (classic)
10. Scope: Repo > Generate token
#### Credentials
11. Navigate out of configuration, into my-pipeline-github
12. Select Credentials
13. Under (Stores scoped to my-pipeline-github) select my-pipeline-github
14. Select Global > Add Credentials > Username with password
15. Add git email, paste git token as password, fill ID, create!
#### Back to pipeline configuration
16. Credentials > select the one we just created above
17. Save
```sh
Processed 1 branches
[Mon May 25 08:43:54 UTC 2026] Finished branch indexing. Indexing took 4.9 sec
Finished: SUCCESS
```
#### Target devops-journey/jenkins repo
18. Configure > Behaviors > Filter by name (with regular expressions)
19. Add Regular expression ^main$
20. Scrll below to Build Configuration > Mode: by Jenkinsfile > Script Path:
21. Change to jenkins/Jenkinsfile
#### Create Jenkinsfile in jenkins repo
- skelaton, testing:
```groovy
pipeline {

    agent any

    stages {

        stage("build") {

            steps {
                echo 'building the application...'
            }
        }

        stage("test") {

            steps {
                echo 'testing the application...'
            }
        }

        stage("deploy") {

            steps {
                echo 'deploying the application...'
            }
        }
    }
}
```
```sh
Checking branches...
  Checking branch main
      ‘jenkins/Jenkinsfile’ found
    Met criteria
No changes detected: main (still at ac090c9ee01d81e2591d2799f3a3b033374b8afe)
Processed 1 branches
[Mon May 25 09:10:48 UTC 2026] Finished branch indexing. Indexing took 1.6 sec
Finished: SUCCESS
```
#### test/execute jenkinsfile changes without commit, using Replay
1. Select my-pipeline-github > select main
2. On the left side pannel, click the build you want to modify/test
3. On the left side pannel, select Replay
4. Test Groovy script, change this block:
```groovy
        stage("build") {

            steps {
                echo 'building the application...'
                
                script {
                    def test = 2 + 2 > 3 ? 'cool' : 'not cool'
                    echo test
                }
            }
        }
```
5. Run > left side pannel, select new build's dropdown menu:
6. Select Pipeline Overview > check build stage
7. Outputs building the application... and cool
#### restart from stage
- to test a specific stage in the jenkinsfile
1. Select my-pipeline-github > main > select Build #
2. On left side pannel, select Restart from Stage 
3. Drop down menu to select desired stage by name
4. Run
#### set multibranch pipeline scan trigger (when using localhost)
1. Select my-pipeline-github, left side pannel click Configure
2. Scroll to Scan Multibranch Pipeline Triggers and check Periodically if not otherwise run
3. Set to desired interval
