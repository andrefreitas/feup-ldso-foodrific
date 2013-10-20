from google.appengine.ext import db
from user import User

# ----------------- CLASS POST -----------------
class Post(db.Model):
	user = db.ReferenceProperty(User, required=True)
	title = db.StringProperty(required=True)
	photo = db.BlobProperty(required=True)
	rating = db.RatingProperty()
	original_date = db.DateProperty(auto_now_add=True)
	last_update_date = db.DateProperty(auto_now=True)


# ----------------- FUNCTIONS POST -----------------
def addPost(user, title, photo, rating):
	post = Post(user=user, title=title, photo=photo, rating=rating)
	post.put()
	return post.key().id()

def getPostsByUser(user_id):
	user = User.get_by_id(user_id)
	post_query = db.GqlQuery('SELECT * FROM Post WHERE user = :1', user)
	return post_query.fetch(1000)
	#TODO
	
def getPostsByUserFollwing(user_id):
	user = User.get_by_id(user_id)
	user_following_query = db.GqlQuery("SELECT user_following FROM Follow WHERE user_follower = :1", user)
	user_following_posts = db.GqlQuery("SELECT * FROM Post WHERE user IN :1", user_following_query.fetch(1000))
	return user_following_posts
	
def deletePost(post_id):
	post_to_delete = Post.get_by_id(post_id)
	db.delete(post_to_delete)
	return True
	
