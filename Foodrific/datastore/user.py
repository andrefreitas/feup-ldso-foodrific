from google.appengine.ext import db
import base64

# ----------------- CLASS USER -----------------
class User(db.Model):
    name = db.StringProperty(required=True)
    email = db.EmailProperty(required=True)
    password = db.StringProperty(indexed=False, required=True)
    birthday = db.DateProperty(required=True)
    gender = db.StringProperty(indexed=False, required=True, choices=set(["m", "f"]))
    photo = db.BlobProperty()

# ----------------- FUNCTIONS USER -----------------
def addUser(name, email, password, gender, birthday):
    encrypted_pw = encrypt(password)
    user = User(name=name, email=email, password=encrypted_pw, gender=gender, birthday=birthday)
    user.put()

def isUser(email):
    user_query = db.GqlQuery("SELECT * FROM User WHERE email = :1", email)
    user = user_query.get()
    if (user is not None):
        return True
    else:
        return False

def addPhotoToUser(user_id, photo):
    user = searchUserByID(user_id)
    user.photo = photo
    user.put()
    return True

def getPhotoByUser(user_id):
    user = searchUserByID(user_id)
    if (user != None):
        return user.photo
    else: return False

def searchUserByID(user_id):
    user = User.get_by_id(user_id)
    return user

def searchUserByName(name):
    # TO IMPROVE QUERY
    user_query = db.GqlQuery("SELECT * FROM User WHERE name = :1", name) 
    return user_query.fetch(1000)

def searchUserByEmail(email):
    # TO IMPROVE QUERY
    user_query = db.GqlQuery("SELECT * FROM User WHERE email = :1", email)
    return user_query.fetch(1000)

# ----------------- ADDITIONAL FUNCTIONS -----------------
# Needing salt element
def encrypt(text):
    encoded_string = base64.b64encode(text)
    return encoded_string

def decrypt(text):
    decoded_string = base64.b64decode(text)
    return decoded_string