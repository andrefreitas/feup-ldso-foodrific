import webapp2
import cgi
from base_handler import *
from datastore import *

class Login(BaseHandler):

    def get(self):
    	email = self.request.get("email")
    	password = self.request.get("password")
    	self.login(email, password)