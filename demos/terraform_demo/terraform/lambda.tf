resource "aws_lambda_function" "example_lambda2" {
  function_name = "MyExampleFunction2"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.8"
  role          = aws_iam_role.lambda_execution_role.arn
  filename      = "../lambda_function/lambda_function.zip"

  source_code_hash = filebase64sha256("../lambda_function/lambda_function.zip")
}

resource "aws_lambda_function" "example_lambda" {
  function_name = "MyExampleFunction"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.8"
  role          = aws_iam_role.lambda_execution_role.arn
  filename      = "../lambda_function/lambda_function.zip"

  source_code_hash = filebase64sha256("../lambda_function/lambda_function.zip")
}