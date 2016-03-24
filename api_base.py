import requests
from login_object import LoginObject


class APIBase(LoginObject):

	def __init__(self):
		return

	def test_request(self):
		self.set_login()
		r = requests.get('https://qacomplete.smartbear.com/rest-api/service/api/v1/projects/91012/tests?format=json&limit=100', auth=(self.user_name, self.password))
		print r.json()
		print type(r.json())


if __name__ == "__main__":
	APIBase().test_request()