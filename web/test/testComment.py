import unittest
from gaetestbed import DataStoreTestCase
from datastore.user import *
from datastore.post import *
from datastore.comment import *
from datetime import date

class testComment(DataStoreTestCase, unittest.TestCase):
    def test_datastore_addComment(self):
        self.assertEqual(Post.all().count(), 0)
        self.assertEqual(User.all().count(), 0)
        self.assertEqual(Comment.all().count(), 0)
        u = User(birthday = date(2000, 3, 11),
                 name = "Carlos",
                 email = "carlos@gmail.com",
                 password = "Hdjdejdh3h",
                 gender = "m"
                 )
        user_id = u.put()
        self.assertEqual(User.all().count(), 1)
        p = Post(user=u, title="First Post", photo="photo_tester")
        post_id = p.put()
        self.assertEqual(Post.all().count(), 1)
        addComment(user_id.id(), post_id.id(), "Muito bom!! P.S. Nao faco a minima ideia do que seja este post!!!! :)")
        self.assertEqual(Comment.all().count(), 1)
        
    def test_datastore_deleteComment(self):
        self.assertEqual(Post.all().count(), 0)
        self.assertEqual(User.all().count(), 0)
        self.assertEqual(Comment.all().count(), 0)
        u = User(birthday = date(2000, 3, 11),
                 name = "Carlos",
                 email = "carlos@gmail.com",
                 password = "Hdjdejdh3h",
                 gender = "m"
                 )
        user_id = u.put()
        self.assertEqual(User.all().count(), 1)
        p = Post(user=u, title="First Post", photo="photo_tester")
        post_id = p.put()
        self.assertEqual(Post.all().count(), 1)
        comment_id = addComment(user_id.id(), post_id.id(), "Muito bom!! P.S. Nao faco a minima ideia do que seja este post!!!! :)")
        self.assertEqual(Comment.all().count(), 1)
        deleteComment(comment_id)
        self.assertEqual(Comment.all().count(), 0)
        
    def test_datastore_getCommentsForPost(self):
        self.assertEqual(Post.all().count(), 0)
        self.assertEqual(User.all().count(), 0)
        self.assertEqual(Comment.all().count(), 0)
        u = User(birthday = date(2000, 3, 11),
                 name = "Carlos",
                 email = "carlos@gmail.com",
                 password = "Hdjdejdh3h",
                 gender = "m"
                 )
        user_id = u.put()
        self.assertEqual(User.all().count(), 1)
        p = Post(user=u, title="First Post", photo="photo_tester")
        post_id = p.put()
        self.assertEqual(Post.all().count(), 1)
        addComment(user_id.id(), post_id.id(), "Muito bom!! P.S. Nao faco a minima ideia do que seja este post!!!! :)")
        addComment(user_id.id(), post_id.id(), "Muito bom!! :)")
        addComment(user_id.id(), post_id.id(), "P.S. Nao faco a minima ideia do que seja este post!!!! :)")
        addComment(user_id.id(), post_id.id(), ":)")
        self.assertEqual(Comment.all().count(), 4)
        comments = getCommentsForPost(post_id.id())
        self.assertEqual(len(comments), 4)

    def test_datastore_deleteCommentsForPost(self):
        self.assertEqual(Post.all().count(), 0)
        self.assertEqual(User.all().count(), 0)
        self.assertEqual(Comment.all().count(), 0)
        u = User(birthday = date(2000, 3, 11),
                 name = "Carlos",
                 email = "carlos@gmail.com",
                 password = "Hdjdejdh3h",
                 gender = "m"
                 )
        user_id = u.put()
        self.assertEqual(User.all().count(), 1)
        p = Post(user=u, title="First Post", photo="photo_tester")
        post_id = p.put()
        self.assertEqual(Post.all().count(), 1)
        addComment(user_id.id(), post_id.id(), "Muito bom!! P.S. Nao faco a minima ideia do que seja este post!!!! :)")
        addComment(user_id.id(), post_id.id(), "Muito bom!! :)")
        addComment(user_id.id(), post_id.id(), "P.S. Nao faco a minima ideia do que seja este post!!!! :)")
        addComment(user_id.id(), post_id.id(), ":)")
        self.assertEqual(Comment.all().count(), 4)
        deleteCommentsForPost(post_id.id())
        self.assertEqual(Comment.all().count(), 0)