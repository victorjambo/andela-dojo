import unittest
import sys
from unittest import TestCase
from cStringIO import StringIO
from src.dojo import Dojo


class TestDojo(TestCase):
    """arguments as received from docopt"""
    def setUp(self):
        self.dojo = Dojo()
        self.held, sys.stdout = sys.stdout, StringIO()
        self.args = {'<room_type>': 'office', '<room_name>': ['blue']}
        self.wrong_args = {'<room_type>': 'space', '<room_name>': ['blue']}
        self.person_args = {'-w': False,
                       '<designation>': 'staff',
                       '<first_name>': 'victor',
                       '<last_name>': 'mutai'}

    def test_create_room_successfully(self):
        """Test room creation with room count"""
        initial_room_count = len(self.dojo.all_rooms)
        self.dojo.create_room(self.args)
        new_room_count = len(self.dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_room(self):
        """Test create room"""
        result = "An Office called blue has been successfully created!\n"
        self.dojo.create_room(self.args)
        self.assertEqual(sys.stdout.getvalue(), result)

    def test_create_room_error(self):
        """Test error while creating room if wrong commands as passed"""
        with self.assertRaises(KeyError):
            self.dojo.create_room(self.wrong_args)

    def test_add_person_successfully(self):
        """Test add person"""
        result = "Staff victor mutai has"\
                 " been successfully added.\nNo office available\n"
        self.dojo.add_person(self.person_args)
        self.assertEqual(sys.stdout.getvalue(), result)
    
    def test_print_room(self):
        """test room"""
        self.dojo.create_room(self.args)
        self.dojo.add_person(self.person_args)
        result = ['blue']
        res = None
        close = sys.stdout
        sys.stdout = res
        self.dojo.print_room('blue')
        sys.stdout = close
        self.assertEqual(res, result)


if __name__ == '__main__':
    unittest.main()
