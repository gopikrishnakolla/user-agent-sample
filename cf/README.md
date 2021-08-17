# user-agent-sample
Sample code to demonstrate setting custom user agent string.

## CloudFormation Template using Custom Resource
Sample code to demonstrate invoking a custom resource (lambda) from CloudFormation, where you can set user agent and invoke EC2 run_instances to create EC2 instance/(s).

## Pre-requisite for running this sample
Before creating stack using CloudFormation, make sure you have created the Lambda function using lambda_function.py.
- Parameters (required for CloudFormation)
    - EC2 instance type
    - ARN of Lambda function you created
    - Key Pair name (Make sure you have the private key file with you)
    - AMI Id

### To create lambda function
- Copy lambda_function.py to a new and empty folder
- Run `pip install -t . crhelper`
- Zip all files recursively in current directory `zip -r ../lambdaec2.zip ./`
- Now create the lambda funciton `aws lambda create-function --function-name "LambdaEC2" --handler "lambda_function.handler" --timeout 60  --zip-file fileb://../lambdaec2.zip --runtime python3.8 --role "arn:aws:iam::123412341234:role/<ROLE_NAME>"`