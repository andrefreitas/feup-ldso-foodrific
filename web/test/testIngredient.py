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

    def test_datastore_existIngredient(self):
    	self.assertEqual(Ingredient.all().count(), 0)
        addIngredient("Arroz", None)
        self.assertEqual(Ingredient.all().count(), 1)
        addIngredient("Arroz", None)
        self.assertEqual(Ingredient.all().count(), 1)
        addIngredient("Frango", None)
        self.assertEqual(Ingredient.all().count(), 2)
        addIngredient("ervilhas", None)
        self.assertEqual(Ingredient.all().count(), 3)
        addIngredient("puré", None)
        self.assertEqual(Ingredient.all().count(), 4)
        self.assertEqual(Ingredient.existIngredient("ervilhas"), True)
        
