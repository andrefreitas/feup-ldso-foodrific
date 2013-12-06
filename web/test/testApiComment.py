import unittest
import webapp2
import api
import webtest
import pages
from google.appengine.ext import testbed
from google.appengine.api import memcache
from gaetestbed import DataStoreTestCase
from datastore.user import *
from datastore.post import *
from datastore.comment import *
from datastore.yummy import *
from datetime import date 
import app

application = app.application
class testApiComment(DataStoreTestCase, unittest.TestCase):
    def setUp(self):
        user_id = addUser("Andre Freitas", "p.andrefreitas1@gmail.com", "12345", "m", date(1985, 5, 22))
        self.user_id = user_id
        self.testapp = webtest.TestApp(application)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_memcache_stub()
        response = self.testapp.get('/login_handler?email=p.andrefreitas1@gmail.com&password=12345')
        u = searchUserByID(user_id)
        self.user = u
        self.post = Post(user=u, title="First Post", photo="DATA")
        self.post.put()
        self.post_id = self.post.key().id()
        self.post.delete()
       
        
    def testComment(self):
        params = { "postId" : str(self.post_id),
                   "comment" : "awesome dude"
                 }
        response = self.testapp.get('/api/new_comment', params)
        comment_id = int(response.json["comment_id"])
        self.comment_id = comment_id
        comment = Comment.get_by_id(comment_id)
        self.assertEqual(comment.content, params["comment"])
        self.assertEqual(response.json["answer"], "done")
        self.assertEqual(response.json["result"], "ok")
        self.assertEqual(len(getCommentsForPost(self.post_id)), 1)
        comment.delete()
        self.assertEqual(len(getCommentsForPost(self.post_id)), 0)

    def testDeleteComment(self):
        comment_id = addComment(self.user_id, self.post_id, "lol")
        self.assertEqual(len(getCommentsForPost(self.post_id)), 1)
        params = { "comment_id" : comment_id}
        response = self.testapp.get('/api/delete_comment', params)
        self.assertEqual(Comment.get_by_id(comment_id), None)
        self.assertEqual(len(getCommentsForPost(self.post_id)), 0)

    def tearDown(self):
        self.user.delete()
        self.post.delete()
        self.testbed.deactivate()