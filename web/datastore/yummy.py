from google.appengine.ext import db
from user import User
from post import Post

# ----------------- CLASS YUMMY -----------------
class Yummy(db.Model):	
	user = db.ReferenceProperty(User, required=True)
	post = db.ReferenceProperty(Post, required=True)

# ----------------- FUNCTIONS YUMMY -----------------
def doYummy(user_id, post_id):
	if (not YummyDone(user_id, post_id)):
		user_yummy = User.get_by_id(user_id)
		post_yummy = Post.get_by_id(post_id)
		yummy = Yummy(user=user_yummy, post=post_yummy)
		yummy.put()
		return True
	else:
		return False

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

def deletePostYummys(post_id):
	yummy_posts = getPostYummys(post_id)
	if(yummy_posts is None):
		return True
	else:
		db.delete(yummy_posts)
		return True

def YummyDone(user_id, post_id):
	user_delete_yummy = User.get_by_id(user_id)
	post_delete_yummy = Post.get_by_id(post_id)
	yummy = db.GqlQuery("SELECT * FROM Yummy WHERE user = :1 AND post = :2", user_delete_yummy, post_delete_yummy)
	if (len(yummy.fetch(1000)) > 0):
		return True
	else:
		return False