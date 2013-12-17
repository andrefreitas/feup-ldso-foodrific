import jinja2
import webapp2
import cgi
import datetime
import os
import time
from base_handler import *
from datastore import *

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class ShowProfile(BaseHandler):

    def get(self):
        if(self.isLoggedIn()):
            email = self.get_session_email()
            user_data = searchUserByEmail(email)
            
            gender = "unknown"

            if user_data.gender == 'm':
                gender = "masculino"

            else:
                gender = "feminino"

            template_values = {
                "p_name" : user_data.name,
                "p_email" : user_data.email,
                "p_birthday" : user_data.birthday.strftime("%d/%m/%Y"),
                "p_gender" : gender,
                "user_id" : self.get_session_user_id()
            }
            template = JINJA_ENVIRONMENT.get_template('show_profile.html')
            self.response.write(template.render(template_values))
        else:
            return self.redirect('/')