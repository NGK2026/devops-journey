1. provider, resource added to main.tf
```sh
# initialize terraform main.tf
terraform init

Initializing the backend...
Initializing provider plugins...
- Finding latest version of hashicorp/aws...
- Installing hashicorp/aws v6.42.0...
- Installed hashicorp/aws v6.42.0 (signed by HashiCorp)

--snip--

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

--snip--
```

2. 
```sh
# check the execution plan for main.tf
terraform plan

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with
the following symbols:
  + create

Terraform will perform the following actions:

  # aws_instance.my-server will be created
  + resource "aws_instance" "my-server" {
      + ami                                  = "ami-0a0823e4ea064404d"
      + arn                                  = (known after apply)
      --snip--
      + instance_type                        = "t3.micro"
      --snip--
      + public_ip                            = (known after apply)
      + region                               = "eu-north-1"
      + secondary_private_ips                = (known after apply)
      --snip--
      + vpc_security_group_ids               = (known after apply)

      + capacity_reservation_specification (known after apply)

      + cpu_options (known after apply)
      --snip--
      + secondary_network_interface (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions
if you run "terraform apply" now.

```

3. 
```sh
# apply the plan proposed for main.tf
terraform apply

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with
the following symbols:
  + create

Terraform will perform the following actions:

  # aws_instance.my-server will be created
  + resource "aws_instance" "my-server" {
      + ami                                  = "ami-0a0823e4ea064404d"
     --snip--
      + vpc_security_group_ids               = (known after apply)

      + capacity_reservation_specification (known after apply)
      --snip--
      + secondary_network_interface (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

aws_instance.my-server: Creating...
aws_instance.my-server: Still creating... [00m10s elapsed]
aws_instance.my-server: Creation complete after 14s [id=i-0e5bde8f0645ec361]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

```
4. Tags were added to the resource, and used -out to save plan
```sh
# plan again after adding tag to resource
# and save plan to a file -out=myserver.tfplan
terraform plan -out=myserver.tfplan

aws_instance.my-server: Refreshing state... [id=i-0e5bde8f0645ec361]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with
the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # aws_instance.my-server will be updated in-place
  ~ resource "aws_instance" "my-server" {
        id                                   = "i-0e5bde8f0645ec361"
      ~ tags                                 = {
          + "Name" = "HelloWorld"
        }
      ~ tags_all                             = {
          + "Name" = "HelloWorld"
        }
        # (39 unchanged attributes hidden)

        # (9 unchanged blocks hidden)
    }

Plan: 0 to add, 1 to change, 0 to destroy.

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Saved the plan to: myserver.tfplan

To perform exactly these actions, run the following command to apply:
    terraform apply "myserver.tfplan"
```