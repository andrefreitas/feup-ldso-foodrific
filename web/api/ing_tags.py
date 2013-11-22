import webapp2
from datastore import *
import json

class IngTags(webapp2.RequestHandler):
	def get(self):
		output = {}
		term = self.request.get("term")
		ing_tags = ["frango","ervilhas"]
		self.response.headers['Content-Type'] = 'application/json'
		'''ingredients = getIngredients()
		for ing in ingredients:
			ing_tags.append(ing.name)
		return ing_tags '''
		self.response.out.write(json.dumps(ing_tags))
