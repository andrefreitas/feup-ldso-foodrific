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
    ('/login_handler', LoginHandler),
    ('/register_handler', RegisterHandler),
    ('/edit_profile_handler', EditProfileHandler),
    ('/login', Login),
    ('/register', Register),
    ('/logout', Logout),
    ('/session', Session),
    ('/feed', Feed),
    ('/send_recover', SendRecoverHandler),
    ('/show_profile', ShowProfile),
    ('/search', SearchResults),
    ('/api/login', api.Login),
    ('/api/newpost', api.NewPost),
    ('/api/postimage', api.PostImage),
    ('/api/send_recover', api.SendRecover),
    ('/api/recovery', api.Recovery),
    ('/api/delete_post', api.DeletePost),
    ('/api/delete_user',api.DeleteUser),
    ('/api/edit_post', api.EditPost),
    ('/api/get_post', api.GetPost),
    ('/api/yummy', api.Yummy),
    ('/api/get_avatar', api.GetAvatar),
    ('/api/new_comment', api.NewComment),
    ('/api/delete_comment', api.DeleteComment),
    ('/api/session_data', api.SessionData),
    ('/api/ing_tags', api.IngTags),
    ('/api/register_verification', api.RegisterVerification),
    ('/api/verifyPassword', api.PasswordVerification),
    ('/cleantokens', CleanTokens),
    ('/recovery', Recovery)
], debug=True, config=config)