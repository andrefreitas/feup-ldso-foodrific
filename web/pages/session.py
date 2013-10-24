import webapp2
import cgi
from base_handler import *
from datastore import *

class Session(BaseHandler):

    def get(self):
    	if(self.isLoggedIn()):
    		self.response.write(self.session.get("user"))
    	else:
    		self.response.write("off")