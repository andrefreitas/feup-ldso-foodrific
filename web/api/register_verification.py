import webapp2
from datastore import *
import json

# api/register_verification?email=peter@gmail.com

class RegisterVerification(webapp2.RequestHandler):

	def get(self):
		email = self.request.get("email")
		self.response.headers['Content-Type'] = 'application/json'
		output = {}
		try:
			if(searchUserByEmail(email) is None):
				output["answer"] = "valid"
			else:
				output["answer"] = "invalid"
			output["result"] = "ok"
			self.response.out.write(json.dumps(output))
		except:
			output["result"] = "error"
			self.response.out.write(json.dumps(output))
		
