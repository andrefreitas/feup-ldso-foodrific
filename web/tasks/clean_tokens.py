import webapp2
from google.appengine.ext import db
from datastore import user

class CleanTokens(webapp2.RequestHandler):
    
    def get(self):
        user_query = db.GqlQuery("SELECT * FROM User")
        user_verify = user_query.fetch(1000)
        for user in user_verify:
            user.token = ""
            db.put(user_verify)