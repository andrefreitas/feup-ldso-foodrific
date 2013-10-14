from user import User
from post import Post
from yummy import Yummy
from google.appengine.ext import db
import base64

# ----------------- USER -----------------
def addUser(name, email, password, gender, birthday):
	encrypted_pw = encrypt(password)
	user = User(name=name, email=email, password=encrypted_pw, gender=gender, birthday=birthday)
	user.put()

def isUser(email):
	user_query = db.GqlQuery("SELECT * FROM User WHERE email = :1", email)
	user = user_query.get()
	#print user.key().id()
	if (user is not None):
		return True
	else:
		return False

def addPhotoToUser(id_user, photo):
	return
	# TODO

def getPhotoByUser(id_user):
	# MUST BE TESTED
	user = User.get_by_id(id_user)
	return user.photo

def searchUserByName(name):
	# TO IMPROVE QUERY
	# FETCH MUST BE TESTED
	user_query = db.GqlQuery("SELECT * FROM User WHERE name = :1", name) 
	return user_query.fetch()

def searchUserByEmail(email):
	# FETCH MUST BE TESTED
	user_query = db.GqlQuery("SELECT * FROM User WHERE email = :1", email)
	return user_query.fetch()
	
# ----------------- POST -----------------

def addPost(user, title, photo, rating):
	post = Post(user=user, title=title, photo=photo, rating=rating)
	post.put()

def getPostsByUser(id_user):
	return
	#TODO

# ----------------- YUMMY -----------------
def doYummy(user, post):
	yummy = Yummy(user=user, post=post)
	yummy.put()

def undoYummy(user, post):
	return
	#TODO

def getPostYummys(post):
	return
	#TODO

# ----------------- ADDITIONAL FUNCTIONS -----------------
# Needing salt element
def encrypt(text):
	encoded_string = base64.b64encode(text)
	return encoded_string

def decrypt(text):
	decoded_string = base64.b64decode(text)
	return decoded_string