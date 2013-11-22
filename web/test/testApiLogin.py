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

class testApiLogin(DataStoreTestCase, unittest.TestCase):
    def setUp(self):
        app = webapp2.WSGIApplication([('/api/login', api.Login)])
        self.testapp = webtest.TestApp(app)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        
    def tearDown(self):
        self.testbed.deactivate()
        
    def testLoginNonExistent(self):
        self.testbed.init_memcache_stub()
        response = self.testapp.get('/api/login?email=peter@gmail.com&password=123456')
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.json, {'answer':'invalid', 'result': 'ok'})
    
    def testLogin(self):
        addUser("Susana", "susana@gmail.com", "iauhd83ISH", "f", date(1985, 5, 22))
        self.testbed.init_memcache_stub()
        response = self.testapp.get('/api/login?email=susana@gmail.com&password=iauhd83ISH')
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.json, {'answer':'valid', 'result': 'ok'})