#!/opt/homebrew/bin/python3

import boto3
from botocore.exceptions import ClientError
import json

REGION = "eu-west-1"

class ECS_HANDLER:
    def __init__(self, clstr_name) -> None:
        self.client = boto3.client("ecs", REGION)
        self.cluster_name = clstr_name
    
    def create_cluster(self):
        try:
            if not self.check_if_cluster_exists():
                response = self.client.create_cluster(clusterName=self.cluster_name)
                print(json.dumps(response, indent=4))
                if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                    print("Successfully created cluster with name : " + response["cluster"]["clusterName"]) 
                else:
                    print("Failed to create cluster.")
            else:
                print("Cluster already exists.")
        except ClientError:
            print("Failed in cluster creation")
            raise
    
    def list_cluster(self):
        try:
            paginator = self.client.get_paginator('list_clusters')
            res_paginator = paginator.paginate(
                PaginationConfig={
                    'PageSize': 50
                }
            )
            print("Following are the Clusters Available : ")
            for each_page in res_paginator:
                for each_arn in each_page["clusterArns"]:
                    print(each_arn)
        except ClientError:
            print("There is some issue in getting list of clusters")
            raise
                
    def check_if_cluster_exists(self):
        try:
            paginator = self.client.get_paginator('list_clusters')
            res_paginator = paginator.paginate(
                PaginationConfig={
                    'PageSize': 50
                }
            )
            for each_page in res_paginator:
                for each_arn in each_page["clusterArns"]:
                    if self.cluster_name in each_arn:
                        return True
            return False
        except ClientError:
            print("There is some issue in getting list of clusters")
            raise

    def describe_cluster(self):
        try:
            response = self.client.describe_clusters(clusters=[self.cluster_name])
            if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                    print(json.dumps(response, indent=4)) 
            else:
                    print("Failed to get data for cluster.")
        except ClientError:
            print("Issue in describing cluster.")
            raise
    
    def delete_cluster(self):
        try:
            response = self.client.delete_cluster(cluster=self.cluster_name)
            if response["ResponseMetadata"]["HTTPStatusCode"] == 200:
                    print(json.dumps(response, indent=4)) 
            else:
                    print("Failed to delete cluster.")
        except ClientError:
            print("Issue in deleteing cluster")
            raise

ecsh = ECS_HANDLER("WebServiceECS")
ecsh.create_cluster()        
ecsh.list_cluster()  
ecsh.describe_cluster()
ecsh.delete_cluster()     
    