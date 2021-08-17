# CloudFormation Template using Custom Resource
Sample code to demonstrate invoking a custom resource (lambda) from CloudFormation, where you can set user agent and invoke EC2 run_instances to create EC2 instance/(s).

## Pre-requisite for running this sample
Before creating stack using CloudFormation, make sure you have created the Lambda function using lambda_function.py (see below).
- Parameters (required for CloudFormation)
    - EC2 instance type
    - ARN of Lambda function you created
    - Key Pair name (Make sure you have the private key file with you)
    - AMI Id

### To create lambda function
You will need aws_access_key_id and aws_secret_access_key in ~/.aws/credentials
optionally you can have AWS configuration like region, output format etc in ~/.aws.config
- Copy lambda_function.py to a new and empty folder
- Run `pip install -t . crhelper`
- Zip all files recursively in current directory `zip -r ../lambdaec2.zip ./`
- Now create the lambda funciton `aws lambda create-function --function-name "LambdaEC2" --handler "lambda_function.handler" --timeout 60  --zip-file fileb://../lambdaec2.zip --runtime python3.8 --role "<ARN_OF_ROLE>"`. Make sure the role has access to create EC2 instances.