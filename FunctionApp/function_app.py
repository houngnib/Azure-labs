import azure.functions as func
import numpy as np
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

def numerical_integration(lower, upper, N):
 x = np.linspace(lower, upper, N)
 y = np.abs(np.sin(x))
 area = np.sum(y) * (upper - lower) / N
 return area

@app.route(route="numericalinte")
def numericalinte(req: func.HttpRequest) -> func.HttpResponse:
   logging.info('Python HTTP trigger function processed a request.')

   lower = float(req.params.get('lower', '0'))
   upper = float(req.params.get('upper', '3.14159'))

   N_values = [10, 100, 1000, 10000, 100000, 1000000]
   results = [numerical_integration(lower, upper, N) for N in N_values]

   return func.HttpResponse(str(results))
