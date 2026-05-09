provider "aws" {
  region = "eu-north-1"
}


# 1- Create VPC
resource "aws_vpc" "health-monitor" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "monitor"
  }
}

# 2- Create Internet Gateway
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.health-monitor.id
}

# 3- Create Custom Route Table
resource "aws_route_table" "monitor-route-table" {
  vpc_id = aws_vpc.health-monitor.id

  route {
    cidr_block = "0.0.0.0/0" # default gateway route
    gateway_id = aws_internet_gateway.gw.id
  }

  route {
    ipv6_cidr_block = "::/0" # default gateway route
    gateway_id = aws_internet_gateway.gw.id
  }

  tags = {
    Name = "monitor-rt"
  }
}

# 4- Create Subnet # add availability zone too
resource "aws_subnet" "subnet-1" {
  vpc_id     = aws_vpc.health-monitor.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "eu-north-1a"
  tags = {
    Name = "monitor-subnet"
  }
}

# 5- Associate subnet with Route Table
resource "aws_route_table_association" "rt-association" {
  subnet_id      = aws_subnet.subnet-1.id
  route_table_id = aws_route_table.monitor-route-table.id
}

resource "aws_security_group" "allow_web" {
  name        = "allow_web_traffic"
  description = "Allow web traffic"
  vpc_id      = aws_vpc.health-monitor.id
  
  ingress {
    description = "SSH"
    from_port        = 22
    to_port          = 22
    protocol         = "6" # meaning TCP , 1 is ICMP, 17 UDP, -1 ALL
    cidr_blocks      = ["0.0.0.0/0"] # any ip can access
    ipv6_cidr_blocks = ["::/0"]
  }
  
    ingress {
    description = "HTTP"
    from_port        = 80
    to_port          = 80
    protocol         = "6" # meaning TCP , 1 is ICMP, 17 UDP, -1 ALL
    cidr_blocks      = ["0.0.0.0/0"] # any ip can access
    ipv6_cidr_blocks = ["::/0"]
  }
  
    ingress {
    description = "health-monitor"
    from_port        = 5000
    to_port          = 5000
    protocol         = "6" # meaning TCP , 1 is ICMP, 17 UDP, -1 ALL
    cidr_blocks      = ["0.0.0.0/0"] # any ip can access
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    description = "prometheus"
    from_port        = 9090
    to_port          = 9090
    protocol         = "6" # meaning TCP , 1 is ICMP, 17 UDP, -1 ALL
    cidr_blocks      = ["0.0.0.0/0"] # any ip can access
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    description = "grafana"
    from_port        = 3000
    to_port          = 3000
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
  security_groups = [aws_security_group.allow_web.id]
}

# 8- Assign an elastic IP to the network interface created in step 7
resource "aws_eip" "one" {
  domain                    = "vpc"
  network_interface         = aws_network_interface.web-server-nic.id
  associate_with_private_ip = "10.0.1.50"
  depends_on = [aws_internet_gateway.gw] 
}

# 9- Create Amazon Linux server and install/enable apache2
resource "aws_instance" "web-server-instance" {
  ami           = "ami-059f32cf6eecf0ef9" # change ami
  instance_type = "t3.micro"
  availability_zone = "eu-north-1a"
  key_name = "main-key"
  primary_network_interface {
    network_interface_id = aws_network_interface.web-server-nic.id
  }
  
  user_data = <<-EOF
                #!/bin/bash
                dnf update -y
                dnf install -y git docker
                systemctl enable docker
                systemctl start docker
                usermod -a -G docker ec2-user
                git clone https://github.com/NGK2026/devops-journey.git /home/ec2-user/devops-journey
                cd /home/ec2-user/devops-journey/projects/health-monitor
                docker network create monitor-net
                docker build -t health-monitor .
                docker run -d --name health-monitor --network monitor-net -p 5000:5000 ngk2026/health-monitor:latest
                EOF
  tags = {
    Name = "health-app"
  }
}

output "public_ip" {
  value = aws_eip.one.public_ip
}