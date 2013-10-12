from user import User
from google.appengine.ext import ndb

def addUser(name, email, password, gender, birthday):
	encrypted_pw = encrypt(password)
	user = User(name=name, email=email, password=encrypted_pw, gender=gender, birthday=birthday)

def isUser(email):
	user_query = ndb.GqlQuery("SELECT email FROM User " + " WHERE email = :1", email)
	"""q = db.GqlQuery("SELECT * FROM Person " +
                "WHERE last_name = :1 AND height <= :2 " +
                "ORDER BY height DESC",
                "Smith", max_height)

	users = user_query.fetch(1)"""
	users = user_query.get()
	if (users.empty()):
		return False
	else:
		return True

def addPost(user, title, photo, rating):
	post = Post(user=user, title=title, photo=photo, rating=rating)

def addYummy(user, post):
	yummy = Yummy(user=user, post=post)

# Get crypt algorithm to use
def encrypt(text):
	return text

def decrypt(text):
	return text