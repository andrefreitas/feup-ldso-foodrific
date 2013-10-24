from google.appengine.ext import db
from user import User

# ----------------- CLASS FOLLOW -----------------
class Follow(db.Model):
    user_follower = db.ReferenceProperty(User, collection_name="follower_set")
    user_following = db.ReferenceProperty(User, collection_name="following_set")
    
    
# ----------------- FUNCTIONS FOLLOW -----------------
def addUserToFollow(user_id_follower, user_id_following):
    follow = Follow(user_follower = User.get_by_id(user_id_follower), user_following = User.get_by_id(user_id_following))
    follow.put()
    return True

def isUserFollowing(user_id_follower, user_id_following):
    user_follower = User.get_by_id(user_id_follower)
    user_following = User.get_by_id(user_id_following)
    follow_query = db.GqlQuery("SELECT * FROM Follow WHERE user_follower = :1 AND user_following = :2", user_follower, user_following)
    is_follow = follow_query.get()
    if(is_follow is not None):
        return True
    else:
        return False
    
def removeUserFollowing(user_id_follower, user_id_following):
    user_follower = User.get_by_id(user_id_follower)
    user_following = User.get_by_id(user_id_following)
    follow_query = db.GqlQuery("SELECT * FROM Follow WHERE user_follower = :1 AND user_following = :2", user_follower, user_following)
    db.delete(follow_query.get())
    
