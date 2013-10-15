import webapp2
from datastore import user
from datastore import post
import datetime

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Foodrific - Soon available!\n')
        u2 = user.searchUserByName('nome')
        self.response.write(u2[0].gender)

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)