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

class Recovery(BaseHandler):

    def get(self):
        if self.isLoggedIn():
            return self.redirect('/feed')
        else:
            token = cgi.escape(self.request.get('token'))
            
            template_values = {
                'token': token
            }
            
            template = JINJA_ENVIRONMENT.get_template('recovery.html')
            self.response.write(template.render(template_values))