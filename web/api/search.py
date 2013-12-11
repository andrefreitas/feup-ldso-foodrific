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
            self.response.headers['Content-Type'] = 'application/json'
            output["answer"] = self.session
            i=0
            post_output = {}
            for post in posts:
                post_output["id"+str(i+1)] = post
                i +=1
            output["posts"] = post_output
            self.response.out.write(json.dumps(output))
        except:
            output["result"] = "error"
            self.response.out.write(json.dumps(output))