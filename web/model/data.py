from user import User
from google.appengine.ext import ndb

# ----------------- USER -----------------
def addUser(name, email, password, gender, birthday):
	encrypted_pw = encrypt(password)
	user = User(name=name, email=email, password=encrypted_pw, gender=gender, birthday=birthday)
	user.put()

def isUser(email):
	user = User.query(User.email = email).get()
	if (user is not None):
		return True
	else:
		return False

def addPhotoToUser(id_user, photo):
	# TODO

def getPhotoByUser(id_user):
	# TODO

def searchUserByName(name):
	user = User.query(User.name = name)
	return user.fetch()
	#TODO

def searchUserByEmail(email):
	user = User.query(User.name = name)
	return user.fetch()
	#TODO

# ----------------- POST -----------------

def addPost(user, title, photo, rating):
	post = Post(user=user, title=title, photo=photo, rating=rating)
	post.put()

def getPostsByUser(id_user):
	#TODO

# ----------------- YUMMY -----------------
def doYummy(user, post):
	yummy = Yummy(user=user, post=post)
	yummy.put()

def undoYummy(user, post):
	#TODO

def getPostYummys(post):
	#TODO

# ----------------- ADDITIONAL FUNCTIONS -----------------
# Get crypt algorithm to use
def encrypt(text):
	return text

def decrypt(text):
	return text