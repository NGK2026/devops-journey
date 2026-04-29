1. 
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
5. 