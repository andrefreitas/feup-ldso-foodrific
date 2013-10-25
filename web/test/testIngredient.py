import unittest
from gaetestbed import DataStoreTestCase
from datastore.ingredient import *
from datetime import date

class testPost(DataStoreTestCase, unittest.TestCase):
    def test_datastore_addIngredient(self):
        self.assertEqual(Ingredient.all().count(), 0)
        addIngredient("Arroz", "/photos/user/rice")
        self.assertEqual(Ingredient.all().count(), 1)
        addIngredient("Arroz", "/photos/user/rice2")
        self.assertEqual(Ingredient.all().count(), 1)
