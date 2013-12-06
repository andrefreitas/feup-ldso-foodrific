import webapp2
from datastore import *
from google.appengine.ext import db
from pages import BaseHandler
import json
import urllib, hashlib
import urllib, cStringIO

class GetGravatar(BaseHandler):

	def get(self):
		output = {}
		try:
			email = self.request.get("email") if(self.request.get("email")) else self.get_session_email()
			size = int(self.request.get("size")) if(self.request.get("size")) else 40
			default = "images/default-avatar.png"
			output["result"] = "ok"
			gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
			gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
			output["url"] = gravatar_url
			self.response.out.write(json.dumps(output))
		except:
			output["result"] = "error"
			self.response.out.write(json.dumps(output))