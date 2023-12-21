import time 
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("?name=0,3.14")

   #wait_time = between(1, 2)
