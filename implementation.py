import requests
import json
from api_base import APIBase

class Implementation(APIBase):

	def __init__(self):
		self.set_login()
		return

	def get_all_test_cases(self):
		results_set = self.test_uri_request('projects/91012/tests?format=json&limit=10000000')
		results = results_set['results']
		test_cases = []
		for test_case in results:
			test_cases.append(test_case)
		return test_cases

	def main(self):
		test_cases = self.get_all_test_cases()
		for test_case in test_cases:
			print '--------------------------------------------------\n'
			print '%s  %s\n' % (test_case['title'],test_case['original_id'])
			if 'test_steps' in test_case:
				for step in test_case['test_steps']:
					if 'step' in step:
						print 'STEP: %s\n' % (step['step'])
					if 'expected_result' in step:
						print 'EXPECTED: %s\n' % (step['expected_result'])

if __name__=="__main__":
	Implementation().main()