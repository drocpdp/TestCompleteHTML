import os
import time
import ConfigParser


class LoginObject(object):

	@property
	def env_var_key(self):
	    return self.env_var_key_var

	@property
	def config_file_location(self):
	    return self.config_file_location_var

	@property
	def config_file_section(self):
	    return self.config_file_section_var
	
	@property
	def user_name(self):
	    return self.user_name_var

	@property
	def password(self):
	    return self.password_var
	
	@password.setter
	def password(self, pw):
		self.password_var = pw

	@user_name.setter
	def user_name(self, user_name):
		self.user_name_var = user_name
	
	@env_var_key.setter
	def env_var_key(self, value):
		self.env_var_key_var = value

	@config_file_section.setter
	def config_file_section(self, value):
		self.config_file_section_var = value

	@config_file_location.setter
	def config_file_location(self, location):
		self.config_file_location_var = location

	def set_login(self, user=None, password=None, env_var_key=None, section=None):
		self.env_var_key = "TestCompleteLogin"
		self.config_file_location = os.getenv(self.env_var_key)
		config = ConfigParser.ConfigParser()
		self.config_file_section = "default"
		config.read(self.config_file_location)
		self.user_name = config.get(self.config_file_section, 'user')
		self.password = config.get(self.config_file_section, 'password')
