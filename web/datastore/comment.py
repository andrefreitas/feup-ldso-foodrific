from google.appengine.ext import ndb

#Class comment
class Comment(ndb.Model):
	user = ndb.ReferenceProperty(User)
	post = ndb.ReferenceProperty(Post)
    content = ndb.TextProperty()
    date = ndb.DateProperty(auto_now=True)