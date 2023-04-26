import requests
from python_REST_API.lib.base_case import BaseCase
from python_REST_API.lib.assertions import Assertions
import pytest

class TestUserDelete(BaseCase):
    def test_delete_admin_user(self):
        # Login
        login_data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        # Delete
        response2 = requests.delete(
            f"https://playground.learnqa.ru/api/user/2",
            headers={"x-csrf-token":token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_code_status(response2, 400)
        Assertions.assert_content(
            response2,
            "Error message. User could not be deleted")

        # Get. Verify that user was not deleted

        response4 = requests.get(
            f"https://playground.learnqa.ru/api/user/2",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_code_status(response4, 200)

    def test_delete_just_created_user(self):
        # Register
        register_data = self.prepare_registration_data()

        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)


        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        # Login
        login_data = {
            "email": email,
            "password": password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)


        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # Delete

        response3 = requests.delete(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token":token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_code_status(response3, 200)

        # Get

        response4 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )


        Assertions.assert_code_status(response4, 404)
        Assertions.assert_content(response4, "User was not found")

    def test_edit_just_created_user_without_authorization(self):
        # Register
        register_data = self.prepare_registration_data()

        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)


        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id = self.get_json_value(response1, "id")

        # Edit
        new_name = "Changed Name"

        response2 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            data={"firstName": new_name}
        )


        Assertions.assert_code_status(response2, 400)
        Assertions.assert_content(response2, "Token was not found")

    def test_delete_user_by_other_authorizated_user(self):
        # Register for User1
        user1_register_data = self.prepare_registration_data()

        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=user1_register_data)


        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user1_email = user1_register_data["email"]
        user1_first_name = user1_register_data["firstName"]
        user1_password = user1_register_data["password"]
        user1_user_id = self.get_json_value(response1, "id")

        # Register for User2
        user2_register_data = self.prepare_registration_data()

        response2 = requests.post("https://playground.learnqa.ru/api/user/", data=user2_register_data)


        Assertions.assert_code_status(response2, 200)
        Assertions.assert_json_has_key(response2, "id")

        user2_email = user2_register_data["email"]
        user2_first_name = user2_register_data["firstName"]
        user2_password = user2_register_data["password"]
        user2_user_id = self.get_json_value(response2, "id")

        # Login User2
        login_data = {
            "email": user2_email,
            "password": user2_password
        }

        response3 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)


        user2_auth_sid = self.get_cookie(response3, "auth_sid")
        user2_token = self.get_header(response3, "x-csrf-token")

        #  Verify that User1 could not be deleted by User2 (Authorization by User2)
        new_name = "Changed Name"

        response4 = requests.delete(
            f"https://playground.learnqa.ru/api/user/{user1_user_id}",
            headers={"x-csrf-token":user2_token},
            cookies={"auth_sid": user2_auth_sid},
        )

        Assertions.assert_code_status(response4, 400)
        Assertions.assert_content(response4, "Token was not found")

        # Login User1. Verify that User2 was not deleted
        login_data = {
            "email": user2_email,
            "password": user2_password
        }

        response5 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)


        Assertions.assert_code_status(response5, 200)
        Assertions.assert_json_has_key(response5, "user_id")