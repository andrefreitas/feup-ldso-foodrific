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

class SearchResults(BaseHandler):

    def get(self):
        term = self.request.get("term")
        output = {}
        posts = searchPosts(term)
        user_id = int(self.get_session_user_id())
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
            "term" : term,
            "posts": posts
        }
        template = JINJA_ENVIRONMENT.get_template('search.html')
        self.response.write(template.render(template_values))