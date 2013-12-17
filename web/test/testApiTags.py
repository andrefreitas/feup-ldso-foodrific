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
class testApiTags(DataStoreTestCase, unittest.TestCase):
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
        self.post = Post(user=u, title="First Post", photo="DATA", ingredients=["chicken", "sauce", "cheese"])
        self.post.put()
        
    def testTags(self):
        addIngredient("chicken", None)
        addIngredient("sauce", None)
        addIngredient("cheese", None)
        response = self.testapp.get('/api/ing_tags', {"term" : "chi"})
        self.assertEqual(response.json, ["chicken"])
        response = self.testapp.get('/api/ing_tags', {"term" : "sa"})
        self.assertEqual(response.json, ["sauce"])
        response = self.testapp.get('/api/ing_tags', {"term" : "ch"})
        self.assertEqual(response.json, ["cheese", "chicken"])
        response = self.testapp.get('/api/ing_tags', {"term" : ""})
        self.assertEqual("cheese" in response.json, True)
        self.assertEqual("chicken" in response.json, True)
        self.assertEqual("sauce" in response.json, True)


    def tearDown(self):
        self.user.delete()
        self.post.delete()
        self.testbed.deactivate()