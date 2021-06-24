variable "aws_region"{
    default="ap-south-1"
}

variable "profile"{
    default="default"
}

variable "vpc_cidr"{
    default="10.0.0.0/16"
}

variable "subnets_cidr"{
    type=list
    default=["10.0.1.0/24","10.0.2.0/24"]
}

variable "AZs"{
    type =list
    default=["ap-south-1a","ap-south-1b"]
}

variable "OS1Ami"{
    default = "ami-010aff33ed5991201"
}

variable "OS1InstanceType"{
     default="t2.micro"
}

variable "OS1AZ"{
    default="ap-south-1a"
}

variable "OS1key"{
    default="myaccountAWS"
}

output "OS1subnetId" {
    value = aws_subnet.mysubnet[0].id
}

variable "OS2Ami"{
    default = "ami-011c99152163a87ae"
}

variable "OS2InstanceType"{
     default="t2.micro"
}

variable "OS2AZ"{
    default="ap-south-1b"
}

variable "OS2key"{
    default="myaccountAWS"
}

output "OS2subnetId" {
    value = aws_subnet.mysubnet[1].id
}