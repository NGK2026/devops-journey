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
7. (2:03:46) Terraform Variables
##### TODO:
- Create a /terraform folder in repo with:
  * /commands.md — every CLI command used, with a one line explanation
  * /setup.md — steps to install Terraform, configure AWS provider, init/plan/apply/destroy
  * /main.tf - Terraform file that provisions EC2 and S3
- Practice Project
  * 1- Create VPC
  * 2- Create Internet Gateway
  * 3- Create Custom Route Table
  * 4- Create Subnet
  * 5- Associate subnet with Route Table
  * 6- Create Security Group to allow port 22, 80, 443
  * 7- Create a network interface with an ip in the subnet that was created in step 4
  * 8- Assign an elastic IP to the network interface created in step 7
  * 9- Create Amazon Linux server and install/enable apache2