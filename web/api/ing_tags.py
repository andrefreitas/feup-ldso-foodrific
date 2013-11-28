import webapp2
from datastore import *
import json

class IngTags(webapp2.RequestHandler):
	def get(self):
		output = {}
		term = self.request.get("term")
		ing_tags = [] #demo tags
		results = searchIngredients(term)
		if results is not None:
			ing_tags = results
		self.response.headers['Content-Type'] = 'application/json'
		self.response.out.write(json.dumps(ing_tags))
