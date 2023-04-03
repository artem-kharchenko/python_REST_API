import requests
from array import *

payload = {
    "method0": "GET",
    "method1": "POST",
    "method2": "PUT",
    "method3": "DELETE"
    }

print(payload["method1"])

i = 0
#method = ["GET", "POST", "PUT", "DELETE"]
#while i < 4:
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={method}payload[1])
    #    print(f"using i_value: {i} and method: {method[i]}  response: {response.text}")
#   i += 1
#else:
#   print("Verification finished")


#method: POST, GET, PUT, DELETE
#response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
#response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
#response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=payload)
#print(response.text)

#i = 0
#method = ["GET", "POST", "PUT", "DELETE"]
#while i < 4:
    #    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload[1])
    #    print(f"using i_value: {i} and method: {method[i]}  response: {response.text}")
#   i += 1
#else:
#   print("Verification finished")