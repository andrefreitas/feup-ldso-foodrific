import webapp2
from datastore import user
from datastore import post
import datetime

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Foodrific - Soon available!\n')


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)