import unittest
from gaetestbed import DataStoreTestCase
from datastore.user import *
from datastore.post import *
from datastore.follow import *
from datetime import date
import urllib
IMG_URL = "http://static4.businessinsider.com/image/51f03f966bb3f73c7700000b-480/big-mac-mcdonalds.jpg"
IMG_DATA = urllib.urlopen(IMG_URL).read()

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
        p = Post(user=u, title="First Post", photo=IMG_DATA)
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
        addPost(u, "My food is awesome", IMG_DATA)
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
        addPost(u, "My food is awesome", IMG_DATA)
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
        post_id = addPost(u, "My food is awesome", IMG_DATA)
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
        addPost(u2, "My food is awesome", IMG_DATA)
        addPost(u2, "My food is very very awesome", IMG_DATA)
        addPost(u3, "My food is even more awesome", IMG_DATA)
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
        post_id = addPost(u, "My food is awesome", IMG_DATA)
        self.assertEqual(Post.all().count(), 1)
        if (addIngredients(post_id, ['cebola', 'batata'])):
            self.assertEqual(Post.get_by_id(post_id).ingredients, ['cebola', 'batata'] )
            
    def test_datastore_addRating(self):
        self.assertEqual(Post.all().count(), 0)
        u = User(birthday = date(2000, 3, 11),
                 name = "Carlos",
                 email = "carlos@gmail.com",
                 password = "Hdjdejdh3h",
                 gender = "m"
                 )
        u.put()
        post_id = addPost(u, "My food is awesome", IMG_DATA)
        self.assertEqual(Post.all().count(), 1)
        if (addRating(post_id, 5)):
            self.assertEqual(Post.get_by_id(post_id).rating, 5 )
        
        
        
    def test_datastore_addReceipt(self):
        self.assertEqual(Post.all().count(), 0)
        u = User(birthday = date(2000, 3, 11),
                 name = "Carlos",
                 email = "carlos@gmail.com",
                 password = "Hdjdejdh3h",
                 gender = "m"
                 )
        u.put()
        post_id = addPost(u, "My food is awesome", IMG_DATA)
        self.assertEqual(Post.all().count(), 1)
        if (addReceipt(post_id, "Cozer as batatas numa panela com agua e sal. Deitar as cebolas.")):
            self.assertEqual(Post.get_by_id(post_id).receipt, "Cozer as batatas numa panela com agua e sal. Deitar as cebolas." )
            
    def test_datastore_get_posts(self):
        self.assertEqual(Post.all().count(), 0)
        u = User(birthday = date(2000, 3, 11),
                 name = "Carlos",
                 email = "carlos@gmail.com",
                 password = "Hdjdejdh3h",
                 gender = "m"
                 )
        u.put()
        u2 = User(birthday = date(1987, 5, 22),
                 name = "Susana",
                 email = "susana@gmail.com",
                 password = "Hdjdea3d5h",
                 gender = "f"
                 )
        u2.put()
        addPost(u, "My food is awesome", IMG_DATA)
        addPost(u, "My food is very awesome", IMG_DATA)
        addPost(u, "Batatas fritas com arroz", IMG_DATA)
        addPost(u, "Peito de peru grelhado com arroz de tomate", IMG_DATA)
        addPost(u, "Salada russa", IMG_DATA)
        addPost(u2, "Feijoada alentejana", IMG_DATA)
        addPost(u2, "Ervilha com carne de vaca e arroz branco", IMG_DATA)
        self.assertEqual(Post.all().count(), 7)
        posts = getPosts()
        self.assertEqual(len(posts), 7)
        
    def test_datastore_get_post_id(self):
        self.assertEqual(Post.all().count(), 0)
        u = User(birthday = date(2000, 3, 11),
                 name = "Carlos",
                 email = "carlos@gmail.com",
                 password = "Hdjdejdh3h",
                 gender = "m"
                 )
        u.put()
        post_id = addPost(u, "My food is awesome", IMG_DATA)
        self.assertEqual(Post.all().count(), 1)
        post = getPostByID(post_id)
        self.assertEqual(post.title, "My food is awesome")
        self.assertEqual(post.photo, IMG_DATA)
        
        
        
        
        
        
        
        