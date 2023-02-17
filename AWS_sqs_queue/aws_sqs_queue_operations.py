###############################################################################
# Class : AWS_SQS_HANDLER
# Inputs:
#       1. queuename - Name of the queue to create or connect
#       2. regionnmae - name of the region in which queue created
# Functions:
#       1. Create QUEUE if not exist
#       2. Get URL of the queue
#       3. Send message to queue
#       4. Get message from queue
#       5. Set attributes of the queue
#       6. Clean the queue
#
# Auther: Navanath Navaskar <navanathnavaskar@gmail.com>
#
###############################################################################

#!/opt/homebrew/bin/python3

import boto3
import json
from botocore.exceptions import ClientError

class AWS_SQS_HANDLER:
    
    def __init__(self, queuename, regionname) -> None:
        self.queue_name = queuename
        self.region_name = regionname
        self.queue_url = None
        self.sqs_client = boto3.client("sqs", region_name=self.region_name)
    
    def create_aws_queue(self):
        print("Started creating queue...")
        try:
            response = self.sqs_client.create_queue(
                QueueName = self.queue_name,
                Attributes = {
                    "DelaySeconds" : "0",
                    "VisibilityTimeout" : "60"
                }
            )
        except ClientError as e:
            print("Error : %s "% e)
            if "QueueAlreadyExists" in str(e):
                return
            else:
                print("Need to check issue. Hence exiting...")
                exit(1)
        
        #print(response)
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            print("Successfully created AWS Queue with below details: ")
            print("Queue Url  : " + response['QueueUrl'])
            self.queue_url = response['QueueUrl']
            print("Queue Name : " + self.queue_name)
            return True
        else:
            print("Failed to create AWS Queue.")
            return False

    def get_queue_url(self):
        print("Getting queue url...")
        response = self.sqs_client.get_queue_url(
            QueueName = self.queue_name,
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            self.queue_url = response['QueueUrl']
            print("Received Queue URL.")
            return True
        else:
            print("Failed to get URL for SQS queue.")
            return False
    
    def send_message(self, name):
        message = {'Name': name}
        response = self.sqs_client.send_message(
            QueueUrl = self.queue_url,
            MessageBody = json.dumps(message)
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True
        else:
            return False
    
    def receive_message(self):
        response = self.sqs_client.receive_message(
            QueueUrl = self.queue_url,
            MaxNumberOfMessages = 1,
            WaitTimeSeconds = 10,
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return response.get("Messages", [])
        else:
            return None
    
    def delete_message(self, receipthandle):
        response = self.sqs_client.delete_message(
            QueueUrl = self.queue_url,
            ReceiptHandle = receipthandle,
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True
        else:
            return False
    
    # Method to set attributes of QUEUE
    def set_queue_attributes(self):
        response = self.sqs_client.set_queue_attributes(
            QueueUrl = self.queue_url,
            Attributes = {
                "DelaySeconds" : "0",
                "VisibilityTimeout" : "300",
            }
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True
        else:
            return False
        
    # Clean queue
    def purge_queue(self):
        response = self.sqs_client.purge_queue(
            QueueUrl = self.queue_url,
        )
        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True
        else:
            return False