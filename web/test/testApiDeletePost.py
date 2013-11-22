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
from google.appengine.ext.remote_api.remote_api_pb import Response

class testApiDeletePost(DataStoreTestCase, unittest.TestCase):
    def setUp(self):
        app = webapp2.WSGIApplication([('/api/delete_post', api.DeletePost)])
        self.testapp = webtest.TestApp(app)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        
    def tearDown(self):
        self.testbed.deactivate()
        
    def testCacheHandler(self):
        postId='192313712381723'
        self.testbed.init_memcache_stub()
        response = self.testapp.get('/api/delete_post?postId='+postId)
        response.decode_content
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.json, {'result': 'error'})
