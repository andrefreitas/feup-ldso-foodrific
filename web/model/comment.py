from google.appengine.ext import ndb

#Class comment
class Comment(ndb.Model):
    content = ndb.TextProperty()
    date = ndb.DateProperty(auto_now=True)