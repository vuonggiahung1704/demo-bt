# config/dynamodb.py
import boto3
from config.settings import AWS_REGION, DYNAMODB_ENDPOINT

dynamodb = boto3.resource(
    "dynamodb",
    region_name=AWS_REGION,
    endpoint_url=DYNAMODB_ENDPOINT,
    aws_access_key_id="dummy",
    aws_secret_access_key="dummy"
)
