from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "your_access_key_id")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "your_secret_access_key")

    # S3 bucket params
    S3_BUCKET = os.getenv("S3_BUCKET_NAME", "your_bucket_name")
    S3_BUCKET_KEY_PREFIX = os.getenv("S3_BUCKET_KEY_PREFIX", "your_bucket_prefix")

    # OIDC config
    OIDC_CLIENT_SECRETS = os.getenv("OIDC_CLIENT_SECRETS", "../client_secrets.json")
    SECRET_KEY = os.getenv("OKTA_CLIENT_SECRET", "your_client_secret")
    OVERWRITE_REDIRECT_URI = os.getenv("OKTA_REDIRECT_URI", "http://localhost:5000/auth/callback")
    TESTING = True
    DEBUG = True
    # OIDC_ENABLED = False
    # OKTA_CLIENT_ID = os.getenv('OKTA_CLIENT_ID', 'your_auth_client_id')
