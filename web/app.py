import webapp2
import os
import datetime
from pages import *

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'j4KLrj43',
}

application = webapp2.WSGIApplication([
    ('/', Home),
    ('/login', Login),
    ('/register', Register),
    ('/logout', Logout),
    ('/session', Session),
    ('/feed', Feed)
], debug=True, config=config)



