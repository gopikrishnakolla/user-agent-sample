from boto3 import client
import botocore

# Create a config
session_config = botocore.config.Config(
  # The value to use in the User-Agent header (overrides)
  user_agent="new_user_agent"
  # The value to append to the current User-Agent header value
  user_agent_extra="new_user_agent"
)

s3 = client(
  's3',
  config=session_config
)

# Make an API call
response = s3.put_object(
  ...
)
