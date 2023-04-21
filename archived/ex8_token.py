import requests
import json
import time

#1 create a task
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(response.text)
json_response = response.json()
itoken = json_response["token"]

#2 request with token and check that "status":"Job is NOT ready"
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":itoken})
print(response.text)

#3 wait couple of seconds and check that "status":"Job is ready"
time.sleep(5)

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":itoken})
print(response.text)