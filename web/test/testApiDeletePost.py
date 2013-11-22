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

class testApiDeletePost(DataStoreTestCase, unittest.TestCase):
    def setUp(self):
        app = webapp2.WSGIApplication([('/api/delete_post', api.DeletePost)])
        self.testapp = webtest.TestApp(app)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        
    def tearDown(self):
     self.testbed.deactivate()

    def testCacheHandler(self):
        key = 'answer'
        value = '42'
        self.testbed.init_memcache_stub()
        params = {'key': key, 'value': value}
        # Then pass those values to the handler.
        response = self.testapp.post('/api/delete_post', params)
        # Finally verify that the passed-in values are actually stored in Memcache.
        #self.assertEqual(value, )