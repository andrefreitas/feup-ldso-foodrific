import unittest
from gaetestbed import DataStoreTestCase
from datastore.user import *
from datastore.post import *
from datastore.yummy import *
from datetime import date
from datastore.yummy import doYummy

class TestYummy(DataStoreTestCase, unittest.TestCase):
    def test_datastore_do_yummy(self):
        user_id = addUser("Carlos", "carlos@gmail.com", "jubdGi12", "m", date(2000, 3, 22))
        user = searchUserByID(user_id)
        post_id = addPost(user, "My food is awesome", "photo_tester")
        self.assertEqual(Yummy.all().count(), 0)
        yummy_done = doYummy(user_id, post_id)
        self.assertEqual(Yummy.all().count(), 1)
        self.assertTrue(yummy_done)
        yummy_done = doYummy(user_id, post_id)
        self.assertEqual(Yummy.all().count(), 1)
        self.assertFalse(yummy_done)
        
    def test_datastore_undo_yummy(self):
        user_id = addUser("Carlos", "carlos@gmail.com", "jubdGi12", "m", date(2000, 3, 22))
        user = searchUserByID(user_id)
        post_id = addPost(user, "My food is awesome", "photo_tester")
        self.assertEqual(Yummy.all().count(), 0)
        doYummy(user_id, post_id)
        self.assertEqual(Yummy.all().count(), 1)
        undoYummy(user_id, post_id)
        self.assertEqual(Yummy.all().count(), 0)
        
    def test_datastore_get_post_yummys(self):
        user_id = addUser("Carlos", "carlos@gmail.com", "jubdGi12", "m", date(2000, 3, 22))
        user = searchUserByID(user_id)
        post_id = addPost(user, "My food is awesome", "photo_tester")
        self.assertEqual(Yummy.all().count(), 0)
        doYummy(user_id, post_id)
        self.assertEqual(Yummy.all().count(), 1)
        yummys = getPostYummys(post_id)
        self.assertEqual(len(yummys), 1)

    def test_datastore_delete_post_yummys(self):
        user_id = addUser("Carlos", "carlos@gmail.com", "jubdGi12", "m", date(2000, 3, 22))
        user = searchUserByID(user_id)
        post_id = addPost(user, "My food is awesome", "photo_tester")
        self.assertEqual(Yummy.all().count(), 0)
        doYummy(user_id, post_id)
        self.assertEqual(Yummy.all().count(), 1)
        deletePostYummys(post_id)
        self.assertEqual(Yummy.all().count(), 0)