#!/opt/homebrew/bin/python3

from aws_sqs_queue_operations import AWS_SQS_HANDLER

queue_name = "nath-sqs-queue-1001"
region = "eu-west-1"
ash = AWS_SQS_HANDLER(queue_name, region)
# Create queue
ash.create_aws_queue()
# Get Queue URL
ash.get_queue_url()
#Send message to Queue
if ash.send_message("Navanath"):
    print("Successfully sent message in queue.")
else:
    print("Failed to send messgae in queue.")

messages = ash.receive_message()
if messages:
    for msg in messages:
        print("Received Message : " + msg['Body']) 
        receiptHandle = msg['ReceiptHandle']
        print("Trying to delete message from queue...")
        if ash.delete_message(receiptHandle):
            print("Message deleted successfully.")
        else:
            print("Failed to delete message successfully.")
else:
    print("Failed to get message.")
    
if ash.set_queue_attributes():
    print("Successfully changed queue attributes.")
else:
    print("Failed to change queue attributes.")

if ash.purge_queue():
    print("Successfully Cleaned Queue.")
else:
    print("Failed to clean queue.")