## Workflow hands-on practice 
###### GitHub Actions Tutorial - TechWorld with Nana
#### 1- DockerHub - access tokens
1. *Create* account
2. Leftside pannel > **Settings** > **Personal access tokens**
3. **Generate new token**
4. Fill requirements, Access permission: *Read & Write*
5. Copy/Save token.
#### 2- GitHub - secrets
1. Create at root: ./github/workflows/pipeline.yml
2. Open repo **Settings**
3. Left settings column > **Secrets and variables** > **Actions**
4. New repository secret, and create:
5. Name: DOCKER_USERNAME , Secret: enter docker hub username , click **Add secret**
6. Name: DOCKER_PASSWORD , Secret: enter access token , click **Add secret**
#### 3- GitHub - Actions
1. *Create* at root: */.github/workflows/pipeline.yml*
2. Open repo **Actions** found at top *repo row*
3. Open **New workflow**
4. Search for **Publish Docker Container** - *By GitHub Actions*

