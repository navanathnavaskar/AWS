# AWS and Elastic Container Service(ECS)

Cluster – A cluster is a logical grouping of tasks or services
Task Definition – The task definition is a text file in JSON format that describes one or more containers, up to a maximum of ten, that form your application. It can be thought of as a blueprint for your application.
Service allows you to run and maintain a specified number of instances of a task definition simultaneously in an AWS ECS cluster
Task – is the instantiation of a task definition within a cluster
An ECS cluster launches the groups of infrastructure resources (services and tasks). The infrastructure capacity is provided by AWS ECS EC2 based and Fargate, where Fargate is a much-preferred option for lower management overhead.

## Cluster Management
#### ECH_HANDLER class has 4 methods to manage cluster
#### 1. Create object with cluster name
###### obj = ECS_HANDLER("NewWebServicesCluster")
#### 2. create_cluster() method
###### This method will create cluster with name given while creating object
#### 3. describe_cluster() method
###### This method will describe cluster
#### 4. list_clusters() method
###### This method will list all clusters in given region
#### 5. checkif_cluster_exists() method
###### This method checks if cluster already exists
#### 6. delete_cluster() method
###### This method deletes cluster 