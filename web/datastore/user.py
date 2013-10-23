from google.appengine.ext import db
import base64

# ----------------- CLASS USER -----------------
class User(db.Model):
    name = db.StringProperty(required=True)
    email = db.EmailProperty(required=True)
    password = db.StringProperty(required=True)
    birthday = db.DateProperty(required=True)
    gender = db.StringProperty(indexed=False, required=True, choices=set(["m", "f"]))
    photo = db.BlobProperty()


# ----------------- FUNCTIONS USER -----------------
def addUser(name, email, password, gender, birthday):
    if (searchUserByEmail(email) == None):
        encrypted_pw = encrypt(password)
        user = User(name=name, email=email, password=encrypted_pw, gender=gender, birthday=birthday)
        user.put()
        return user.key().id()
    else:
        return False
    
def editUser(name, old_email, new_email,  password, gender, birthday):
    encrypted_pw = encrypt(password)
    user_query = db.GqlQuery("SELECT * FROM User WHERE email = :1", old_email)
    user_verify = user_query.get()
    if (user_verify is not None):
        user_verify.name = name
        user_verify.email = new_email
        user_verify.password = encrypted_pw
        user_verify.gender = gender
        user_verify.birthday = birthday
        db.put(user_verify)
        return True
    else:
        return False

def loginUser(email, password):
    user_query = db.GqlQuery("SELECT * FROM User WHERE email = :1 AND password = :2", email, encrypt(password))
    user = user_query.get()
    if (user is not None):
        return user.key().id()
    else:
        return False
    
def isUser(email):
    user_query = db.GqlQuery("SELECT * FROM User WHERE email = :1", email)
    user = user_query.get()
    if (user is not None):
        return True
    else: 
        return False
    
def deleteUser(user_id):
    user_delete = User.get_by_id(user_id)
    db.delete(user_delete)
    return True

def addPhotoToUser(user_id, photo):
    user = searchUserByID(user_id)
    user.photo = photo
    user.put()
    return True

def editPhotoUser(user_id, photo):
    user = searchUserByID(user_id)
    user.photo = photo
    db.put(user)
    return True

def getPhotoByUser(user_id):
    user = searchUserByID(user_id)
    if (user != None):
        return user.photo
    else: 
        return False

def searchUserByID(user_id):
    user = User.get_by_id(user_id)
    return user

def searchUserByName(name):
    # TO IMPROVE QUERY !!!
    user_query = db.GqlQuery("SELECT * FROM User WHERE name >= :1 AND name < :2", name, name + "\uFFFD")
    
    return user_query.fetch(1000)

def searchUserByEmail(email):
    user_query = db.GqlQuery("SELECT * FROM User WHERE email = :1", email)
    return user_query.get()

# ----------------- ADDITIONAL FUNCTIONS -----------------
# Needing salt element
def encrypt(text):
    encoded_string = base64.b64encode(text)
    return encoded_string

def decrypt(text):
    decoded_string = base64.b64decode(text)
    return decoded_string