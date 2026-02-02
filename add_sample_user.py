import boto3

# Kết nối DynamoDB local

dynamodb = boto3.resource(
    "dynamodb",
    region_name="ap-southeast-1",
    endpoint_url="http://localhost:8000",
    aws_access_key_id="dummy",
    aws_secret_access_key="dummy"
)

table = dynamodb.Table("users-local")

# Thêm user mẫu
user_item = {
    "id": "1",
    "name": "Demo User",
}

response = table.put_item(Item=user_item)
print("PutItem succeeded:", response)
