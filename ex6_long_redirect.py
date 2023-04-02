import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
history_info = response.history[0]
last_response = response

print(history_info.url)
print(last_response.url)

