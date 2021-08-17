from crhelper import CfnResource
from boto3 import client
import botocore

helper = CfnResource()

@helper.create
@helper.update
def ec2_set_useragent(event, _):    
    session_config = botocore.config.Config(     
        user_agent='gkolla-ua-test'
    )
    ec2 = client(
        'ec2',
        config=session_config
    )   

    instances = ec2.run_instances(
     ImageId=event['ResourceProperties']['ImageId'],     
     MinCount=1,
     MaxCount=1,
     InstanceType=event['ResourceProperties']['InstanceType'],
     KeyName=event['ResourceProperties']['KeyPair']
    )

    helper.Data['InstId'] = instances["Instances"][0]["InstanceId"]
@helper.delete
def no_op(_, __):
    pass

def handler(event, context):
    helper(event, context)
