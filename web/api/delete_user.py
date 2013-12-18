import webapp2
from datastore.user import *
from datastore.comment import *
from datastore.yummy import *
from datastore.post import *
from datastore.follow import *
import json
from datastore.post import getPostByID
from pages import BaseHandler
import cgi

class DeleteUser(BaseHandler):
	def post(self):
		id_user = self.session.get("user_id")
		user = searchUserByID(id_user)

		if (user.admin is False):
			posts = getPostsByUser(id_user)
			for post in posts:
				id_post = post.key().id()
				if(getPostByID(id_post)):
					deleteCommentsForPost(id_post)
					deletePostYummys(id_post)
					deletePost(id_post)
			deleteUser(id_user)
			self.redirect('/logout')
		else:
			id_user_str = self.request.get("profile_id_user")
			id_user = int(id_user_str)
			if(isUserFollowing(self.session.get("user_id"), id_user)):
				removeUserFollowing(self.session.get("user_id"), id_user)
			posts = getPostsByUser(id_user)
			for post in posts:
				id_post = post.key().id()
				if(getPostByID(id_post)):
					deleteCommentsForPost(id_post)
					deletePostYummys(id_post)
					deletePost(id_post)
			deleteUser(id_user)
			self.redirect('/feed')