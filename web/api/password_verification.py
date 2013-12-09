import webapp2
from datastore import *
import json
from pages import BaseHandler

class PasswordVerification(BaseHandler):

	def get(self):
		email = self.get_session_email()
		password = self.request.get("password")
		self.response.headers['Content-Type'] = 'application/json'
		output = {}
		try:
			if(loginUser(email, password)):
				output["answer"] = "valid"
			else:
				output["answer"] = "invalid"
			output["result"] = "ok"
			self.response.out.write(json.dumps(output))
		except:
			output["result"] = "error"
			self.response.out.write(json.dumps(output))
		
