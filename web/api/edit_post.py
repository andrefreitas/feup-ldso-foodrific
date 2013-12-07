import webapp2
from datastore.user import *
from datastore.comment import *
from datastore.yummy import *
from datastore.post import *
import json
from datastore.post import getPostByID

class EditPost(webapp2.RequestHandler):

	def get(self):
		output = {}
		try:
			id_post_str = self.request.get("postId")
			id_post = int(id_post_str)
			self.response.headers['Content-Type'] = 'application/json'
			if(getPostByID(id_post)):
				output["answer"] = "find"
				output["title"] = getPostByID(id_post).title
				output["user"] = getPostByID(id_post).user.name
				output["recipe"] = getPostByID(id_post).recipe
				output["ingredients"] = getPostByID(id_post).ingredients
			else:
				output["answer"] = "not find"
			output["result"] = "ok"
			self.response.out.write(json.dumps(output))
		except:
			output["result"] = "error"
			self.response.out.write(json.dumps(output))