import webapp2
import os
import datetime
from tasks import *
from pages import *
import api

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
    ('/feed', Feed),
    ('/api/login', api.Login),
    ('/api/newpost', api.NewPost),
    ('/api/postimage', api.PostImage),
    ('/api/send_recover', api.SendRecover),
    ('/api/recovery', api.Recovery),
    ('/api/delete_post', api.DeletePost),
    ('/api/yummy', api.Yummy),
    ('/api/register_verification', api.RegisterVerification),
    ('/cleantokens', CleanTokens),
    ('/recovery', Recovery)
], debug=True, config=config)