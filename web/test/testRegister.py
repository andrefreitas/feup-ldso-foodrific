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
import hashlib

application = app.application
class testRegister(DataStoreTestCase, unittest.TestCase):
    def setUp(self):
        self.testapp = webtest.TestApp(application)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_memcache_stub()

    def tearDown(self):
        self.testbed.deactivate()
        
    def testRegister(self):
        params = {"name": "Andre",
                  "email": "p.andrefreitas@gmail.com",
                  "password": "12345",
                  "gender": "m",
                  "birthday" : "20/03/2000"
                 }
        response = self.testapp.post('/register_handler', params)
        self.assertEqual(response.status, "302 Moved Temporarily")
        user = searchUserByEmail(params["email"])
        self.assertEqual(user.name, params["name"])
        self.assertEqual(user.email, params["email"])
        self.assertEqual(user.gender, params["gender"])
        self.assertEqual(user.birthday, date(2000, 03, 20))
        self.assertEqual(user.password, hashlib.sha256(params["password"]).hexdigest())