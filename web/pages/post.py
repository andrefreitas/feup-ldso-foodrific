import jinja2
import webapp2
import cgi
import datetime
import os
import time
from base_handler import *
from datastore import *

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class PostPage(BaseHandler):
    def get(self):
        if(self.isLoggedIn()):
            post_id = int(self.request.get("id"))
            post = getPostByID(post_id)
            
            user_id = int(self.get_session_user_id())
            
            yummys = getPostYummys(post_id)
            post.yummys = len(yummys)
            post.yummyDone = YummyDone(user_id, post_id)
           
            comments = getCommentsForPost(post_id)
            post.comments = sorted(comments, key=lambda c: c.date, reverse=True)
            post.commentsNumber = len(comments)
    
            template_values = {
                "post": post,
                "user_email" : self.session.get("user")
            }
            template = JINJA_ENVIRONMENT.get_template('post.html')
            self.response.write(template.render(template_values))
        else:
            return self.redirect('/')