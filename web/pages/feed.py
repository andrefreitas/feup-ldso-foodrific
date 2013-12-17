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
            user_id = int(self.get_session_user_id())
            posts = getPostsByUserFollowing(user_id)
            posts = posts + getPostsByUser(user_id)
            posts = sorted(posts, key = lambda post: post.original_date, reverse=True)
            is_admin = searchUserByID(user_id).admin
            
            # Get post yummis
            def putYummys(post):
                post_user_id = post.user.key().id()
                post_id = post.key().id()
                yummys = getPostYummys(post_id)
                post.yummys = len(yummys)
                post.yummyDone = YummyDone(user_id, post_id)
                return post

            # Get post comments
            def putComments(post):
                post_id = post.key().id()
                comments = getCommentsForPost(post_id)
                post.comments = sorted(comments, key=lambda c: c.date, reverse=True)
                post.commentsNumber = len(comments)
                return post

            

            posts = map(putYummys, posts)
            posts = map(putComments, posts)

            template_values = {
                "posts" : posts,
                "user_email" : self.session.get("user"),
                "is_admin" : is_admin,
                "user_id" : self.get_session_user_id()
            }
            template = JINJA_ENVIRONMENT.get_template('feed.html')
            self.response.write(template.render(template_values))
        else:
            return self.redirect('/')