## Workflow hands-on practice 
###### GitHub Actions Tutorial - TechWorld with Nana
#### 1- DockerHub - access tokens
1. *Create* account
2. Leftside pannel > **Settings** > **Personal access tokens**
3. **Generate new token**
4. Fill requirements, Access permission: *Read & Write*
5. Copy/Save token.
#### 2- GitHub - secrets
1. Open repo **Settings**
2. Left settings column > **Secrets and variables** > **Actions**
3. New repository secret, and create:
4. Name: DOCKER_USERNAME , Secret: enter docker hub username , click **Add secret**
5. Name: DOCKER_PASSWORD , Secret: enter access token , click **Add secret**
#### 3- DockerHub - repository
1. Leftside pannel > Repositories > Create a Repository
2. Fill *Repository Name* , Visibility: *Public* > **Create**
#### 4- GitHub - Actions
1. Open repo **Actions** found at top *repo row*
2. Open **New workflow**
3. Search for **Publish Docker Container** - *By GitHub Actions*
4. **Save** it. It will be */.github/workflows/docker-publish.yml*


