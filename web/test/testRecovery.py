import unittest
from google.appengine.api import mail
from google.appengine.ext import testbed
from gaetestbed import DataStoreTestCase
from datastore.user import *
from datetime import date

class TestRecovery(DataStoreTestCase, unittest.TestCase):

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_mail_stub()
        self.mail_stub = self.testbed.get_stub(testbed.MAIL_SERVICE_NAME)

    def tearDown(self):
        self.testbed.deactivate()

    def testMailSent(self):
        
        u = User(birthday = date(2000, 3, 11),
                 name = "Carlos",
                 email = "carlos@gmail.com",
                 password = "Hdjdejdh3h",
                 gender = "m"
                 )
        u.put()
        
        u2 = User(birthday = date(2000, 3, 11),
                 name = "Ana",
                 email = "example@ex.com",
                 password = "ewhuifhewifh",
                 gender = "f"
                 )
        u2.put()
        
        generateUserRecoveryToken("carlos@gmail.com")
        generateUserRecoveryToken("example@ex.com")
        
        messages = self.mail_stub.get_sent_messages(to='carlos@gmail.com')
        messages2 = self.mail_stub.get_sent_messages(to='example@ex.com')
        self.assertEqual(1, len(messages))
        self.assertEqual('carlos@gmail.com', messages[0].to)
        self.assertEqual('foodrific.service@gmail.com', messages[0].sender)
        self.assertEqual('Recuperacao de password', messages[0].subject)
        
        textbody =  str(messages[0].body)
        index1 = textbody.index('\n')
        part1 = textbody[index1 + 1:]
        index2 = part1.index('\n')
        part2 = part1[index2 + 1:]
        index3 = part2.index('\n')
        part3 = part2[index3 + 1:]
        index4 = part3.index('\n')
        part4 = part3[index4 + 2:]
        
        self.assertEqual("Ola.\n\nEfetuaste um pedido de recuperacao de password. Para prosseguir acede a http://foodrific.appspot.com/recovery?token=" + getUserToken("carlos@gmail.com") + " .\n\nA equipa Foodrific.", part4)
        
        self.assertEqual(1, len(messages2))
        
        self.assertEqual('example@ex.com', messages2[0].to)
        self.assertEqual('foodrific.service@gmail.com', messages2[0].sender)
        self.assertEqual('Recuperacao de password', messages2[0].subject)
        
        textbody =  str(messages2[0].body)
        index1 = textbody.index('\n')
        part1 = textbody[index1 + 1:]
        index2 = part1.index('\n')
        part2 = part1[index2 + 1:]
        index3 = part2.index('\n')
        part3 = part2[index3 + 1:]
        index4 = part3.index('\n')
        part4 = part3[index4 + 2:]
        
        self.assertEqual("Ola.\n\nEfetuaste um pedido de recuperacao de password. Para prosseguir acede a http://foodrific.appspot.com/recovery?token=" + getUserToken("example@ex.com") + " .\n\nA equipa Foodrific.", part4)