def lambda_handler(event, context):
    print("Hello, World!, this is from the terraform demo")
    return {
        'statusCode': 200,
        'body': 'Hello, World! this is from the terraform demo'
    }