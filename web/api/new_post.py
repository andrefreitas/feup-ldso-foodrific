import webapp2
from datastore import *
from google.appengine.ext import db
from pages import BaseHandler

class NewPost(BaseHandler):

	def post(self):
		title = self.request.get("title")
		photo = self.request.get("photo")
		ingString = self.request.get("ingredients")
		ingredients = []
		if len(ingString) > 0:
			ingredients = ingString.split(",")
		recipe = self.request.get("recipe")
		email = self.session.get("user")
		user = searchUserByEmail(email)
		postId = addPost(user, title, photo)
		if postId is not None:
			addIngredients(postId, ingredients)
			for ing in ingredients:
				addIngredient(ing,None)
			if len(recipe) > 0:
				addRecipe(postId,recipe)
		return self.redirect('/')