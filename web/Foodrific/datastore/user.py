from google.appengine.ext import db

#Class user
class User(db.Model):
    name = db.StringProperty(required=True)
    email = db.EmailProperty(required=True)
    password = db.StringProperty(indexed=False, required=True)
    birthday = db.DateProperty(required=True)
    gender = db.StringProperty(indexed=False, required=True, choices=set(["m", "f"]))
    photo = db.BlobProperty()