import json

String_as_json_format = '{"answer": "Hello, User"}'
obj = json.loads(string_as_json_format)

key = "answer"

if key in obj:
    print(obj[key])
else:
    print(f"Key {key}" is not detected)