import requests
import json
from login_object import LoginObject


class APIBase(LoginObject):

	def __init__(self):
		self.set_login()

	@property
	def protocol(self):
	    return "https"

	@property
	def host_url(self):
	    return "qacomplete.smartbear.com"

	@property
	def api_service_directive(self):
	    return "rest-api/service/api"

	@property
	def api_version(self):
	    return "v1"
	
	def base_uri(self):
		uri = "%s://%s/%s/%s/" % (self.protocol, self.host_url, self.api_service_directive, self.api_version)
		return uri

	def send_request(self, full_uri):
		r = requests.get(full_uri)
		return r

	def pretty(self, json_content):
		return json.dumps(json_content, sort_keys=True, indent=4, separators=(',', ': '))

	def full_uri(self, uri):
		full_uri = self.base_uri() + uri
		print full_uri
		return full_uri

	def test_uri_request(self, uri):
		requests_object = requests.get(self.full_uri(uri), auth=(self.user_name, self.password))
		json_obj = requests_object.json()
		return json_obj

	def test_request(self):
		results_set = self.test_uri_request('projects/91012/tests?format=json&limit=10000000')
		results = results_set['results']
		for test_case in results:
			print test_case['folder_name']
		for test_case in results:
			print test_case.keys()


if __name__ == "__main__":
	APIBase().test_request()