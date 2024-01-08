
<img width="1433" alt="Screenshot 2024-01-08 at 9 11 07 AM" src="https://github.com/Rupesh-132/End-To-End-MLOPs-Credit_Card_Fraud_Detection/assets/79595858/0453de4d-fc0f-419f-b4e0-ce63d5ca7643">

## How to run?
Clone the repository

```bash
https://github.com/Rupesh-132/End-To-End-MLOPs-Credit_Card_Fraud_Detection
```
### STEP 01- Create a virtual environment after opening the repository


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


### dagshub : Add your dagshub credentials here.
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=
MLFLOW_TRACKING_USERNAME=
MLFLOW_TRACKING_PASSWORD=
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=

export MLFLOW_TRACKING_USERNAME=

export MLFLOW_TRACKING_PASSWORD=

```



## AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment --(search IAM-create user)

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image -- Search ECR(create repo)
    - Save the URI: 160179019096.dkr.ecr.us-east-1.amazonaws.com/credit-card-fraud-detection-mlops

	
## 4. Create EC2 machine (Ubuntu) 
    -(search-EC2-service for virtual machine - Click on Launch instance)
    -(give name)
    -(select-Ubuntu)
    -(select-instance type- for this project-t2.large is sufficient)
    -(create-key-pair-give name-with default settings)
    -(From network settings-check all boxes)
    -(keep configuration size at least 32 GiB)
    -(Click on Launch instance)
    -(After instance creation click on View all Instances)
    -(click on instance id)
    -(click on connect button-keep the default settings and click on connect)
    -(you can see one terminal opening)
    -(Now proceed to step-5 and install all the dependencies)

## 5. Open EC2 and Install docker in EC2 Machine:

	#optional

	sudo apt-get update -y

	sudo apt-get upgrade(In case any pop-up screen appears just hit enter button from keyboard)
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu
    check docker version  (docker --version) -
    
    Now proceed to step-6
	newgrp docker
	
## 6. Configure EC2 as self-hosted runner:
    Go to your project on Github
    setting>actions>runner>new self hosted runner> choose os(linux for current proj)> then run all the commands one by one in AWS command line
    - Press enter for default
    - Enter the name of runner as (self-hosted)
    - Run last-command ./run.sh - (connected to github-listening to jobs-congratulations for successful connections)
     Proceed to step-7

# 7. Setup github secrets:
    
    - Go to your project on github
    - Go to settings > secrets and variables > Actions > New repository secrets

    Add  the below mentioned Key one by one

    AWS_ACCESS_KEY_ID= get this from the downloaded csv file

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  160179019096.dkr.ecr.us-east-1.amazonaws.com

    ECR_REPOSITORY_NAME = credit-card-fraud-detection-mlops




## About MLflow 
MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & tagging your model

- If you want to create your own project you can follow the below workflow to write your custom code.
## Workflows : Follow the below steps while wrting the code for each modul this is make it look very easy.
1. Update config.yaml
2. Update schema.yaml
3. update params.yaml
4. update the entity
5. update the configuration manager in src config
6. update the strategies
7. update the pipeline
8. update the main.py
9. update the app.py



