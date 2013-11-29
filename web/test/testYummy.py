import unittest
from gaetestbed import DataStoreTestCase
from datastore.user import *
from datastore.post import *
from datastore.yummy import *
from datetime import date
from datastore.yummy import toogleYummy
import urllib

IMG_URL = "http://static4.businessinsider.com/image/51f03f966bb3f73c7700000b-480/big-mac-mcdonalds.jpg"
IMG_DATA = urllib.urlopen(IMG_URL).read()

class TestYummy(DataStoreTestCase, unittest.TestCase):
    def test_datastore_do_yummy(self):
        user_id = addUser("Carlos", "carlos@gmail.com", "jubdGi12", "m", date(2000, 3, 22))
        user = searchUserByID(user_id)
        post_id = addPost(user, "My food is awesome", IMG_DATA)
        self.assertEqual(Yummy.all().count(), 0)
        yummy_done = toogleYummy(user_id, post_id)
        self.assertEqual(Yummy.all().count(), 1)
        self.assertTrue(yummy_done)
        yummy_done = toogleYummy(user_id, post_id)
        self.assertEqual(Yummy.all().count(), 0)
        self.assertFalse(yummy_done)
        
    def test_datastore_undo_yummy(self):
        user_id = addUser("Carlos", "carlos@gmail.com", "jubdGi12", "m", date(2000, 3, 22))
        user = searchUserByID(user_id)
        post_id = addPost(user, "My food is awesome", IMG_DATA)
        self.assertEqual(Yummy.all().count(), 0)
        toogleYummy(user_id, post_id)
        self.assertEqual(Yummy.all().count(), 1)
        toogleYummy(user_id, post_id)
        self.assertEqual(Yummy.all().count(), 0)
        
    def test_datastore_get_post_yummys(self):
        user_id = addUser("Carlos", "carlos@gmail.com", "jubdGi12", "m", date(2000, 3, 22))
        user = searchUserByID(user_id)
        post_id = addPost(user, "My food is awesome", IMG_DATA)
        self.assertEqual(Yummy.all().count(), 0)
        toogleYummy(user_id, post_id)
        self.assertEqual(Yummy.all().count(), 1)
        yummys = getPostYummys(post_id)
        self.assertEqual(len(yummys), 1)

    def test_datastore_delete_post_yummys(self):
        user_id = addUser("Carlos", "carlos@gmail.com", "jubdGi12", "m", date(2000, 3, 22))
        user = searchUserByID(user_id)
        post_id = addPost(user, "My food is awesome", IMG_DATA)
        self.assertEqual(Yummy.all().count(), 0)
        toogleYummy(user_id, post_id)
        self.assertEqual(Yummy.all().count(), 1)
        deletePostYummys(post_id)
        self.assertEqual(Yummy.all().count(), 0)