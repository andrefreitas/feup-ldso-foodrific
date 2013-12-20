from google.appengine.ext import db
from user import User
from post import Post

# ----------------- CLASS YUMMY -----------------
class Yummy(db.Model):	
	user = db.ReferenceProperty(User, required=True)
	post = db.ReferenceProperty(Post, required=True)

# ----------------- FUNCTIONS YUMMY -----------------
def toogleYummy(user_id, post_id):
	user_yummy = User.get_by_id(user_id)
	post_yummy = Post.get_by_id(post_id)
	if (not YummyDone(user_id, post_id)):
		yummy = Yummy(user=user_yummy, post=post_yummy)
		yummy.put()
		return True
	else:
		yummy_delete = Yummy.all()
		yummy_delete.filter("user =", user_yummy)
		yummy_delete.filter("post =", post_yummy)
		db.delete(yummy_delete.get())
		return False

def getPostYummys(post_id):
	post_yummy = Post.get_by_id(post_id)
	all_yummy = Yummy.all()
	all_yummy.filter("post =", post_yummy)
	return all_yummy.fetch(1000)

def deletePostYummys(post_id):
	yummy_posts = getPostYummys(post_id)
	if(yummy_posts is None):
		return True
	else:
		db.delete(yummy_posts)
		return True
	
def deleteYummysUser(user_id): 
	yummys = Yummy.all().filter("user =", User.get_by_id(user_id))
	db.delete(yummys)

def YummyDone(user_id, post_id):
	user_delete_yummy = User.get_by_id(user_id)
	post_delete_yummy = Post.get_by_id(post_id)
	yummy = Yummy.all()
	yummy.filter("user =", user_delete_yummy)
	yummy.filter("post =", post_delete_yummy)
	if (len(yummy.fetch(1000)) > 0):
		return True
	else:
		return False