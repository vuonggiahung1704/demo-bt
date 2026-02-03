# config/settings.py
import os

ENV = os.getenv("ENV", "local")
IS_LOCAL = ENV == "local"
AWS_REGION = os.getenv("AWS_REGION", "ap-southeast-1")
DYNAMODB_ENDPOINT = os.getenv("DYNAMODB_ENDPOINT", "http://host.docker.internal:8000")
