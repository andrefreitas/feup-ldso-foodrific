from google.appengine.ext import db
from user import User
from post import Post

# ----------------- CLASS YUMMY -----------------
class Yummy(db.Model):	
	user = db.ReferenceProperty(User, required=True)
	post = db.ReferenceProperty(Post, required=True)

# ----------------- FUNCTIONS YUMMY -----------------
def doYummy(user, post):
	yummy = Yummy(user=user, post=post)
	yummy.put()

def undoYummy(user, post):
	return
	#TODO

def getPostYummys(post):
	return
	#TODO