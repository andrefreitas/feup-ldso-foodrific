from datastore import *
from pages import BaseHandler

class PostImage(BaseHandler):

	def get(self):
		post = getPostByID(int(self.request.get("id")))
		self.response.headers['Content-Type'] = 'image/png'
		self.response.out.write(post.photo)
