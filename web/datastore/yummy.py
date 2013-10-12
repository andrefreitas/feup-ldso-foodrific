from google.appengine.ext import ndb

#Class Yummy
class Yummy(ndb.Model):
	user = ndb.ReferenceProperty(User)
	post = ndb.ReferenceProperty(Post)