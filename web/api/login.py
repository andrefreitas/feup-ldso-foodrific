import webapp2
from datastore import *
import json

# api/login?email=peter@gmail.com&password=123456

class Login(webapp2.RequestHandler):

	def get(self):
		email = self.request.get("email")
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
		
