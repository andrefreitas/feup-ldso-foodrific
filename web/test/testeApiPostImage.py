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
import urllib

STANDARD_WIDTH = 800

IMG_URL = "http://static4.businessinsider.com/image/51f03f966bb3f73c7700000b-480/big-mac-mcdonalds.jpg"
IMG_DATA = urllib.urlopen(IMG_URL).read()

application = app.application
class testApiPostImage(DataStoreTestCase, unittest.TestCase):
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
        self.post = Post(user=u, title="First Post", photo = IMG_DATA)
        self.post.put()
        self.post_id = self.post.key().id()

    def testGetPostImage(self):
        response = self.testapp.get('/api/postimage', {"id" : self.post_id})
        self.assertEqual(self.post.photo, response.body)

    def tearDown(self):
        self.user.delete()
        self.post.delete()
        self.testbed.deactivate()