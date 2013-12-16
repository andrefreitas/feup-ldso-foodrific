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
            params = {"user": user}
            template = JINJA_ENVIRONMENT.get_template('profile.html')
            self.response.write(template.render(params))
        else:
            return self.redirect("/")