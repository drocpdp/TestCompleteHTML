import requests
import json
import os
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

	def form_values(self):
		test_cases = self.get_all_test_cases()
		output_html = "<html>"
		output_html += "<table style='table-layout: fixed;font-size:9px;' border='1'>"
		for test_case in test_cases:
			output_html += "<tr>"
			output_html += "<td style='width:300px;'>TITLE: <b>%s</b><br/><br/></td>" % (test_case['title'])
			if 'test_steps' in test_case:
				steps_output = ''
				steps_expected = ''		
				for step in test_case['test_steps']:
					if 'step' in step:
						steps_output += "<b>STEP</b>: %s<br/>" % (step['step'])
					if 'expected_result' in step:
						steps_expected += "<b>EXPECTED</b>: %s<br/>" % (step['expected_result'])
				output_html += "<td style='width:130px;'>%s</td><td style='width:130px;'>%s</td>" % (steps_output, steps_expected)
			output_html += "</tr>"
		output_html += "</table>"
		output_html += "</html>"
		if os.path.exists("C:/Users/C11904A/Desktop/test.html"):
			f = file("C:/Users/C11904A/Desktop/test.html", "r+")
		else:
			f = file("C:/Users/C11904A/Desktop/test.html", "w")
		f.write(output_html)
		f.close()

if __name__=="__main__":
	Implementation().form_values()