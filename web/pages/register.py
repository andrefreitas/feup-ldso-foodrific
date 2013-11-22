import jinja2
import webapp2
import cgi
import datetime
import os
from base_handler import *

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Register(BaseHandler):

    def get(self):
    	if self.isLoggedIn():
    		return self.redirect('/feed')
    	else:
    		template = JINJA_ENVIRONMENT.get_template('register.html')
    		self.response.write(template.render())