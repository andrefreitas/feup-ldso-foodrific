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
        self.assertEqual(User.all().count(), 1)

    def test_datastore_still_empty(self):
        self.assertEqual(User.all().count(), 0)
        
    def test_datastore_add_user(self):
        self.assertEqual(User.all().count(), 0)
        addUser("Susana", "susana@gmail.com", "iauhd83ISH", "f", date(1985, 5, 22))
        self.assertEqual(User.all().count(), 1)
        result = addUser("Susana", "susana@gmail.com", "iauhd83ISH", "f", date(1985, 5, 22))
        self.assertFalse(result)
        result = addUser("Susana", "susanaasda@gmail.com", "iauhd83ISH", "f", date(1985, 5, 22))
        self.assertNotEqual(result, False)
        
    def test_datastore_login(self):
        self.assertEqual(User.all().count(), 0)
        addUser("Susana", "susana@gmail.com", "iauhd83ISH", "f", date(1985, 5, 22))
        self.assertEqual(User.all().count(), 1)
        self.assertNotEqual(loginUser("susana@gmail.com", "iauhd83ISH"), False)
        
    def test_get_user_id(self):
        self.assertEqual(User.all().count(), 0)
        addUser("Susana", "susana@gmail.com", "iauhd83ISH", "f", date(1985, 5, 22))
        self.assertEqual(User.all().count(), 1)
        user_id = getUserID("susana@gmail.com")
        user = searchUserByID(user_id)
        self.assertEqual(user.email, "susana@gmail.com")
        
    def test_datastore_is_user(self):
        self.assertEqual(User.all().count(), 0)
        addUser("Susana", "susana@gmail.com", "iauhd83ISH", "f", date(1985, 5, 22))
        self.assertEqual(User.all().count(), 1)
        self.assertTrue(isUser("susana@gmail.com"))
        
    def test_datastore_search_user_email(self):
        self.assertEqual(User.all().count(), 0)
        addUser("Susana", "susana@gmail.com", "iauhd83ISH", "f", date(1985, 5, 22))
        self.assertEqual(User.all().count(), 1)
        user = searchUserByEmail("susana@gmail.com")
        self.assertTrue(user.email=="susana@gmail.com")
        
    """def test_datastore_search_user_name(self):
        addUser("Susana", "susana@gmail.com", "iauhd83ISH", "f", date(1985, 5, 22))
        addUser("Silva Susana", "susanasilva@gmail.com", "iauhd83ISHasdas", "f", date(1987, 7, 22))
        users = searchUserByName("Susana")
        self.assertEqual(User.all().count(), 2)
        self.assertEqual(len(users), 2)
        for user in users:
            self.assertEqual(user.name, "Susana")"""
        
    def test_datastore_delete_user(self):
        self.assertEqual(User.all().count(), 0)
        addUser("Susana", "susana@gmail.com", "iauhd83ISH", "f", date(1985, 5, 22))
        self.assertEqual(User.all().count(), 1)
        user = searchUserByEmail("susana@gmail.com")
        deleteUser(user.key().id())
        self.assertEqual(User.all().count(), 0)
        
    def test_datastore_edit_user(self):
        self.assertEqual(User.all().count(), 0)
        addUser("Susana", "susana@gmail.com", "iauhd83ISH", "f", date(1985, 5, 22))
        self.assertEqual(User.all().count(), 1)
        editUser("SusanaG", "susana@gmail.com", "susanag@gmail.com", "123456", "f", date(1980, 3, 20))
        self.assertEqual(User.all().count(), 1)
        user = searchUserByEmail("susanag@gmail.com")
        self.assertEqual(user.name, "SusanaG")
        self.assertEqual(user.email, "susanag@gmail.com")
        self.assertEqual(user.password, encrypt("123456"))
        self.assertEqual(user.gender, "f")
        self.assertEqual(user.birthday, date(1980, 3, 20))
        
    def test_datastore_search_user_id(self):
        self.assertEqual(User.all().count(), 0)
        addUser("Susana", "susana@gmail.com", "iauhd83ISH", "f", date(1985, 5, 22))
        self.assertEqual(User.all().count(), 1)
        user = searchUserByEmail("susana@gmail.com")
        user2 = searchUserByID(user.key().id()) 
        self.assertEqual(user.name, user2.name)
        self.assertEqual(user.email, user2.email)
        self.assertEqual(user.password, user2.password)
        self.assertEqual(user.gender, user2.gender)
        self.assertEqual(user.birthday, user2.birthday)
        
        
    def test_datastore_photo(self):
        self.assertEqual(User.all().count(), 0)
        addUser("Susana", "susana@gmail.com", "iauhd83ISH", "f", date(1985, 5, 22))
        self.assertEqual(User.all().count(), 1)
        user = searchUserByEmail("susana@gmail.com")
        user_id = user.key().id()
        addPhotoToUser(user_id, "photo_test")
        photo = getPhotoByUser(user_id)
        self.assertEqual(photo, "photo_test")
        editPhotoUser(user_id, "another_photo_test")
        photo_edit = getPhotoByUser(user_id)
        self.assertEqual(photo_edit, "another_photo_test")
        
    
        
    

        