import requests
import json

json_methods = '{"methods":[{"method":"GET"},{"method":"POST"},{"method":"PUT"},{"method":"DELETE"}]}'
obj = json.loads(json_methods)

#Verification of GET method:
i = 0
while i < 4:
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=obj["methods"][i])
    print(f"using i_value: {i} and method: {obj['methods'][i]}  response: {response.text}")
    i += 1
else:
    print("Verification of GET method finished")

#Verification of POST method:
i = 0
while i < 4:
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=obj["methods"][i])
    print(f"using i_value: {i} and method: {obj['methods'][i]}  response: {response.text}")
    i += 1
else:
    print("Verification of POST method finished")

#Verification of PUT method:
i = 0
while i < 4:
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=obj["methods"][i])
    print(f"using i_value: {i} and method: {obj['methods'][i]}  response: {response.text}")
    i += 1
else:
    print("Verification of PUT method finished")

#Verification of DELETE method:
i = 0
while i < 4:
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=obj["methods"][i])
    print(f"using i_value: {i} and method: {obj['methods'][i]}  response: {response.text}")
    i += 1
else:
    print("Verification of DELETE method finished")