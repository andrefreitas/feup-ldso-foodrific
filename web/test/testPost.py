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
        p = Post(user=u, title="First Post", photo="photo_tester")
        p.put()
        self.assertEqual(Post.all().count(), 1)
        
    def test_datastore_add_post(self):
        self.assertEqual(Post.all().count(), 0)
        u = User(birthday = date(2000, 3, 11),
                 name = "Carlos",
                 email = "carlos@gmail.com",
                 password = "Hdjdejdh3h",
                 gender = "m"
                 )
        u.put()
        addPost(u, "My food is awesome", "photo_tester")
        self.assertEqual(Post.all().count(), 1)
        
    def test_datastore_get_posts_user(self):
        self.assertEqual(Post.all().count(), 0)
        u = User(birthday = date(2000, 3, 11),
                 name = "Carlos",
                 email = "carlos@gmail.com",
                 password = "Hdjdejdh3h",
                 gender = "m"
                 )
        u.put()
        addPost(u, "My food is awesome", "photo_tester")
        self.assertEqual(Post.all().count(), 1)
        user_id = getUserID("carlos@gmail.com")
        posts = getPostsByUser(user_id)
        self.assertEqual(len(posts), 1)
        
    def test_datastore_delete_post(self):
        self.assertEqual(Post.all().count(), 0)
        u = User(birthday = date(2000, 3, 11),
                 name = "Carlos",
                 email = "carlos@gmail.com",
                 password = "Hdjdejdh3h",
                 gender = "m"
                 )
        u.put()
        post_id = addPost(u, "My food is awesome", "photo_tester")
        self.assertEqual(Post.all().count(), 1)
        deletePost(post_id)
        self.assertEqual(Post.all().count(), 0)
        
        
        