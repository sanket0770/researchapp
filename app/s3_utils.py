# source: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-examples.html
# the code included here is taken or adapted from the Amazon S3 examples available on Boto3 documentation

import logging
import boto3
from botocore.exceptions import ClientError
class S3Utils:
    
    @staticmethod
    def get_S3_client(region=None):
        if region is None:
            s3_client = boto3.client('s3')
        else:
            s3_client = boto3.client('s3', region_name=region)
        return s3_client

    @staticmethod
    def upload_file(bucket, file_name, object_name=None):
        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = file_name
        # Upload the file
        s3_client = S3Utils.get_S3_client()
        try:
            response = s3_client.upload_file(file_name, bucket, object_name)
            return response
        except ClientError as e:
            logging.error(e)
            return False
        return True
        
        
    