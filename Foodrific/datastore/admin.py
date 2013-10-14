from google.appengine.ext import db
import base64

# ----------------- CLASS ADMIN -----------------
class Admin(db.Model):
    name = db.StringProperty(required=True)
    email = db.StringProperty(required=True)
    password = db.StringProperty(indexed=False, required=True)
    
    
# ----------------- FUNCTIONS ADMIN -----------------
def addAdmin(name, email, password):
    encrypted_pw = encrypt(password)
    admin = Admin(name=name, email=email, password=encrypted_pw)
    admin.put()
    return True

def isAdmin(email, password):
    admin_query = db.GqlQuery("SELECT * FROM Admin WHERE email = :1 AND password = :2", email, encrypt(password))
    admin = admin_query.get()
    if (admin is not None):
        return True
    else:
        return False
    
def editAdmin(name, email, password):
    encrypted_pw = encrypt(password)
    admin_query = db.GqlQuery("SELECT * FROM Admin WHERE email = :1", email)
    admin_verify = admin_query.get()
    if (admin_verify is not None):
        admin_verify.name = name
        admin_verify.email = email
        admin_verify.password = encrypted_pw
        db.put(admin_verify)
        return True
    else:
        return False

def deleteAdmin(admin_id):
    admin_delete = Admin.get_by_id(admin_id)
    db.delete(admin_delete)
    return True
    
def searchAdminByName(name):
    # TO IMPROVE QUERY
    admin_query = db.GqlQuery("SELECT * FROM Admin WHERE name = :1", name) 
    return admin_query.fetch(1000)

def searchAdminByEmail(email):
    # TO IMPROVE QUERY
    admin_query = db.GqlQuery("SELECT * FROM Admin WHERE email = :1", email)
    return admin_query.fetch(1000)
    
# ----------------- ADDITIONAL FUNCTIONS -----------------
# Needing salt element
def encrypt(text):
    encoded_string = base64.b64encode(text)
    return encoded_string

def decrypt(text):
    decoded_string = base64.b64decode(text)
    return decoded_string