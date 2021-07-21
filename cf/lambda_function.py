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
    response = ec2.describe_instance_attribute(
        Attribute='instanceType',
        InstanceId=event['ResourceProperties']['instId']
    )    
    helper.Data['instTyp'] = response['InstanceType']['Value']
@helper.delete
def no_op(_, __):
    pass

def handler(event, context):
    helper(event, context)
