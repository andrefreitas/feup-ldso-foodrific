from google.appengine.ext import db
from user import User
from post import Post

# ----------------- CLASS COMMENT -----------------
class Comment(db.Model):
	user = db.ReferenceProperty(User)
	post = db.ReferenceProperty(Post)
	content = db.TextProperty()
	date = db.DateProperty(auto_now=True)
	

# ----------------- FUNCTIONS COMMENT -----------------
def addComment(user_id, post_id, content):
	user_comment = User.get_by_id(user_id)
	post_comment = Post.get_by_id(post_id)
	comment = Comment(user = user_comment, post = post_comment, content = content)
	comment.put()
	return True

def deleteComment(comment_id):
	comment_to_delete = Comment.get_by_id(comment_id)
	db.delete(comment_to_delete)
	return True
	