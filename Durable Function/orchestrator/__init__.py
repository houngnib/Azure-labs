# This function is not intended to be invoked directly. Instead it will be
# triggered by an HTTP starter function.
# Before running this sample, please:
# - create a Durable activity function (default name is "Hello")
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import json

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    dataOut = yield context.call_activity('GetInputData', 'test')

    mapOut = yield context.call_activity("mapper", {"1": dataOut})

    shufOut = yield context.call_activity('shuffler', mapOut)

    toRet = []
    for word in shufOut:
       toRet.append(context.call_activity('reducer', word))
    redOut = yield context.task_all(toRet)

    return redOut

main = df.Orchestrator.create(orchestrator_function)