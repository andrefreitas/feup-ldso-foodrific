from google.appengine.ext import db
from user import User
from post import Post

# ----------------- CLASS YUMMY -----------------
class Yummy(db.Model):	
	user = db.ReferenceProperty(User, required=True)
	post = db.ReferenceProperty(Post, required=True)

# ----------------- FUNCTIONS YUMMY -----------------
def doYummy(user_id, post_id):
	user_yummy = User.get_by_id(user_id)
	post_yummy = Post.get_by_id(post_id)
	yummy = Yummy(user=user_yummy, post=post_yummy)
	yummy.put()
	return True

def undoYummy(user_id, post_id):
	user_delete_yummy = User.get_by_id(user_id)
	post_delete_yummy = Post.get_by_id(post_id)
	yummy_delete = db.GqlQuery("SELECT * FROM Yummy WHERE user = :1 AND post = :2", user_delete_yummy, post_delete_yummy)
	db.delete(yummy_delete.get())
	return True

def getPostYummys(post_id):
	post_yummy = Post.get_by_id(post_id)
	all_yummy = db.GqlQuery("SELECT * FROM Yummy WHERE post = :1", post_yummy)
	return all_yummy.fetch(1000)