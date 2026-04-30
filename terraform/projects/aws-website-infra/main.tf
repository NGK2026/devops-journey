provider "aws" {
  region = "eu-north-1"
  access_key = "--snip--"
  secret_key = "--snip--"
}

# 1- Create VPC
resource "aws_vpc" "prod-vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "production"
  }
}

# 2- Create Internet Gateway
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.prod-vpc.id
}

# 3- Create Custom Route Table
resource "aws_route_table" "prod-route-table" {
  vpc_id = aws_vpc.prod-vpc.id

  route {
    cidr_block = "0.0.0.0/0" # default gateway route
    gateway_id = aws_internet_gateway.gw.id
  }

  route {
    ipv6_cidr_block        = "::/0" # default gateway route
    egress_only_gateway_id = aws_internet_gateway.gw.id
  }

  tags = {
    Name = "Prod"
  }
}

# 4- Create Subnet # add availability zone too
resource "aws_subnet" "subnet-1" {
  vpc_id     = aws_vpc.prod-vpc.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "eu-north-1a"
  tags = {
    Name = "prod-subnet"
  }
}

# 5- Associate subnet with Route Table
resource "aws_route_table_association" "rt-association" {
  subnet_id      = aws_subnet.subnet-1.id
  route_table_id = aws_route_table.prod-route-table.id
}

# 6- Create Security Group to allow port 22, 80, 443
resource "aws_security_group" "allow_web" {
  name        = "allow_web_traffic"
  description = "Allow web traffic"
  vpc_id      = aws_vpc.prod-vpc.id

  ingress {
    description = "HTTP"
    from_port        = 80
    to_port          = 80
    protocol         = "6" # meaning TCP , 1 is ICMP, 17 UDP, -1 ALL
    cidr_blocks      = ["0.0.0.0/0"] # any ip can access
    ipv6_cidr_blocks = ["::/0"]
  }

    ingress {
    description = "HTTPS"
    from_port        = 443
    to_port          = 443
    protocol         = "6" # meaning TCP , 1 is ICMP, 17 UDP, -1 ALL
    cidr_blocks      = ["0.0.0.0/0"] # any ip can access
    ipv6_cidr_blocks = ["::/0"]
  }

    ingress {
    description = "SSH"
    from_port        = 22
    to_port          = 22
    protocol         = "6" # meaning TCP , 1 is ICMP, 17 UDP, -1 ALL
    cidr_blocks      = ["0.0.0.0/0"] # any ip can access
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1" # Allow all protocols
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "allow_web"
  }
}

# 7- Create a network interface with an ip in the subnet that was created in step 4
resource "aws_network_interface" "web-server-nic" {
  subnet_id       = aws_subnet.subnet-1.id
  private_ips     = ["10.0.1.50"]
  /* In a production environment, engineers often group IPs. For example:
  .10 through .20 for Load Balancers.
  .50 through .100 for Web Servers.
  .200+ for Databases.*/
  security_groups = [aws_security_group.allow_web.id]
}

# 8- Assign an elastic IP to the network interface created in step 7
resource "aws_eip" "one" {
  domain                    = "vpc"
  network_interface         = aws_network_interface.multi-ip.id
  associate_with_private_ip = "10.0.0.10"
}

# 9- Create Amazon Linux server and install/enable apache2