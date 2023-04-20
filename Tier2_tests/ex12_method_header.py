import requests

response = requests.get("https://playground.learnqa.ru/api/homework_header")
print(response.text)
header_value = response.headers
print(f"Headers in the response equal to: {header_value}")

assert 'Date' in header_value, "There are no headers in the response"
assert 'Content-Type' in header_value, "There are no headers in the response"
assert 'Content-Length' in header_value, "There are no headers in the response"
assert 'Connection' in header_value, "There are no headers in the response"








"""
response = requests.get("http://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response is not a JSON format")
"""