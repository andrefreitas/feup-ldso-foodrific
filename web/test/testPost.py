import unittest
from gaetestbed import DataStoreTestCase
from datastore.user import *
from datastore.post import *
from datetime import date

class testPost(DataStoreTestCase, unittest.TestCase):
    def test_datastore_post(self):
        self.assertEqual(Post.all().count(), 0)
        self.assertEqual(User.all().count(), 0)
        u = User(birthday = date(2000, 3, 11),
                 name = "Carlos",
                 email = "carlos@gmail.com",
                 password = "Hdjdejdh3h",
                 gender = "m"
                 )
        u.put()
        self.assertEqual(User.all().count(), 1)
        #db_user = searchUserByEmail("carlos@gmail.com")
        p = Post(user=u, title="First Post", photo="photo_tester")
        p.put()
        self.assertEqual(Post.all().count(), 1)