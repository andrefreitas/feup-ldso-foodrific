import unittest
import webapp2
import api
import webtest
import pages
from google.appengine.ext import testbed
from google.appengine.api import memcache
from google.appengine.api import images
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

class testApiNewPost(DataStoreTestCase, unittest.TestCase):
    def setUp(self):
        self.testapp = webtest.TestApp(application)
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_memcache_stub()
        user_id = addUser("Andre Freitas", "p.andrefreitas@gmail.com", "12345", "m", date(1985, 5, 22))
        self.testapp.get('/login_handler?email=p.andrefreitas@gmail.com&password=12345')
        self.user = searchUserByID(user_id)

    def testNewPost(self):
        self.assertEqual(Post.all().count(), 0)
        title = "Good chicken"
        photo = webtest.Upload('photo.jpg', IMG_DATA)
        ingredients = "chicken,sauce"
        recipe = "Fry chicken in the pan"
        params = { "title" : title,
                   "photo" : photo,
                   "ingredients" : ingredients,
                   "recipe" : recipe
                 }
        response = self.testapp.post('/api/newpost', params)
        post_query = Post.all().filter("title =", title)
        post = post_query.get()
        self.assertEqual(post.title, title)
        image = images.Image(db.Blob(IMG_DATA))
        image.resize(width=STANDARD_WIDTH)
        photo = image.execute_transforms(output_encoding=images.JPEG)
        self.assertEqual(post.photo, photo)
        self.assertEqual(post.ingredients, ["chicken","sauce"])
        self.assertEqual(post.recipe, recipe)
        self.assertEqual(Post.all().count(), 1)
        post.delete()

    def tearDown(self):
        self.user.delete()
        self.testbed.deactivate()