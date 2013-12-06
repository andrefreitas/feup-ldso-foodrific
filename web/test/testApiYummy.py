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
class testApiYummy(DataStoreTestCase, unittest.TestCase):
    def setUp(self):
        user_id = addUser("Andre Freitas", "p.andrefreitas@gmail.com", "12345", "m", date(1985, 5, 22))
        self.testapp = webtest.TestApp(application)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_memcache_stub()
        response = self.testapp.get('/login_handler?email=p.andrefreitas@gmail.com&password=12345')
        u = searchUserByID(user_id)
        p = Post(user=u, title="First Post", photo="DATA")
        p.put()
        self.post_id = p.key().id()
       
        
    def tearDown(self):
        self.testbed.deactivate()
        
    def testYummy(self):
        response = self.testapp.get('/api/yummy?postId=' + str(self.post_id))
        self.assertEqual(response.json, {'answer':'done', 'result': 'ok'})
        self.assertEqual(1, len(getPostYummys(self.post_id)))
        response = self.testapp.get('/api/yummy?postId=' + str(self.post_id))
        self.assertEqual(0, len(getPostYummys(self.post_id)))
        user_id = addUser("Carlos Faria", "carlossdd@gfas.com", "12345", "m", date(1985, 5, 22))
        self.testapp.get('/login_handler?email=carlossdd@gfas.com&password=12345')
        response = self.testapp.get('/api/yummy?postId=' + str(self.post_id))
        self.assertEqual(response.json, {'answer':'done', 'result': 'ok'})
        self.assertEqual(1, len(getPostYummys(self.post_id)))
        self.testapp.get('/login_handler?email=p.andrefreitas@gmail.com&password=12345')
        response = self.testapp.get('/api/yummy?postId=' + str(self.post_id))
        self.assertEqual(response.json, {'answer':'done', 'result': 'ok'})
        self.assertEqual(2, len(getPostYummys(self.post_id)))

