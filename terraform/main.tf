provider "aws" {
  region = "eu-north-1"
  access_key = "--snip--"
  secret_key = "--snip--"
}

resource "aws_instance" "my-server" {
  ami           = "ami-0a0823e4ea064404d" # name of instance (AMI ID)
  instance_type = "t3.micro"
}