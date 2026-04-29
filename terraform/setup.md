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
  access_key = "--snip--"
  secret_key = "--snip--"
}
```