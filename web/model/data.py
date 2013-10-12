from user import User

def addUser(name, email, password, gender, birthday):
	encrypted_pw = encrypt(password)
	user = User(name=name, email=email, password=encrypted_pw, gender=gender, birthday=birthday)


def addPost(user, title, photo, rating):
	post = Post(user=user, title=title, photo=photo, rating=rating)

def addYummy(user, post):
	yummy = Yummy(user=user, post=post)

# Get crypt algorithm to use
def encrypt(text):
	return text

def decrypt(text):
	return text