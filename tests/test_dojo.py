import unittest
import sys
from unittest import TestCase
from cStringIO import StringIO
from src.dojo import Dojo


class TestDojo(TestCase):
    args = {'<room_type>': 'office', '<room_name>': ['blue']}
    wrong_args = {'<room_type>': 'offices', '<room_name>': ['blue']}
    person_args = {'-w': False,
                   '<designation>': 'staff',
                   '<first_name>': 'victor',
                   '<last_name>': 'mutai'}
    
    def setUp(self):
        self.dojo = Dojo()
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_create_room_successfully(self):
        result = "An Office called blue has been successfully created!\n"
        self.dojo.create_room(self.args)
        self.assertEqual(sys.stdout.getvalue(), result)

    def test_create_room_error(self):
        with self.assertRaises(KeyError):
            self.dojo.create_room(self.wrong_args)
            
    def test_add_person_successfully(self):
        result = "Staff victor mutai has been successfully added.\nNo room available\n"
        self.dojo.add_person(self.person_args)
        self.assertEqual(sys.stdout.getvalue(), result)

if __name__ == '__main__':
    unittest.main()
