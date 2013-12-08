import webapp2
import cgi
from datetime import date
from base_handler import *
from datastore import *


class EditProfileHandler(BaseHandler):
    
    def post(self):
        # Fields
        type = cgi.escape(self.request.get('type'))

        if type == 'name':
            name = cgi.escape(self.request.get('name'))
            editUserName(self.session["user"], name)
        elif type == 'email':
            email = cgi.escape(self.request.get('email'))
            editUserEmail(self.session["user"], email)
            self.session["user"] = email
        elif type =='birthday':
            birthday = cgi.escape(self.request.get('birthday'))
            birthDay = int(birthday.split("/")[0])
            birthMonth = int(birthday.split("/")[1])
            birthYear = int(birthday.split("/")[2])
            birthTime = date(birthYear, birthMonth, birthDay)
            editUserBirthday(self.session["user"], birthTime)
        elif type == 'gender':
            gender = cgi.escape(self.request.get('gender'))
            editUserGender(self.session["user"], gender)
        elif type == 'password':
            old_password = cgi.escape(self.request.get('old_password'))
            new_password = cgi.escape(self.request.get('password'))
            editUserPassword(self.session["user"], old_password, new_password)
        

        '''
        self.session["user"] = email
        self.session["user_id"] = user_id'''
        self.redirect('/show_profile')
        