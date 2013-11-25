import webapp2
from datastore import *
import json

class SendRecover(webapp2.RequestHandler):

	def get(self):
		email = self.request.get("email")
		self.response.headers['Content-Type'] = 'application/json'
		output = {}
		try:
			if(isUser(email)):
				output["answer"] = "valid"
				generateUserRecoveryToken(email)
			else:
				output["answer"] = "invalid"
			output["result"] = "ok"
			self.response.out.write(json.dumps(output))
		except:
			output["result"] = "error"
			self.response.out.write(json.dumps(output))
		