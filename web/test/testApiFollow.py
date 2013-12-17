import unittest
import webapp2
import api
import webtest
import pages
from google.appengine.ext import testbed
from google.appengine.api import memcache
from gaetestbed import DataStoreTestCase
from datastore import *
from datetime import date 
import app

application = app.application
class testApiFollow(DataStoreTestCase, unittest.TestCase):
    def setUp(self):
        user_id = addUser("Andre Freitas", "p.andrefreitas1@gmail.com", "12345", "m", date(1985, 5, 22))
        user_id2 = addUser("Carla Vanessa", "carla@sapa.pt", "12345", "m", date(1985, 5, 22))
        self.user_id = user_id
        self.user_id2 = user_id2

        self.user = searchUserByID(user_id)
        self.user2 = searchUserByID(user_id2)


        self.testapp = webtest.TestApp(application)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_memcache_stub()

        response = self.testapp.get('/login_handler?email=p.andrefreitas1@gmail.com&password=12345')
       
        
    def testFollow(self):
        self.assertEqual(isUserFollowing(self.user_id, self.user_id2), False)
        response = self.testapp.get('/api/toggleFollow', {"user" : self.user_id2})
        self.assertEqual(isUserFollowing(self.user_id, self.user_id2), True)
        response = self.testapp.get('/api/toggleFollow', {"user" : self.user_id2})
        self.assertEqual(isUserFollowing(self.user_id, self.user_id2), False)


    def tearDown(self):
        self.user.delete()
        self.user2.delete()
        self.testbed.deactivate()