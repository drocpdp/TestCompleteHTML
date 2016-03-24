import os
import time
import ConfigParser


class LoginObject(object):

	@property
	def env_var_key(self):
	    return self._env_var_key

	@property
	def config_file_location(self):
	    return self._config_file_location

	@property
	def config_file_section(self):
	    return self._config_file_section
	
	@property
	def user_name(self):
	    return self._user_name

	@property
	def password(self):
	    return self._password
	
	@password.setter
	def password(self, pw):
		self._password = pw

	@user_name.setter
	def user_name(self, user_name):
		self._user_name = user_name
	
	@env_var_key.setter
	def env_var_key(self, value):
		self._env_var_key = value

	@config_file_section.setter
	def config_file_section(self, value):
		self._config_file_section = value

	@config_file_location.setter
	def config_file_location(self, location):
		self._config_file_location = location

	def login(self, user=None, password=None, env_var_key=None, section=None):
		self.env_var_key = "TestCompleteLogin"
		self.config_file_location = os.getenv(self.env_var_key)
		config = ConfigParser.ConfigParser()
		self.config_file_section = "default"
		config.read(self.config_file_location)
		self.user_name = config.get(self.config_file_section, 'user')
		self.password = config.get(self.config_file_section, 'password')
		print self.user_name
		print self.password



if __name__=="__main__":
	LoginObject().login()