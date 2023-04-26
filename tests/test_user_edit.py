import requests
from python_REST_API.lib.base_case import BaseCase
from python_REST_API.lib.assertions import Assertions
class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        #Register
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        user_id = self.get_json_value(response1,"id")
        password = register_data['password']

        #Login
        login_data = {
            'email':email,
            'password': password
        }
        response2 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, 'auth_sid')
        token = self.get_header(response2, 'x-csrf-token')

        #Edit
        new_name = "Changed Name"

        response3 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token":token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 200)

        #Get
        response4 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )
    # 1. change user details while being unauthorized
    def test_edit_user_without_authorization(self):
        # 1.1 Register
        register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=register_data)

        Assertions.assert_code_status(response1,200)
        Assertions.assert_json_has_key(response1,"id")

        user_id = self.get_json_value(response1,"id")

        # 1.2 EDIT
        new_name = "Changed Name"

        response2 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response2,400)
        Assertions.assert_content(response2,"Auth token not supplied")


    # 2. change user data while being authorized by another user
    def test_edit_user_authorized_by_another_user(self):
        # 2.1 Register User1
        user1_register_data = self.prepare_registration_data()
        response1 = requests.post("https://playground.learnqa.ru/api/user/", data=user1_register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user1_email = user1_register_data['email']
        user1_first_name = user1_register_data['firstName']
        user1_user_id = self.get_json_value(response1, "id")
        user1_password = user1_register_data['password']

        # 2.2 Register User2
        user2_register_data = self.prepare_registration_data()
        response2 = requests.post("https://playground.learnqa.ru/api/user/", data=user2_register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user2_email = user2_register_data['email']
        user2_first_name = user2_register_data['firstName']
        user2_user_id = self.get_json_value(response1, "id")
        user2_password = user2_register_data['password']

        # 2.3 Login User2
        login_data = {
            "email": user2_email,
            "password": user2_password
        }

        response3 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        user2_auth_sid = self.get_cookie(response3, 'auth_sid')
        user2_token = self.get_header(response3, 'x-csrf-token')


        #2.4 Verify that User2 could not update User1 data (Login by User2)
        new_name = "Changed Name"
        response4 = requests.put(f"https://playground.learnqa.ru/api/user/{user1_user_id}",
            headers={"x-csrf-token": user2_token},
            cookies={"auth_sid": user2_auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response4, 400)
        Assertions.assert_content(response4, "Auth token not supplied")

        # 2.4 Login User1
        login_data = {
            "email": user1_email,
            "password": user1_password
        }

        response5 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        user1_auth_sid = self.get_cookie(response5, 'auth_sid')
        user1_token = self.get_header(response5, 'x-csrf-token')

        #2.5 Verify that User1 data should not updated

        response5 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user1_user_id}",
            headers={"x-csrf-token": user1_token},
            cookies={"auth_sid": user1_auth_sid},
        )

        Assertions.assert_json_value_by_name(
            response5,
            "firstName",
            user1_first_name,
            "Wrong name of the user after edit"
        )

    def test_edit_user_with_wrong_data(self, wrong_param):

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

        # Edit

        if wrong_param == "email":
            data_for_edit = {"email": "wrong_email.coogle.com"}
        else:
            data_for_edit = {"firstName": "q"}

        response3 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token":token},
            cookies={"auth_sid": auth_sid},
            data=data_for_edit
        )

        Assertions.assert_code_status(response3, 400)
        if wrong_param == "email":
            Assertions.assert_content(response3, "Wrong email format")
        elif wrong_param == "firstName":
            Assertions.assert_json_value_by_name(
                response3,
                "error",
                "To short field 'firstName'",
                "To short value 'firstName'")

    #4. Verify that data wasn't edited with wrong param

        response4 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            first_name,
            f"'firstName' param should not be updated"
            f"current value: {first_name} "
        )
        Assertions.assert_json_value_by_name(
            response4,
            "email",
            email,
            f"param 'email' should not be updated"
            f"current value: {email}"
        )