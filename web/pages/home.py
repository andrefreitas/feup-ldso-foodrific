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

class Home(BaseHandler):

    def get(self):
    	if self.isLoggedIn():
    		return self.redirect('/feed')
    	else:
    		message = self.request.get("message")
    		template_values = {
    			"message" : message
    		}

    		template = JINJA_ENVIRONMENT.get_template('home.html')
    		self.response.write(template.render(template_values))