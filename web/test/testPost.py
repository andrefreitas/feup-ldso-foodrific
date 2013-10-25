import unittest
from gaetestbed import DataStoreTestCase
from datastore.user import *
from datastore.post import *
from datastore.follow import *
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
        
    def test_datastore_get_stream(self):
        u1 = User(birthday = date(2000, 3, 11),
                 name = "Carlos",
                 email = "carlos@gmail.com",
                 password = "Hdjdejdh3h",
                 gender = "m"
                 )
        u1.put()
        u2 = User(birthday = date(1987, 5, 22),
                 name = "Susana",
                 email = "susana@gmail.com",
                 password = "iaisda12FE",
                 gender = "f"
                 )
        u2.put()
        u3 = User(birthday = date(1985, 5, 22),
                 name = "Luis",
                 email = "luis@gmail.com",
                 password = "itea12FE",
                 gender = "m"
                 )
        u3.put()
        user_id1 = getUserID("carlos@gmail.com")
        user_id2 = getUserID("susana@gmail.com")
        user_id3 = getUserID("luis@gmail.com")
        self.assertEqual(Follow.all().count(),0)
        addUserToFollow(user_id1, user_id2)
        addUserToFollow(user_id1, user_id3)
        self.assertEqual(Follow.all().count(), 2)
        self.assertEqual(Post.all().count(), 0)
        addPost(u2, "My food is awesome", "photo_tester")
        addPost(u2, "My food is very very awesome", "photo_tester2")
        addPost(u3, "My food is even more awesome", "photo_tester3")
        self.assertEqual(Post.all().count(), 3)
        posts = getPostsByUserFollowing(user_id1)
        self.assertEqual(len(posts), 3)
    
    def test_datastore_addIngredients(self):
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
        if (addIngredients(post_id, ['cebola', 'batata'])):
            self.assertEqual(Post.get_by_id(post_id).ingredients, ['cebola', 'batata'] )
        
        
        
        
        
        
        
        
        