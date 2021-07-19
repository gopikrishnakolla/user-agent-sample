from boto3 import client
import botocore

# Create a config
session_config = botocore.config.Config(
  # The value to use in the User-Agent header (overrides)
  user_agent='gkolla-ua-test',
  # The value to append to the current User-Agent header value
  user_agent_extra='gkolla-ua-test-append'
)

BUCKET_NAME = 'gkolla-user-agent-testing'
PREFIX = 'python/'

s3 = client(
  's3',
  config=session_config
)

# Make an API call
response = s3.put_object(
  Bucket=BUCKET_NAME,
  Body=b'just some sample text to upload to s3',
  Key=PREFIX+'test1.txt'
)
