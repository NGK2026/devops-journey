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
###### Provides the virtualized CPU, RAM, and storage needed to run the operating system
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance#example-usage
##### Basic
```tf
resource "aws_instance" "my-server" {
  ami           = "ami-0a0823e4ea064404d" # name of instance (AMI ID)
  instance_type = "t3.micro"
}
```
##### Less Basic
- Check Docs: Availability Zone, Key Name, Primary Network Interface, User Data
```tf
resource "aws_instance" "example" {
  ami           = "ami-0a0823e4ea064404d" # name of instance (AMI ID)
  instance_type = "t3.micro"
  availability_zone = " "
  key_name = " "

  # network interface inside instance is depreciated 
  # reference with primary_netowrk_interface instead
  primary_network_interface {
    network_interface_id = aws_network_interface-example.id
  }

  # runs script when launching instance
  user_data = <<-EOF
                #!/bin/bash
                sudo apt update -y
                # add more bash commands
                EOF
  tags = {
    Name = ""
  }
}
```
## Create VPC (Isolated cloud resource):
###### Provides a private, isolated logical network on the AWS cloud to house all resources
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance#example-usage
```tf
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}
```
## Create Subnet: 
###### Isolate a range of IP addresses within the VPC to organize and secure specific resource groups
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
## Create Internet gateway
###### Acts as a bridge between the VPC and the public internet to allow traffic flow
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/internet_gateway.html
```tf
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "main"
  }
}
```
## Create Route Table
###### Contains a set of routes that determine where network traffic from the subnet is directed
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route_table
```tf
resource "aws_route_table" "example" {
  vpc_id = aws_vpc.example.id

  route {
    cidr_block = "10.0.1.0/24"
    gateway_id = aws_internet_gateway.example.id
  }

  route {
    ipv6_cidr_block        = "::/0"
    egress_only_gateway_id = aws_egress_only_internet_gateway.example.id
  }

  tags = {
    Name = "example"
  }
}
```
## Availability Zones
- https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
```txt
Europe (Stockholm 'eu-north-1') - availability zones: 3

Meaning:

Zone 1 - eu-north-1a
Zone 2 - eu-north-1b
Zone 3 - eu-north-1c
```
## Create Route Table Association
###### Explicitly links the subnet to the route table so the subnet knows to send traffic through the Internet Gateway
- https://registry.terraform.io/providers/-/aws/latest/docs/resources/route_table_association
```tf
# to connect route table with subnet
resource "aws_route_table_association" "example" {
  subnet_id      = aws_subnet.example.id
  route_table_id = aws_route_table.example.id
}
```
## Create Security Group
###### Functions as a virtual firewall to control inbound and outbound traffic at the instance level
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group
```tf
resource "aws_security_group" "allow_tls" {
  name        = "allow_tls"
  description = "Allow TLS inbound traffic and all outbound traffic"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "allow_tls"
  }
}
```
## Create Network Interface
###### Provides a logical networking component that represents a primary connection point for the server
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/network_interface
```tf
resource "aws_network_interface" "test" {
  subnet_id       = aws_subnet.public_a.id
  private_ips     = ["10.0.0.50"]
  security_groups = [aws_security_group.web.id]

  attachment {
    instance     = aws_instance.test.id
    device_index = 1
  }
}
```
## Create Elastic IP 'EIP'
###### Grants a static, public IPv4 address that remains constant even if the instance is stopped or restarted
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/eip
```tf
resource "aws_eip" "one" {
  domain                    = "vpc"
  network_interface         = aws_network_interface.multi-ip.id
  associate_with_private_ip = "10.0.0.10"
}
```
# Terraform Variables
## Create Variable
```tf
variable "subnet_prefix" {
  description = "cidr block for the subnet
}
# if used terraform apply, terraform will prompt for value
```
```sh
# or can define variable value directly in CLI
terraform apply -var "subnet_prefix=10.0.100/24"
```
```txt
or create file 'terraform.tfvars'
and assign the value to the variable 
```
```tf
subnet_prefix = "10.0.200.0/24"
```