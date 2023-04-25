import requests
from python_REST_API.lib.base_case import BaseCase
from python_REST_API.lib.assertions import Assertions
class TestUserGet(BaseCase):
    def test_get_user_details_not_auth(self):

        response = requests.get("https://playground.learnqa.ru/api/user/69265")
        print(response.content)
        print(response.status_code)
        print(response.text)
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstname")
        Assertions.assert_json_has_not_key(response, "lastname")

    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email':'vinkotov@example.com',
            'password':'1234'
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = requests.get(f"https://playground.learnqa.ru/api/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response2, expected_fields)



#        assert response.status_code == 400, f"Unexpected status code {response.status_code}"
#        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"