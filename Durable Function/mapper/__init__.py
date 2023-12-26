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


def main(name: tuple) -> list:

    # # Retrieve the connection string for use with the application. The storage
    # # connection string is stored in an environment variable on the machine
    # # running the application called AZURE_STORAGE_CONNECTION_STRING. If the environment variable is
    # # created after the application is launched in a console or with Visual Studio,
    # # the shell or application needs to be closed and reloaded to take the
    # # environment variable into account.
    # connect_str = os.getenv('DefaultEndpointsProtocol=https;AccountName=mapreduceadi;AccountKey=ptkxCEvHE8yOjOrgpwF1rp/gMffhnyu3ItYjHv7XNTVUnND6IZ3OXengsk6WsnwjenOc575LC8DM+AStNIVWfQ==;EndpointSuffix=core.windows.net')

    # # Create the BlobServiceClient object
    # blob_service_client = BlobServiceClient.from_connection_string(connect_str)


    # try:
    #     print("Azure Blob Storage Python quickstart sample")

    # # Quickstart code goes here

    # except Exception as ex:
    #     print('Exception:')
    #     print(ex)http://localhost:7071/runtime/webhooks/durabletask/instances/91d98ff037164d21b330ffba75d4c739?taskHub=TestHubName&connection=Storage&code=9Ka1V6q0adSD90a_vgljU6nu4b_HLOYaNQ_e5cbcx7ODAzFuCt6qBA==

    sentence = name['1'].split(' ')
    toRet = []
    for value in sentence:
        toRet.append([value, "1"])

    return toRet
