import webapp2
from google.appengine.ext import db
from datastore import *
from pages import BaseHandler
import json

class Follow(BaseHandler):

    def get(self):
        output = {}
        try:
            user_id = int(self.request.get("user"))
            follower_id = int(self.get_session_user_id())
            is_following = isUserFollowing(follower_id, user_id)
            success = True
            follow_type = "follow"
            if(is_following):
                follow_type = "unfollow"
                removeUserFollowing(follower_id, user_id)
            else:
                addUserToFollow(follower_id, user_id)
            self.response.headers['Content-Type'] = 'application/json'
            if(success):
                output["action"] = follow_type
                output["answer"] = "done"
                output["result"] = "ok"
            else:
                output["result"] = "error"
            self.response.out.write(json.dumps(output))
        except:
            output["result"] = "error"
            self.response.out.write(json.dumps(output))