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
class testLoginLogout(DataStoreTestCase, unittest.TestCase):
    def setUp(self):
        self.user_id = addUser("Andre Freitas", "p.andrefreitas@gmail.com", "12345", "m", date(1985, 5, 22))
        self.testapp = webtest.TestApp(application)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_memcache_stub()
        
       
    def tearDown(self):
        self.testbed.deactivate()
        
    def testLogin(self):
        response = self.testapp.get('/login_handler?email=p.andrefreitas@gmail.com&password=12345')
        # should redirect to feed
        self.assertEqual(response.status, "302 Moved Temporarily")
        session_response = self.testapp.get('/api/session_data')
        user_data = session_response.json["answer"]
        self.assertEqual(user_data["name"], "Andre Freitas")
        self.assertEqual(user_data["user"], "p.andrefreitas@gmail.com")
        self.assertEqual(user_data["user_id"], self.user_id)
        session_response = self.testapp.get('/api/session_data')
        # feed can't redirect because is loggedin
        response = self.testapp.get('/feed')
        self.assertEqual(response.status, "200 OK")
        response = self.testapp.get('/api/login?email=p.andrefreitas@gmail.com&password=12345')
        self.assertEqual(response.json["result"], "ok")
        self.assertEqual(response.json["answer"], "valid")
        response = self.testapp.get('/api/login?email=p.andrefreids@gmail.com&password=12345')
        self.assertEqual(response.json["result"], "ok")
        self.assertEqual(response.json["answer"], "invalid")
        response = self.testapp.get('/api/login?email=p.andrefreitas@gmail.com&password=')
        self.assertEqual(response.json["result"], "ok")
        self.assertEqual(response.json["answer"], "invalid")
        response = self.testapp.get('/api/login')
        self.assertEqual(response.json["result"], "ok")
        self.assertEqual(response.json["answer"], "invalid")
 

    def testLogout(self):
        response = self.testapp.get('/logout')
        self.assertEqual(response.status, "302 Moved Temporarily")
        response = self.testapp.get('/api/session_data')
        self.assertEqual(response.json["answer"], {})
        # feed redirect because of the logout
        response = self.testapp.get('/feed')
        self.assertEqual(response.status, "302 Moved Temporarily")
