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

class Feed(BaseHandler):

    def get(self):
    	if(self.isLoggedIn()):
    		template = JINJA_ENVIRONMENT.get_template('feed.html')
    		self.response.write(template.render())
    	else:
    		return self.redirect('/')