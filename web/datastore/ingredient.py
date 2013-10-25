from google.appengine.ext import db

class Ingredient(db.Model):
    name = db.StringProperty(required=True);
    photo = db.BlobProperty()

def addIngredient(name, photo):
    if(existIngredient(name)):
        return False
    else:
        ingredient = Ingredient(name = name, photo = photo)
        ingredient.put()
        return True

def existIngredient(name):
    ingredient_query = db.GqlQuery("SELECT * FROM Ingredient WHERE name = :1", name)
    ingredient = ingredient_query.get()
    if (ingredient is None):
        return False
    else:
        return True