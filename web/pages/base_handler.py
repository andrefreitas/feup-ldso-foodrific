import webapp2
from webapp2_extras import sessions
from datastore import *

class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)
 
        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)
 
    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        return self.session_store.get_session()

    def isLoggedIn(self):
        return "user" in self.session

    def login(self, email, password):
        if(loginUser(email, password) != False):
            user = searchUserByEmail(email)
            self.session["user"] = email
            self.session["user_id"] = int(getUserID(email))
            self.session["name"] = user.name
            return True
        return False

    def get_session_user_id(self):
        return self.session["user_id"]

    def get_session_email(self):
        return self.session["user"]
