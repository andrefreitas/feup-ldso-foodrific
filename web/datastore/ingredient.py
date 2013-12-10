from google.appengine.ext import db
import re

class Ingredient(db.Model):
    name = db.StringProperty(required=True);
    photo = db.BlobProperty()

def addIngredient(name, photo):
    name = name.lower()
    name = name.strip()
    if(existIngredient(name) or len(name) == 0 or name is None):
        return False
    else:
        ingredient = Ingredient(name = name, photo = photo)
        ingredient.put()
        return True

def existIngredient(name):
    ingredient_query = Ingredient.all()
    ingredient_query.filter("name =", name)
    ingredient = ingredient_query.get()
    if (ingredient is None):
        return False
    else:
        return True

def getIngredients():
    ingredient_query = Ingredient.all()
    return ingredient_query.fetch(1000)

def searchIngredients(term):
    ingredients_query = getIngredients()
    match_ingredients = []
    if ingredients_query:
        term = term.lower().strip()
        for ing in ingredients_query:
            if re.search(term, ing.name) is not None:
                match_ingredients.append(ing.name)
        return match_ingredients