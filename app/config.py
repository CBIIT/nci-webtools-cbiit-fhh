import os

class Config:
    AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID', 'your_access_key_id')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', 'your_secret_access_key')

    # S3 bucket params
    S3_BUCKET = os.getenv('S3_BUCKET_NAME', 'your_bucket_name')
    S3_BUCKET_KEY_PREFIX = os.getenv('S3_BUCKET_KEY_PREFIX', 'your_bucket_prefix')
