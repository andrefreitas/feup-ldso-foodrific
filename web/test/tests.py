import unittest
from gaetestbed import DataStoreTestCase
from datastore.user import User

class TestUser(DataStoreTestCase, unittest.TestCase):
    def test_datastore_gets_hit(self):
        self.assertEqual(User.all().count(), 0)
        u = User(birthday="20-02-1994")
        u.name = "Carlos"
        u.email = "carlos@gmail.com"
        u.password ="Hdjdejdh3h"

        u.gender = "m"
        u.put()
        self.assertEqual(User.all().count(), 1)

    def test_datastore_still_empty(self):
        self.assertEqual(User.all().count(), 0)