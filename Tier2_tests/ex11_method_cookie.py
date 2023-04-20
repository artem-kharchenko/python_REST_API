import requests

response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
cookie_value = response.cookies
print(f"Cookie in the response equals to: {cookie_value}")

response_data = {'cookie':cookie_value}
assert 'cookie' in response_data, "There is no cookie in the response"