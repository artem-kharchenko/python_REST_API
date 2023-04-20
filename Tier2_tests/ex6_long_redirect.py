import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
history_info0 = response.history[0]
history_info1 = response.history[1]
last_response = response

print(history_info0.url)
print(history_info1.url)
print(last_response.url)




