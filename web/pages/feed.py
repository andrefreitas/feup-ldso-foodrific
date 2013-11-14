import jinja2
import webapp2
import cgi
import datetime
import os
from base_handler import *
from datastore import *

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Feed(BaseHandler):

    def get(self):
        if(self.isLoggedIn()):
            posts = getPosts()
            user_id = int(self.get_session_user_id())
            
            def putYummys(post):
                post_user_id = post.user.key().id()
                post_id = post.key().id()
                yummys = getPostYummys(post_id)
                post.yummys = len(yummys)
                post.yummyDone = False
                return post

            posts = map(putYummys, posts)

            template_values = {
                "posts" : posts,
                "user_email" : self.session.get("user")
            }
            template = JINJA_ENVIRONMENT.get_template('feed.html')
            self.response.write(template.render(template_values))
        else:
            return self.redirect('/')