from datastore import *
from pages import BaseHandler

class PostImage(BaseHandler):

	def get(self):
		self.response.write("lol")
