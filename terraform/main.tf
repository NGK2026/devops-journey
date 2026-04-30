provider "aws" {
  region = "eu-north-1"
  access_key = "--snip--"
  secret_key = "--snip--"
}

# create instance called my-server with 
# specific AMI ID of Amazon Linux kernel 6.1 
# instance type t3.micro
# resource "aws_instance" "my-server" {
#   ami           = "ami-0a0823e4ea064404d" # name of instance (AMI ID)
#   instance_type = "t3.micro"
#   tags = {
#     Name = "HelloWorld"
#   }
# }

# Create VPC, and add Tags 
resource "aws_vpc" "my-vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "production"
  }
}

# Create subnet, reference the previous vpc in vpc_id
resource "aws_subnet" "subnet-1" {
  vpc_id     = aws_vpc.my-vpc.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "prod-subnet"
  }
}