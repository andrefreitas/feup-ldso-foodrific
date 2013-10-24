import webapp2
import cgi

from base_handler import *

class Login(BaseHandler):

    def post(self):
    	email = self.request.post("email")
    	password = self.request.post("password")
    	self.response.write("email " + email)
    	self.response.write("password " + password)