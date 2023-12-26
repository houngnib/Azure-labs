# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def downloadData():
    connect_str = 'DefaultEndpointsProtocol=https;AccountName=rychlab1;AccountKey=Ut1JXwvuGb43rF9NwTuHx6wzZ1/y4pZGNcaZzw3x5k762D/zvlZirfXecACvPa0WwDIdTlM5uNSg+AStzaUquw==;EndpointSuffix=core.windows.net'
    container_name = 'map-reduce'

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    try:
        container_client = blob_service_client.get_container_client(container= container_name)
        blob_list = container_client.list_blobs()
        all_strings = []

        for blob in blob_list:
            print("\t" + blob.name)
            file2str = container_client.download_blob(blob.name).readall().decode("utf-8").replace("\r", "").split("\n")
            all_strings.append(file2str)\

        return all_strings
        # Quickstart code goes here

    except Exception as ex:
        print('Exception:')
        print(ex)

def main(name: str) -> str:
    return " ".join([j for sub in downloadData() for j in sub])