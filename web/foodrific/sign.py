import webapp2
import jinja2
import os
import cgi

class LoginPage(webapp2.RequestHandler):

    def post(self):
        self.response.write(cgi.escape(self.request.get('email')))
        self.response.write(cgi.escape(self.request.get('password')))

