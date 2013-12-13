import webapp2
from datastore import *
from google.appengine.ext import db
from pages import BaseHandler
import time

class EditPost(BaseHandler):

	def post(self):
		postId = self.request.get("postId")
		id_post = int(postId)
		title = self.request.get("title")
		photo = self.request.get("photo")
		ingString = self.request.get("ingredients")
		ingredients = []
		if len(ingString) > 0:
			ingredients = ingString.split(",")
		recipe = self.request.get("recipe")
		editPost(id_post, title, photo, recipe, ingredients)
		for ing in ingredients:
			addIngredient(ing,None)
		time.sleep(1)
		return self.redirect('/')