import webapp2
import cgi
from base_handler import *
from datastore import *

class Logout(BaseHandler):

    def get(self):
    	for key in self.session.keys():
    		del self.session[key]
    	return self.redirect('/')