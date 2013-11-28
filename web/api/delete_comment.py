import webapp2
from datastore import *
from google.appengine.ext import db
from pages import BaseHandler
import json

class DeleteComment(BaseHandler):

	def get(self):
		output = {}
		try:
			# todo check, if comment is owned by the requester
			comment_id = int(self.request.get("comment_id"))
			deleteComment(comment_id)
			output["answer"] = "done"
			output["result"] = "ok"
			self.response.out.write(json.dumps(output))
		except:
			output["result"] = "error"
			self.response.out.write(json.dumps(output))