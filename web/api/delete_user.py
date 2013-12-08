import webapp2
from datastore.user import *
from datastore.comment import *
from datastore.yummy import *
from datastore.post import *
import json
from datastore.post import getPostByID
from pages import BaseHandler
import cgi

class DeleteUser(BaseHandler):
	def post(self):
		id_user = self.session.get("user_id")
		posts = getPostsByUser(id_user)
		for post in posts:
			id_post = post.key().id()
			if(getPostByID(id_post)):
				deleteCommentsForPost(id_post)
				deletePostYummys(id_post)
				deletePost(id_post)
		deleteUser(id_user)
		self.redirect('/logout')