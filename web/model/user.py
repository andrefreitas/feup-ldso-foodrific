from google.appengine.ext import ndb

#Class user
class User(ndb.Model):
    name = ndb.StringProperty(required=True)
    email = ndb.EmailProperty(required=True)
    password = ndb.StringProperty(indexed=False, required=True)
    birthday = ndb.DateProperty(required=True)
    gender = ndb.StringProperty(indexed=False, required=True, choices=set(["m", "f"]))
    photo = ndb.BlobProperty()