import unittest
from gaetestbed import DataStoreTestCase
from datastore.user import User
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
        self.assertEqual(User.all().count(), 1)

    def test_datastore_still_empty(self):
        self.assertEqual(User.all().count(), 0)