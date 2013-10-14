from google.appengine.ext import db

#Class admin
class Admin(db.Model):
    name = db.StringProperty(required=True)
    email = db.StringProperty(required=True)
    password = db.StringProperty(indexed=False, required=True)