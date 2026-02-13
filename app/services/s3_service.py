import boto3
import os

s3 = boto3.client(
    "s3",
    region_name="eu-north-1",
    aws_access_key_id=os.getenv("S3_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("S3_SECRET_KEY"),
)

BUCKET_NAME = os.getenv("S3_BUCKET")


def upload_file(file_obj, key):
    file_obj.seek(0)
    s3.upload_fileobj(file_obj, BUCKET_NAME, key)
    return key