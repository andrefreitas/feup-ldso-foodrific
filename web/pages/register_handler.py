import webapp2
import cgi
from datetime import date
from base_handler import *
from datastore import *


class RegisterHandler(BaseHandler):
    
    def post(self):
        # Fields
        name = cgi.escape(self.request.get('name'))
        email = cgi.escape(self.request.get('email'))
        birthday = cgi.escape(self.request.get('birthday'))
        gender = cgi.escape(self.request.get('gender'))
        password = cgi.escape(self.request.get('password'))
        birthDay = int(birthday.split("/")[0])
        birthMonth = int(birthday.split("/")[1])
        birthYear = int(birthday.split("/")[2])
        birthTime = date(birthYear, birthMonth, birthDay)
        user_id = addUser(name, email, password, gender, birthTime)
        self.session["user"] = email
        self.session["user_id"] = user_id
        self.redirect('/feed')
        