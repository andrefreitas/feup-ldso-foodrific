from google.appengine.ext import db
from user import User
from post import Post

#Class Yummy
class Yummy(db.Model):	
	user = db.ReferenceProperty(User, required=True)
	post = db.ReferenceProperty(Post, required=True)