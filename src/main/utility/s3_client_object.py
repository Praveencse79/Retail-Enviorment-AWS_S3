import boto3
import os

class S3ClientProvider:
    def _init_(self):
        # Read keys from OS environment variables
        self.aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
        self.aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

        # Create session without hardcoding keys
        self.session = boto3.Session(
            aws_access_key_id=self.aws_access_key,
            aws_secret_access_key=self.aws_secret_key
        )
        self.s3_client = self.session.client('s3')

    def get_client(self):
        return self.s3_client