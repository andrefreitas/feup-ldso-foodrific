import webapp2
from datastore import *
from google.appengine.ext import db
from pages import BaseHandler
import json

class NewComment(BaseHandler):

	def get(self):
		output = {}
		try:
			post_id = int(self.request.get("postId"))
			comment = self.request.get("comment")
			user_id = int(self.get_session_user_id())
			self.response.headers['Content-Type'] = 'application/json'
			if(len(comment) > 0):
				comment_id = addComment(user_id, post_id, comment)
				output["comment_id"] = comment_id
				output["answer"] = "done"
				output["result"] = "ok"
			else:
				output["result"] = "error"
			self.response.out.write(json.dumps(output))
		except:
			output["result"] = "error"
			self.response.out.write(json.dumps(output))