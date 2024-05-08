terraform {
  backend "s3" {
    bucket         = "terraform-backend-sliu"
    key            = "terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
  }
}
