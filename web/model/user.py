from google.appengine.ext import ndb

#Class user
class User(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.EmailProperty()
    password = ndb.StringProperty(indexed=False)
    birthday = ndb.DateProperty()
    gender = ndb.StringProperty(indexed=False)

 		