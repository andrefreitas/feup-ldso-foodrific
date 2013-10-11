from google.appengine.ext import ndb

#Class admin
class Admin(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    password = ndb.StringProperty(indexed=False)