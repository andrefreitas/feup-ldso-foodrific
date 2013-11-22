import webapp2
from datastore.user import *
from datastore.comment import *
from datastore.yummy import *
from datastore.post import *
import json
from datastore.post import getPostByID

class DeletePost(webapp2.RequestHandler):

	def get(self):
		output = {}
		try:
			id_post_str = self.request.get("postId")
			id_post = int(id_post_str)
			self.response.headers['Content-Type'] = 'application/json'
			if (getPostByID(id_post)):
				deleteCommentsForPost(id_post)
				deletePostYummys(id_post)
				if(deletePost(id_post)):
					output["answer"] = "valid"
				else:
					output["answer"] = "invalid"
				output["result"] = "ok"
				self.response.out.write(json.dumps(output))
		except:
			output["result"] = "error"
			self.response.out.write(json.dumps(output))