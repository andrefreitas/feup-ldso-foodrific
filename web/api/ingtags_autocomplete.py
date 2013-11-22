import webapp2
from datastore import *
import json

class ingTagsAutoComplete(webapp2.RequestHandler):
	def get(self):
		output = {}
		ing_tags = ["frango","ervilhas"]
		ingredients = getIngredients()
		for ing in ingredients:
			ing_tags.append(ing.name)
		return ing_tags
