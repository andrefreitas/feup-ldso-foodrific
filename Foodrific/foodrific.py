import webapp2
from datastore import data
from datastore import user
import datetime

class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Foodrific - Soon available!\n')
        users = data.searchUserByEmail('email@email.com')
        posts = data.getPostsByUser(users[0].key().id())
        self.response.write(posts[0].title)


application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)