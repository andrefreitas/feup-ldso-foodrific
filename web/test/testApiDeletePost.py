import unittest
import webapp2
import api
import webtest
from google.appengine.ext import testbed
from google.appengine.api import memcache
from gaetestbed import DataStoreTestCase
from datastore.user import *
from datastore.post import *
from datastore.comment import *
from datetime import date
import urllib
IMG_URL = "http://static4.businessinsider.com/image/51f03f966bb3f73c7700000b-480/big-mac-mcdonalds.jpg"
IMG_DATA = urllib.urlopen(IMG_URL).read()

class testApiDeletePost(DataStoreTestCase, unittest.TestCase):
    def setUp(self):
        app = webapp2.WSGIApplication([('/api/delete_post', api.DeletePost)])
        self.testapp = webtest.TestApp(app)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        
    def tearDown(self):
        self.testbed.deactivate()
        
    def testDeletePostNonExistent(self):
        postId='192313712381723'
        self.testbed.init_memcache_stub()
        response = self.testapp.get('/api/delete_post?postId='+postId)
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.json, {'answer':'invalid', 'result': 'error'})
        
    def testDeletePost(self):
        self.assertEqual(Post.all().count(), 0)
        self.assertEqual(User.all().count(), 0)
        u = User(birthday = date(2000, 3, 11),
                 name = "Carlos",
                 email = "carlos@gmail.com",
                 password = "Hdjdejdh3h",
                 gender = "m"
                 )
        u.put()
        self.assertEqual(User.all().count(), 1)
        postId = addPost(u, "My food is awesome", IMG_DATA)
        self.assertEqual(Post.all().count(), 1)
        self.testbed.init_memcache_stub()
        response = self.testapp.get('/api/delete_post?postId='+str(postId))
        response.decode_content
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.json, {'answer':'valid', 'result': 'ok'})
