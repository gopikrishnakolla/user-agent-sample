from boto3 import client
import botocore

# Create a config
session_config = botocore.config.Config(
  # The value to use in the User-Agent header (overrides)
  user_agent='gkolla-ua-test',
  # The value to append to the current User-Agent header value
  user_agent_extra='gkolla-ua-test-append'
)

ec2 = client(
  'ec2',
  config=session_config
)

instances = ec2.run_instances(
     ImageId='ami-0dc2d3e4c0f9ebd18',     
     MinCount=1,
     MaxCount=1,
     InstanceType='t2.micro',
     KeyName='ec2-ssh'
 )

print(instances["Instances"][0]["InstanceId"])
