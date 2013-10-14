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

def getPostsByUser(user_id):
	user = User.get_by_id(user_id)
	post_query = db.GqlQuery('SELECT * FROM Post WHERE user = :1', user)
	return post_query.fetch(1000)
	#TODO
