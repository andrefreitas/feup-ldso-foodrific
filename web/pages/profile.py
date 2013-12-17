import jinja2
import webapp2
import cgi
import datetime
import os
from base_handler import *
from datastore import *

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Profile(BaseHandler):

    def get(self):
        user_id = int(self.request.get("user"))
        user = searchUserByID(user_id)
        if(user):
            genderDict = {"m" : "Man", "f" : "Woman"}
            profileOwner = self.get_session_user_id() == user_id
            is_following = isUserFollowing(self.get_session_user_id(), user_id)
            params = {"user": user, 
                      "profileOwner" : profileOwner,
                      "user_id" : self.get_session_user_id(),
                      "is_following" : is_following }
            template = JINJA_ENVIRONMENT.get_template('profile.html')
            self.response.write(template.render(params))
        else:
            return self.redirect("/")