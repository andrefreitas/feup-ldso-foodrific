import webapp2
from datastore import *
import json

class NewPost(webapp2.RequestHandler):

	def post(self):
		title = self.request.get("title")
		photo = self.request.get("photo")
		ingredients = self.request.get("ingredients")



