from google.appengine.ext import db

class Ingredient(db.Model):
    name = db.StringProperty(required=True);
    photo = db.BlobProperty()