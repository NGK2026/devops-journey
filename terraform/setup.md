1. 
```sh
sudo pacman -S terraform
```
2. Open VScode > install extension **HashiCorp Terraform**
3. Create **main.tf**
4. To use AWS on terraform, get provider code from: https://registry.terraform.io/providers/hashicorp/aws/latest
```tf
provider "aws" {
  # Configuration options
}
```
5. Add region:
```tf
provider "aws" {
  region = "eu-north-1"
}
```
6. Check Authentication and Configuration "AWS" : https://registry.terraform.io/providers/hashicorp/aws/latest/docs#authentication-and-configuration
```tf
provider "aws" {
  region = "eu-north-1"
  access_key = "--snip--" # not recommended !
  secret_key = "--snip--" # this is not safe !
}
```
7. Basic syntax to create resource for provider eg:
```tf
resource "<provider>_<resource_type>" "name" {
  config options...connection 
  key = "value"
  key2 = "another value"
}
```
8. EC2 instance: Create, update, delete
- https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance#example-usage
```tf
resource "aws_instance" "my-server" {
  ami           = "ami-0a0823e4ea064404d" # name of instance (AMI ID)
  instance_type = "t3.micro"
}
```
