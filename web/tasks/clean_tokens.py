import webapp2
from google.appengine.ext import db
from datastore import user

KEYDEF = "TreyYWtmtDM33VbontpHbQJ63eGwByfz6N1INuaJeJ0ZQ7qxWs3AdB0o5bLlGOFc"

class CleanTokens(webapp2.RequestHandler):
    
    def get(self):
        key = self.request.get("key")
        if(key == KEYDEF):
            user_query = db.GqlQuery("SELECT * FROM User")
            user_verify = user_query.fetch(1000)
            for user in user_verify:
                user.token = ""
                db.put(user_verify)