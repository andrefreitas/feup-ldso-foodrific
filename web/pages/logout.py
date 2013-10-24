import webapp2
import cgi
from base_handler import *
from datastore import *

class Logout(BaseHandler):

    def get(self):
    	if "user" in self.session:
    		del self.session["user"]