import unittest
from gaetestbed import DataStoreTestCase
from datastore.user import *
from datastore.follow import *
from datetime import date
from datastore.follow import addUserToFollow

class TestFollow(DataStoreTestCase, unittest.TestCase):
    def test_datastore_add_user_follow(self):
        user_id1 = addUser("Susana", "susana@gmail.com", "iaisda12FE", "f", date(1987, 5, 22))
        user_id2 = addUser("Carlos", "carlos@gmail.com", "iDUD18nasE", "m", date(1997, 2, 1))
        self.assertEqual(user_id1, getUserID("susana@gmail.com"))
        self.assertEqual(User.all().count(), 2)
        self.assertEqual(Follow.all().count(), 0)
        addUserToFollow(user_id1, user_id2)
        self.assertEqual(Follow.all().count(), 1)
        
    def test_datastore_is_following(self):
        user_id1 = addUser("Susana", "susana@gmail.com", "iaisda12FE", "f", date(1987, 5, 22))
        user_id2 = addUser("Carlos", "carlos@gmail.com", "iDUD18nasE", "m", date(1997, 2, 1))
        self.assertEqual(User.all().count(), 2)
        self.assertEqual(Follow.all().count(), 0)
        addUserToFollow(user_id1, user_id2)
        self.assertEqual(Follow.all().count(), 1)
        is_following = isUserFollowing(user_id1, user_id2)
        self.assertTrue(is_following)
        is_following = isUserFollowing(user_id2, user_id1)
        self.assertFalse(is_following)
        
    def test_datastore_remove_following(self):
        user_id1 = addUser("Susana", "susana@gmail.com", "iaisda12FE", "f", date(1987, 5, 22))
        user_id2 = addUser("Carlos", "carlos@gmail.com", "iDUD18nasE", "m", date(1997, 2, 1))
        self.assertEqual(User.all().count(), 2)
        self.assertEqual(Follow.all().count(), 0)
        addUserToFollow(user_id1, user_id2)
        self.assertEqual(Follow.all().count(), 1)
        removeUserFollowing(user_id1, user_id2)
        self.assertEqual(Follow.all().count(), 0)
        
    
    