#this is the script use to run locust on VMSS and local machine
#the one use for the Function App is stored in the Function App repo

import time 
from locust import HttpUser, task, between

class NumericalIntegrationUser(HttpUser):
   @task
   def numerical_integration(self):
       self.client.get("/integrate?lower=0&upper=3.14159")

   wait_time = between(1, 2)
