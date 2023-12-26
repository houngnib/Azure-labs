# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging


def main(name: list) -> list:
    buffer = {}
    toRet = []

    for value in name:
        if value[0] in buffer.keys():
            buffer[value[0]] += [1]
        else:
            buffer[value[0]] = [1]

    for key in buffer.keys():
        toRet.append([key, buffer[key]])

    return toRet
