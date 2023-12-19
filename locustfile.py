import time 
from locust import HttpUser, task, between

class NumericalIntegrationUser(HttpUser):
   @task
   def numerical_integration(self):
       self.client.get("/integrate?lower=0&upper=3.14159")

   wait_time = between(1, 2)
