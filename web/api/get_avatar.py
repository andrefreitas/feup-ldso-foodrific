from datastore import *
from pages import BaseHandler
from google.appengine.api import images
import urllib, hashlib
import json

class GetAvatar(BaseHandler):

	def get(self):
		
		#default = "http://" + self.request.host_url + "/images/default-avatar.png"
		email = self.request.get("email") if self.request.get("email") else self.get_session_email()
		size = self.request.get("size") if self.request.get("size") else 100
		# construct the url
		gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
		gravatar_url += urllib.urlencode({'d':"mm", 's':str(size)})
		
		imgData = urllib.urlopen(gravatar_url).read()
		self.response.headers['Content-Type'] = 'image/png'
		self.response.out.write(imgData)
		"""
		output = {}
		self.response.headers['Content-Type'] = 'application/json'
		output["url"] = gravatar_url
		self.response.out.write(json.dumps(output))
		"""
		