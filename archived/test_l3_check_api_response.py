import requests

class TestApiName:
    def test_api_call(self):
        url = "http://playground.learnqa.ru/api/hello"
        name = 'Jon'
        data = {'name':name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response code"

        response_dict = response.json()
        assert "answer" in response_dict, "There is no field 'answer' in the response"

        expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, "Actual text in the response is not correct"
