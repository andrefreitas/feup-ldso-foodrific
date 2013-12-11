import webapp2
from datastore.post import *
from google.appengine.ext import db
from pages import BaseHandler
import json

class Search(BaseHandler):

    def get(self):
        output = {}
        try:
            term = self.request.get("term")
            posts = searchPosts(term)
            # EM DESENVOLVIMENTO
            self.response.headers['Content-Type'] = 'application/json'
            output["answer"] = self.session
            output["result"] = "ok"
            self.response.out.write(json.dumps(output))
        except:
            output["result"] = "error"
            self.response.out.write(json.dumps(output))