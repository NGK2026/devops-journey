# Purpose
Documentation of my devops path

## Step-1 Automate the Boring Stuff with Python Book
- Add practiced scripts to repo
###### Skipped
1. Chapter 13 - Web Scraping
2. Chapter 14 - Excel Spreadsheets
3. Chapter 15 - Google Sheets
4. Chapter 17 - PDF and Word Documents
5. Chapter 20 - Sending Email, Texts, and Push Notifications
6. Chapter 21 - Making Graphs and Manipulating Images
7. Chapter 22 - Recognizing Text in Images
8. Chapter 23 - Controlling the Keyboard and Mouse
9. Chapter 24 - Text-to-Speech and Speech Recognition Engines

## Step-2 Git
#### youtube: Git and GitHub for Beginners - Crash Course - freeCodeCamp.org
- https://www.youtube.com/watch?v=RGOj5yH7evk

## Step-3 Bash
#### youtube: Bash Scripting Tutorial for Beginners - TechWorld with Nana
- https://www.youtube.com/watch?v=PNhq_4d-5ek
###### Projects
1. Backup a directory to another location with a timestamp
2. Monitors disk usage and prints a warning if above 80%
3. Auto-organizes files in a folder by extension into subfolders

## Step-4 Cloud Concepts
#### youtube: Cloud Computing In 6 Minutes - Simplilearn
- https://www.youtube.com/watch?v=M988_fsOSWo
#### youtube: AWS Certified Cloud Practitioner Training 2020 - Full Course - freeCodeCamp.org
- https://www.youtube.com/watch?v=3hLmDS179YE
###### Cloud Concepts
1. (0:09:57) — What is Cloud Computing
2. (0:12:10) — Six Advantages
3. (0:14:42) — Types of Cloud Computing
4. (0:16:48) — Deployment Models
###### AWS Global Infrastructure
5. (0:19:27) — Introduction and Map
6. (0:20:30) — Regions
7. (0:24:30) — Availability Zones
###### Getting Started
8. (0:29:20) — Creating an AWS Account
9. (0:32:43) — Billing Preferences and Budgets (so you don't get charged accidentally)
10. (0:40:09) — IAM Users
11. (0:41:14) — MFA on Root Account
12. (0:43:40) — Create IAM User
###### Hands On
13. (0:49:50) — Intro and Regions
14. (0:51:03) — EC2
15. (1:12:47) — S3
16. (1:22:00) — Lambda
###### Technology Overview
17. (2:44:13) — AWS Networking
###### Security
18. (3:13:49) — Shared Responsibility Model
19. (3:35:06) — Security Groups vs NACLs

## Step-5 AWS Hands On (Core Services)
#### youtube: AWS Tutorial for Beginners – Kevin Stratvert
- https://www.youtube.com/watch?v=Nzv-tzU-UAw
##### Done:
- Launch an EC2 instance, SSH into it from terminal
- Create an S3 bucket, upload a file via CLI (not console)
- Create an IAM user with limited permissions
- Create an /aws folder in repo with:
  * /commands.md — every CLI command used, with a one line explanation
  * /setup.md — steps taken to launch EC2, create S3 bucket, set up IAM user

##### Website hosted with S3
- http://onyx-core-system.s3-website-us-east-1.amazonaws.com/

## Step-6 Terraform
#### youtube: Terraform explained in 15 mins - TechWorld with Nana
- https://www.youtube.com/watch?v=l5k1ai_GBDE
#### youtube: Terraform Course - Automate your AWS cloud infrastructure - freeCodeCamp.org
- https://www.youtube.com/watch?v=SLB_c_ayRMo
1. (0:20:51) Terraform Overview
2. (0:43:31) Modifying Resources
3. (0:50:30) Deleting Resources
4. (0:54:55) Referencing Resources
5. (1:04:47) Terraform Files
6. (1:09:45) Practice Project
  * 1- Create VPC
  * 2- Create Internet Gateway
  * 3- Create Custom Route Table
  * 4- Create Subnet
  * 5- Associate subnet with Route Table
  * 6- Create Security Group to allow port 22, 80, 443
  * 7- Create a network interface with an ip in the subnet that was created in step 4
  * 8- Assign an elastic IP to the network interface created in step 7
  * 9- Create Amazon Linux server and install/enable apache2
7. (2:03:46) Terraform Variables
##### Done:
- Create /terraform folder in repo with:
  * /commands.md — every CLI command used, with a one line explanation, init/plan/apply/destroy
  * /setup.md — steps to install Terraform, configure AWS provider
  * /main.tf - Terraform file that provisions EC2 and S3
##### Created Apache Server Address:
- http://13.61.210.62/

## Step-7 Docker
#### youtube: Docker Tutorial for Beginners [FULL COURSE in 3 Hours] - TechWorld with Nana
- https://www.youtube.com/watch?v=3c-iBn73dDE
##### Done:
* 1- Tutorial
* 2- Project
  
## Step-8 Kubernetes
#### youtube: Kubernetes Tutorial for Beginners [FULL COURSE in 4 Hours] - TechWorld with Nana
- https://www.youtube.com/watch?v=X48VuDVv0do
#### TODO:
* 1- Project: Deploy Docker container from Step-7 onto local Kubernetes cluster using Minikube