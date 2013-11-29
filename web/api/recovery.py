import webapp2
from datastore import *
import json
import cgi


class Recovery(webapp2.RequestHandler):

	def post(self):
		
		token = cgi.escape(self.request.get('token'))
		password = cgi.escape(self.request.get('password'))
		changePasswordByToken(token, password)
		return self.redirect('/?message=Password alterada com sucesso!')
		
