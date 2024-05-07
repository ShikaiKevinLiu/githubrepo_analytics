how to upload a file into s3
```
provider "aws" {
  region = "us-east-1"  # 确保使用了正确的 AWS 区域
}
resource "aws_s3_object" "my_file" {
  bucket = "skliu-bucket1"
  key    = "your-file-name.pdf"
  source = "./myresume.pdf"
}```
