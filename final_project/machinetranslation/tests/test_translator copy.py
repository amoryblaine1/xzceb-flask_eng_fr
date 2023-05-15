
import unittest

from translator import english_to_french, french_to_english

class test_tranlsate_english(unittest.TestCase):

    def test_etof_equal(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_etof_notequal(self):
        self.assertNotEqual(english_to_french("Hello"), "Sumy")

class test_translate_french(unittest.TestCase):
    
    def test_etof_equal(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    
    def test_etof_notequal(self):
        self.assertNotEqual(french_to_english("Bonjour"), "Sumy")

unittest.main()