# Machine Learning in the Cloud
An End-To-End Project from Data Preparation to Model Deployment

## Description

## Prerequisites
- A Scaleway Account: https://console.scaleway.com/register
- Scaleway CLI: https://www.scaleway.com/en/docs/manage-cloud-servers-with-scaleway-cli/
- Configured SSH Key: https://www.scaleway.com/en/docs/configure-new-ssh-key/

## Todo:
-[x] Get csv with metadata
-[] Create pipeline (store all images as keras images to a csv via streams)
-[] Store the csv on S3 and under /data
-[] Create a .sh script for automatically running the pipeline
-[] Create an EDA Notebook
-[] Create an Image Data Generator under /model (train, test and validation)
-[] Create a Model under /model
-[] Save the Model under /model and on S3
-[] Create an Inference Notebook?