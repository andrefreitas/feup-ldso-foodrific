from google.appengine.ext import db
import hashlib
from random import randint
from google.appengine.api import mail
import re

maxLimit = 999999999

# ----------------- CLASS USER -----------------
class User(db.Model):
    name = db.StringProperty(required=True)
    email = db.EmailProperty(required=True)
    password = db.StringProperty(required=True)
    birthday = db.DateProperty(required=True)
    gender = db.StringProperty(indexed=False, required=True, choices=set(["m", "f"]))
    photo = db.BlobProperty()
    token = db.StringProperty(required=False)
    admin = db.BooleanProperty()


# ----------------- FUNCTIONS USER -----------------
def addUser(name, email, password, gender, birthday):
    if (searchUserByEmail(email) == None):
        encrypted_pw = encrypt(password)
        user = User(name=name, email=email, password=encrypted_pw, gender=gender, birthday=birthday, admin=False)
        user.put()
        sender_address = "foodrific.service@gmail.com"
        subject = "Bem-vindo ao Foodrific!"
        body = "Ola.\n\nBem-vindo ao Foodrific! Aqui poderas partilhar e encontrar novas receitas e experiencias.\nAcede ja a http://foodrific.appspot.com .\n\nA equipa Foodrific."
        mail.send_mail(sender_address, email, subject, body)
        return user.key().id()
    else:
        return False
    
def editUser(name, old_email, new_email,  password, gender, birthday):
    encrypted_pw = encrypt(password)
    user_query = User.all()
    user_query.filter("email =", old_email)
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

def editUserName(email, newName):
    user_query = User.all()
    user_query.filter("email =", email)
    user_verify = user_query.get()
    if (user_verify is not None):
        user_verify.name = newName
        user_verify.put()
        return True
    else:
        return False

def editUserEmail(old_email, new_email):
    user_query = User.all()
    user_query.filter("email =", old_email)
    user_verify = user_query.get()
    if (user_verify is not None):
        user_verify.email = new_email
        user_verify.put()
        return True
    else:
        return False

def editUserBirthday(email, birthday):
    user_query = User.all()
    user_query.filter("email =", email)
    user_verify = user_query.get()
    if (user_verify is not None):
        user_verify.birthday = birthday
        user_verify.put()
        return True
    else:
        return False

def editUserGender(email, gender):
    user_query = User.all()
    user_query.filter("email =", email)
    user_verify = user_query.get()
    if (user_verify is not None):
        user_verify.gender = gender
        user_verify.put()
        return True
    else:
        return False

def editUserPassword(email, old_password, new_password):
    old_encrypted_pw = encrypt(old_password)
    encrypted_pw = encrypt(new_password)
    user_query = User.all()
    user_query.filter("email =", email)
    user_verify = user_query.get()
    if (user_verify is not None):
        if user_verify.password == old_encrypted_pw:
            user_verify.password = encrypted_pw
            user_verify.put()
            return True
        else:
            return False
    else:
        return False

def loginUser(email, password):
    user_query = User.all()
    user_query.filter("email =", email)
    user_query.filter("password =", encrypt(password))
    user = user_query.get()
    if (user is not None):
        return user.key().id()
    else:
        return False
    
def getUserID(email):
    user_query = User.all()
    user_query.filter("email =", email)
    return user_query.get().key().id()
    
def isUser(email):
    user_query = User.all()
    user_query.filter("email =", email)
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
    user_query = User.all()
    user_query.filter('email =', email)
    return user_query.get()

def generateUserRecoveryToken(email):
    user_query = User.all()
    user_query.filter("email =", email)
    if user_query is not None:
        user_value = user_query.get()
        user_value.token = encrypt(user_value.email + str(randint(1, maxLimit)))
        sender_address = "foodrific.service@gmail.com"
        subject = "Recuperacao de password"
        body = "Ola.\n\nEfetuaste um pedido de recuperacao de password. Para prosseguir acede a http://foodrific.appspot.com/recovery?token=" + user_value.token + " .\n\nA equipa Foodrific."
        mail.send_mail(sender_address, email, subject, body)
        db.put(user_value)
        return True
    else:
        return False
    
def changePasswordByToken(token, password):
    user_query = User.all()
    user_query.filter("token =", token)
    if user_query is not None:
        user_value = user_query.get()
        user_value.token = ""
        user_value.password = encrypt(password)
        db.put(user_value)
        return True
    else:
        return False
    
def getUserToken(email):
    user_query = User.all()
    user_query.filter("email =", email)
    if user_query is not None:
        user_value = user_query.get()
        return user_value.token
    else:
        return

def getUsers():
    users_query = User.all()
    return users_query.fetch(1000)

def searchUsers(searchword):
    users_query = getUsers()
    match_Users = []
    if users_query:
        searchword = searchword.encode('utf-8').lower().strip()
        for user in users_query:
            if re.search(searchword, user.name.encode('utf-8').lower().strip()):
                match_Users.append(user)
    return match_Users

# ----------------- ADDITIONAL FUNCTIONS -----------------
# Needing salt element
def encrypt(text):
    encoded_string = hashlib.sha256(text).hexdigest()
    return encoded_string