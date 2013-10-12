from user import User
from google.appengine.ext import ndb

def addUser(name, email, password, gender, birthday):
	encrypted_pw = encrypt(password)
	user = User(name=name, email=email, password=encrypted_pw, gender=gender, birthday=birthday)
	user.put()

def isUser(email):
	user_query = ndb.GqlQuery("SELECT email FROM User " + " WHERE email = :1", email)
	users = user_query.get()
	if (users.empty()):
		return False
	else:
		return True

def addPost(user, title, photo, rating):
	post = Post(user=user, title=title, photo=photo, rating=rating)
	post.put()

def addYummy(user, post):
	yummy = Yummy(user=user, post=post)
	yummy.put()

# Get crypt algorithm to use
def encrypt(text):
	return text

def decrypt(text):
	return text