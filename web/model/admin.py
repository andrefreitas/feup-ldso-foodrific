from google.appengine.ext import ndb

#Class admin
class Admin(ndb.Model):
    name = ndb.UserProperty()
    email = ndb.StringProperty(indexed=False)
    password = ndb.DateTimeProperty(auto_now_add=True)