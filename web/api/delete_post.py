import webapp2
from datastore import *
import json

class DeletePost(webapp2.RequestHandler):

	def get(self):
		id_post_str = self.request.get("id_post_to_delete")
		id_post = int(id_post_str)
		self.response.headers['Content-Type'] = 'application/json'
		output = {}
		try:
			if(deletePost(id_post)):
				output["answer"] = "valid"
				deleteCommentsForPost(id_post)
				deletePostYummys(id_post)
			else:
				output["answer"] = "invalid"
			output["result"] = "ok"
			self.response.out.write(json.dumps(output))
		except:
			output["result"] = "error"
			self.response.out.write(json.dumps(output))