from google.appengine.ext import db
from user import User
from post import Post

#Class comment
class Comment(db.Model):
	user = db.ReferenceProperty(User)
	post = db.ReferenceProperty(Post)
	content = db.TextProperty()
	date = db.DateProperty(auto_now=True)