from google.appengine.ext import ndb

#Class post
class Post(ndb.Model):
    title = ndb.StringProperty()
    photo = ndb.BlobProperty()
    original_date = ndb.DateProperty(auto_now_add=True)
    last_update_date = ndb.DateProperty(auto_now=True)
