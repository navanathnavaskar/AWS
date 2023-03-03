#!/opt/homebrew/bin/python3

import boto3
from botocore.exceptions import ClientError

class AWS_DYNAMODB_HANDLER:
    def __init__(self, tablename):
        self.dyndb_client = boto3.resource("dynamodb")
        self.dtable = self.dyndb_client.Table(tablename)
        
    def insert_item(self, rno, name, age, feepaid):
        response = self.dtable.put_item(
        Item = {
                'roll_no': rno,
                'Name': name,
                'Age': age,
                'FeePaid': feepaid
            }
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True
        else:
            return False
    
    