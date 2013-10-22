import unittest
from gaetestbed import DataStoreTestCase
from datastore.user import *
from datetime import date

class TestUser(DataStoreTestCase, unittest.TestCase):
    def test_datastore_gets_hit(self):
        self.assertEqual(User.all().count(), 0)
        u = User(birthday = date(2000, 3, 11),
                 name = "Carlos",
                 email = "carlos@gmail.com",
                 password = "Hdjdejdh3h",
                 gender = "m"
                 )
        u.put()
        self.assertEqual(User.all().count(), 0)

    def test_datastore_still_empty(self):
        self.assertEqual(User.all().count(), 0)
        
    def test_datastore_add_user(self):
        self.assertEqual(User.all().count(), 0)
        addUser("Susana", "susana@gmail.com", "iauhd83ISH", "f", date(1985, 5, 22))
        self.assertEqual(User.all().count(), 1)
        
    def test_datastore_login(self):
        addUser("Susana", "susana@gmail.com", "iauhd83ISH", "f", date(1985, 5, 22))
        self.assertNotEqual(loginUser("susana@gmail.com", "iauhd83ISH"), False)
        
    def test_datastore_search_user_name(self):
        addUser("Susana", "susana@gmail.com", "iauhd83ISH", "f", date(1985, 5, 22))
        
        
    
        