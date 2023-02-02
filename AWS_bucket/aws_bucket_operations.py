#!/opt/homebrew/bin/python3

import boto3
from botocore.exceptions import ClientError
import os

s3 = boto3.client("s3")

class AWS_BUCKET_HANDLER:
    def download_file(self, bucketName, filename):
        dirPath = "data/" + filename
        try:
            s3.download_file(Bucket=bucketName, Key=filename, Filename=dirPath)
            print("File downloaded successfully")
        except ClientError as e:
            print("download_file : Unexpected error : %s " % e)
    
    def upload_file(self, bucketName, filename):
        uploadFileName = os.path.basename(filename)
        try:
            s3.upload_file(
                Filename=filename,
                Bucket=bucketName,
                Key=uploadFileName
            )
        except ClientError as e:
            print("upload_file : Unexpected error : %s " % e)
            

abh = AWS_BUCKET_HANDLER()
abh.upload_file("nath-bucket-1000", "data/abc.txt")