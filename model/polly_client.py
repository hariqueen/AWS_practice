import boto3
from model.config import AWS_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

__all__ = ["create_polly_clien"]

def create_polly_client():
    return boto3.client('polly', 
                        region_name=AWS_REGION,
                        aws_access_key_id=AWS_ACCESS_KEY_ID, 
                        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
