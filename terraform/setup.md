# AWS
## Create EC2 Key pairs
1. AWS *Dashboard*
2. View all services
3. **EC2** > **Network & Security** > **Key Pairs**
4. **Create key pair** > Give *Name* > *ED25519* > *.pem*

# Terraform
## Get Started
```sh
sudo pacman -S terraform
```
2. Open VScode > install extension **HashiCorp Terraform**
3. Create **main.tf**
4. To use AWS on terraform, get provider code from: 
- https://registry.terraform.io/providers/hashicorp/aws/latest
```tf
provider "aws" {
  # Configuration options
}
```
## Add region:
```tf
provider "aws" {
  region = "eu-north-1"
}
```
## Check Authentication and Configuration "AWS" : 
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs#authentication-and-configuration
```tf
provider "aws" {
  region = "eu-north-1"
  access_key = "--snip--" # not recommended !
  secret_key = "--snip--" # this is not safe !
}
```
## Basic syntax to create resource for provider eg:
```tf
resource "<provider>_<resource_type>" "name" {
  config options...connection 
  key = "value"
  key2 = "another value"
}
```
## Create EC2 instance:
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance#example-usage
```tf
resource "aws_instance" "my-server" {
  ami           = "ami-0a0823e4ea064404d" # name of instance (AMI ID)
  instance_type = "t3.micro"
}
```
## Add Tags!
```tf
resource "aws_instance" "my-server" {
  ami           = "ami-0a0823e4ea064404d" # name of instance (AMI ID)
  instance_type = "t3.micro"
  tags = {
    Name = "HelloWorld"
  }
}
```
## Create VPC (Isolated cloud resource):
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance#example-usage
```tf
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}
```
## Create subnet: 
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/subnet
```tf
# 'vpc_id\ is the reference of the created vpc .id
resource "aws_subnet" "main" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "Main"
  }
}
```
## Create internet gateway
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/internet_gateway.html
```tf
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "main"
  }
}
```
