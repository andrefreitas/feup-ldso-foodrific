from google.appengine.ext import db
from user import *
from datastore.user import getUserID

# ----------------- CLASS POST -----------------
class Post(db.Model):
	user = db.ReferenceProperty(User, required=True)
	title = db.StringProperty(required=True)
	photo = db.BlobProperty(required=True)
	rating = db.RatingProperty()
	receipt = db.TextProperty()
	ingredients = db.ListProperty(str)
	original_date = db.DateProperty(auto_now_add=True)
	last_update_date = db.DateProperty(auto_now=True)


# ----------------- FUNCTIONS POST -----------------
def addPost(user, title, photo):
	post = Post(user=user, title=title, photo=photo)
	post.put()
	return post.key().id()

def getPostsByUser(user_id):
	user = User.get_by_id(user_id)
	post_query = db.GqlQuery('SELECT * FROM Post WHERE user = :1', user)
	return post_query.fetch(1000)
	
def getPostsByUserFollowing(user_follower_id):
	user = User.get_by_id(user_follower_id)
	user_following_query = db.GqlQuery("SELECT user_following FROM Follow WHERE user_follower = :1", user)
	follow_list = user_following_query.fetch(1000)
	posts_list = []
	for follow in follow_list:
		u = searchUserByEmail(follow.user_following.email)
		user_following_posts = db.GqlQuery("SELECT * FROM Post WHERE user = :1", u)
		posts_list.extend(user_following_posts.fetch(1000))
	return posts_list
	
def deletePost(post_id):
	post_to_delete = Post.get_by_id(post_id)
	db.delete(post_to_delete)
	return True
	
