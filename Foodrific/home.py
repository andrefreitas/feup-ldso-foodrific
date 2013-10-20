import webapp2
import datetime
import jinja2
import os
import urllib
import google.appengine.api.users
from datastore import user
from datastore import post

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

DEFAULT_EMAIL = 'email'
DEFAULT_PW = 'password'

class MainPage2(webapp2.RequestHandler):

    def post(self):
        email = self.request.post('email', DEFAULT_EMAIL)
        password = self.request.post('password', DEFAULT_PW)
        
        template = JINJA_ENVIRONMENT.get_template('templates/index.html')
        self.response.write(template.render())

application = webapp2.WSGIApplication([
    ('/', MainPage2),
], debug=True)



