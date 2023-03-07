#!/opt/homebrew/bin/python3

import boto3
import json
from botocore.exceptions import ClientError

class SECRET_MANAGER_HANDLER:
    def __init__(self):
        self.client = boto3.client("secretsmanager")
        
    def create_secret(self):
        try:
            response = self.client.create_secret(
                Name = 'NathTestSecret',
                SecretString='{"username":"navanath", "password":"aseqw332fsdf"}'
            )
        except ClientError as e:
            print("Exception occured : " + str(e))
            return
    
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print("Successfully added secrets...")
        else:
            print("Failed to add secrets...")
    
    def list_secrets(self):
        response = self.client.list_secrets()
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print("List of Secrets: ")
            print(response['SecretList'])
        else:
            print("Failed to list secrets...")
            
    def get_secrets(self, secretname):
        response = self.client.get_secret_value(
            SecretId = secretname
        )
        
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            secret_data = json.loads(response['SecretString'])
            print("Password: " + secret_data['password'])
        else:
            print("Failed to get secret data")
            
    def delete_secret(self, secretname):
        response = self.client.delete_secret(
            SecretId = secretname,
            RecoveryWindowsInDays=10,
            ForceDeleteWithoutRecovery=False
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print("Successfully deleted secret")
        else:
            print("Failed to delete secret")
    
    def restore_secret(self, secretname):
        response = self.client.delete_secret(
            SecretId = secretname
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print("Successfully restored secret")
        else:
            print("Failed to restore secret")
        

smh = SECRET_MANAGER_HANDLER()
smh.create_secret()
smh.get_secrets('NathTestSecret')