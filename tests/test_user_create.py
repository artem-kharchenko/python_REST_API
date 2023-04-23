import requests
from python_REST_API.lib.base_case import BaseCase
from python_REST_API.lib.assertions import Assertions
from datetime import datetime

class TestUserRegister(BaseCase):
    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"
        self.email_without_symbol = f"{base_part}{random_part}{domain}"


    def test_create_user_successfully(self):
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstName':'learnqa',
            'lastName': 'learnqa',
            'email' : self.email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")
    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstName':'learnqa',
            'lastName': 'learnqa',
            'email' : email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_create_user_without_symbol(self):
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstName':'learnqa',
            'lastName': 'learnqa',
            'email' : self.email_without_symbol
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.text == "Invalid email format"

    def test_create_user_with_short_name(self):
        email = "vinkotov@example.com"
        data = {
            'password': '1234',
            'username': 'a',
            'firstName':'a',
            'lastName': 'learnqa',
            'email' : email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "The value of 'username' field is too short", f"Unexpected response content {response.content}"

    def test_create_user_with_long_name(self):
        email = "vinkotov@example.com"
        data = {
            'password': '1234',
            'username': 'abdqwertyuiopasdfghjklzxcvbnmtabdqwertyuiopasdfghjklzxcvbnmtabdqwertyuiopasdfghjklzxcvbnmttyhgfrtyhgabdqwertyuiopasdfghjklzxcvbnmtabdqwertyuiopasdfghjklzxcvbnmtabdqwertyuiopasdfghjklzxcvbnmttyhgfrtyhgabdqwertyuiopasdfghjklzxcvbnmtabdqwertyuiopasdfghjklzxcvbnmtabdqwertyuiopasdfghjklzxcvbnmttyhgfrtyhg',
            'firstName':'learnqa',
            'lastName': 'learnqa',
            'email' : email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "The value of 'username' field is too long", f"Unexpected response content {response.content}"
