#!/opt/homebrew/bin/python3

import boto3
from botocore.exceptions import ClientError

AWS_REGION = "eu-west-1"

class SNS_HANDLER:
    def __init__(self) -> None:
        self.sns = boto3.client("sns", region_name=AWS_REGION)
        self.topic = ""
        self.topic_arn = ""
    
    def create_topic(self, topic_name):
        try:
            self.topic = self.sns.create_topic(Name=topic_name)
            print("Created topic {topic_name} successsfully.")
            self.topic_arn = self.topic['TopicArn']
        except ClientError:
            print("Failed to create topic {topic_name}")
            raise
        else:
            return self.topic
            
    def list_topics(self):
        try:
            topic_paginator = self.sns.get_paginator('list_topics')
            p_itr = topic_paginator.paginate().build_full_result()
            all_topics = []
            
            for page in p_itr['Topics']:
                all_topics.append(page['TopicArn'])
        except ClientError:
            print("Failed to list topics")
            raise
        else:
            print("Following are the topics : ")
            for topic in all_topics:
                print(topic)    
            
    def subscribe_to_topic(self, protocol, endpoint):
        if self.topic_arn == "":
            print("Topic not created. Create topic first and then subscribe.")
            return
        try:
            subscription = self.sns.subscribe(TopicArn=self.topic_arn, Protocol=protocol, Endpoint=endpoint, ReturnSubscriptionArn=True)['SubscriptionArn']
            print("Successfully subscribed {endpoint} to topic {self.topic_arn}")
        except ClientError:
            print("Failed to subscribe for {endpoint}")
            raise
        else:
            return subscription
        
    def list_subscriptions_of_topic(self):
        try:
            paginator = self.sns.get_paginator('list_subscriptions_by_topic')
            p_itr = paginator.paginate(TopicArn=self.topic_arn, PaginationConfig={'MaxItems': 100})
            
            for page in p_itr:
                print("Subscriptions are : ")
                for sub in page['Subscriptions']:
                    print(sub)
        except ClientError:
            print("Failed to get list of subscriptions")
            raise
        
    def publish_message(self, message, subject):
        try:
            rersponse = self.sns.publish(
                TopicArn=self.topic_arn,
                Message=message,
                Subject=subject,
            )['MessageId']
            print("Successfully pusblished message")
        except ClientError:
            print("Failed to pusblish message in topic")
            raise
                    
SH = SNS_HANDLER()
print(SH.create_topic("nath_sns_test"))
SH.list_topics()
SH.subscribe_to_topic("email", "navanathnavaskar@gmail.com")
SH.list_subscriptions_of_topic()
SH.publish_message("Hi Navanath, This is offfer for you", "Test Message for AWS SNS")

