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

class Profile(BaseHandler):

    def get(self):
        user_id = int(self.request.get("user"))
        user = searchUserByID(user_id)

        if(user):
            posts = getPostsByUser(user_id)
            
            # Get post yummis
            def putYummys(post):
                post_user_id = post.user.key().id()
                post_id = post.key().id()
                yummys = getPostYummys(post_id)
                post.yummys = len(yummys)
                post.yummyDone = YummyDone(self.get_session_user_id(), post_id)
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

            genderDict = {"m" : "Man", "f" : "Woman"}
            profileOwner = self.get_session_user_id() == user_id
            is_admin = searchUserByID(self.get_session_user_id()).admin
            is_following = isUserFollowing(self.get_session_user_id(), user_id)
            params = {"user": user, 
                      "user_email":self.session.get("user"),
                      "profileOwner" : profileOwner,
                      "user_id" : self.get_session_user_id(),
                      "is_following" : is_following,
                      "posts" : posts,
                      "is_admin": is_admin }
            template = JINJA_ENVIRONMENT.get_template('profile.html')
            self.response.write(template.render(params))
        else:
            return self.redirect("/")