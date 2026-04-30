1. provider, resource added to main.tf
```sh
# initialize terraform main.tf
# creates .terraform folder/ with licence.txt and necessary provider plugins
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
5. Apply tags from saved file
```sh
terraform apply "myserver.tfplan"

aws_instance.my-server: Modifying... [id=i-0e5bde8f0645ec361]
aws_instance.my-server: Modifications complete after 2s [id=i-0e5bde8f0645ec361]

Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
```
6. Destroy myserver instance
```sh
terraform destroy

aws_instance.my-server: Refreshing state... [id=i-0e5bde8f0645ec361]

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with
the following symbols:
  - destroy

Terraform will perform the following actions:

  # aws_instance.my-server will be destroyed
  - resource "aws_instance" "my-server" {
      - ami                                  = "ami-0a0823e4ea064404d" -> null
      - arn                                  = "arn:aws:ec2:eu-north-1:825386256642:instance/i-0e5bde8f0645ec361" -> null
      --snip--
      - cpu_options {
          - core_count            = 1 -> null
          - threads_per_core      = 2 -> null
            # (2 unchanged attributes hidden)
        }
      --snip--
        }
    }

Plan: 0 to add, 0 to change, 1 to destroy.

Do you really want to destroy all resources?
  Terraform will destroy all your managed infrastructure, as shown above.
  There is no undo. Only 'yes' will be accepted to confirm.

  Enter a value: yes

aws_instance.my-server: Destroying... [id=i-0e5bde8f0645ec361]
aws_instance.my-server: Still destroying... [id=i-0e5bde8f0645ec361, 00m10s elapsed]
aws_instance.my-server: Still destroying... [id=i-0e5bde8f0645ec361, 00m20s elapsed]
aws_instance.my-server: Still destroying... [id=i-0e5bde8f0645ec361, 00m30s elapsed]
aws_instance.my-server: Destruction complete after 30s

Destroy complete! Resources: 1 destroyed.
```
### NB: If an instance is up, but has been removed from the main.tf, executing 'terraform apply' would destroy that omitted resource from main.tf
7. Create VPC and Subnet
```sh
terraform apply                  

--snip--

Terraform will perform the following actions:

  # aws_subnet.subnet-1 will be created
  # aws_vpc.my-vpc will be created
--snip--
Plan: 2 to add, 0 to change, 0 to destroy.
--snip--
aws_vpc.my-vpc: Creating...
aws_vpc.my-vpc: Creation complete after 2s [id=vpc-063936681f47c2224]
aws_subnet.subnet-1: Creating...
aws_subnet.subnet-1: Creation complete after 1s [id=subnet-0c31b72d21c7a330c]

Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```
### Use Auto approve to skip 'yes' confirmation
```sh
terraform apply --auto-approve
```
