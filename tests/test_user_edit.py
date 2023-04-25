import requests
from python_REST_API.lib.base_case import BaseCase
from python_REST_API.lib.assertions import Assertions
class TestUserEdit(BaseCase):
    def test_get_user_details_not_auth(self):

        response = requests.get("https://playground.learnqa.ru/api/user/69265")
        print(response.content)
