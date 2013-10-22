import jinja2
import webapp2
import cgi
import datetime
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Home(webapp2.RequestHandler):

    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('home.html')
    	self.response.write(template.render())