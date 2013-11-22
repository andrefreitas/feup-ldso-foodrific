import unittest
import webapp2
import api
import webtest
from google.appengine.ext import testbed
from google.appengine.api import memcache
from gaetestbed import DataStoreTestCase
from datastore.user import addUser
from datetime import date

class testApiSendRecover(DataStoreTestCase, unittest.TestCase):
    def setUp(self):
        app = webapp2.WSGIApplication([('/api/send_recover', api.SendRecover)])
        self.testapp = webtest.TestApp(app)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        
    def tearDown(self):
        self.testbed.deactivate()
        
    def testEmailNonExistent(self):
        self.testbed.init_memcache_stub()
        response = self.testapp.get('/api/send_recover?email=peter@gmail.com')
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.json, {'answer':'invalid', 'result': 'ok'})
        
    def testEmail(self):
        addUser("Susana", "susana@gmail.com", "iauhd83ISH", "f", date(1985, 5, 22))
        self.testbed.init_memcache_stub()
        response = self.testapp.get('/api/send_recover?email=susana@gmail.com')
        self.assertEqual(response.status, "200 OK")
        self.assertEqual(response.json, {'answer':'valid', 'result': 'ok'})