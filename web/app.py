import webapp2
import os
import datetime
from pages import *

application = webapp2.WSGIApplication([
    ('/', Home),
    ('/login', Login),
    ('/register', Register)
], debug=True)



