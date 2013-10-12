from google.appengine.ext import ndb

#Class admin
class Admin(ndb.Model):
    name = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(indexed=False, required=True)