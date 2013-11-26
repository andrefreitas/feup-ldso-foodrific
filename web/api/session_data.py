import webapp2
from datastore import *
from google.appengine.ext import db
from pages import BaseHandler
import json

class SessionData(BaseHandler):

	def get(self):
		output = {}
		try:
			self.response.headers['Content-Type'] = 'application/json'
			output["answer"] = self.session
			output["result"] = "ok"
			self.response.out.write(json.dumps(output))
		except:
			output["result"] = "error"
			self.response.out.write(json.dumps(output))