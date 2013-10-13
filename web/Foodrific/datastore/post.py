from google.appengine.ext import db
from user import User

#Class post
class Post(db.Model):
	user = db.ReferenceProperty(User, required=True)
	title = db.StringProperty(required=True)
	photo = db.BlobProperty(required=True)
	rating = db.RatingProperty()
	original_date = db.DateProperty(auto_now_add=True)
	last_update_date = db.DateProperty(auto_now=True)
