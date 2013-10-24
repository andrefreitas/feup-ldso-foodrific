import webapp2
import cgi
from base_handler import *
from datastore import *

class Logout(BaseHandler):

    def get(self):
    	del self.session["user"]