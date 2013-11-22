import webapp2
from datastore import *
from google.appengine.ext import db
from pages import BaseHandler

class NewPost(BaseHandler):

	def post(self):
		title = self.request.get("title")
		photo = db.Blob(self.request.get("photo"))
		ingredients = self.request.get("ingredients").split(",")
		email = self.session.get("user")
		user = searchUserByEmail(email)
		postId = addPost(user, title, photo)
		addIngredients(postId, ingredients)
		for ing in ingredients:
			Ingredient.addIngredient(ing,None)
		return self.redirect('/')