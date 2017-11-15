import unittest
import sys
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from unittest import TestCase
from src.dojo import Dojo
from src.room import *
from src.person import *


class TestDojo(TestCase):
    """arguments as received from docopt"""
    def setUp(self):
        self.dojo = Dojo()
        self.held, sys.stdout = sys.stdout, StringIO()
        self.args = {'<room_type>': 'office', '<room_name>': ['blue']}
        self.red_args = {'<room_type>': 'office', '<room_name>': ['red']}
        self.wrong_args = {'<room_type>': 'space', '<room_name>': ['blue']}
        self.person_args = {'-w': False,
                            '<designation>': 'staff',
                            '<first_name>': 'victor',
                            '<last_name>': 'mutai'}
        self.reallocate_args = {'<new_room_name>': 'red',
                                '<person_identifier>': '1000'}

    def test_create_room_successfully(self):
        """Test room creation with room count"""
        initial_room_count = len(self.dojo.all_rooms)
        self.dojo.create_room(self.args)
        new_room_count = len(self.dojo.all_rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_room(self):
        """Test create room"""
        result = "\x1b[32mAn Office called blue has "\
                 "been successfully created!\x1b[0m\n"
        self.dojo.create_room(self.args)
        self.assertEqual(sys.stdout.getvalue(), result)

    def test_create_room_error(self):
        """Test error while creating room if wrong commands as passed"""
        with self.assertRaises(KeyError):
            self.dojo.create_room(self.wrong_args)

    def test_add_person_successfully(self):
        """Test add person"""
        self.dojo.add_person(self.person_args)
        self.assertEqual(len(self.dojo.all_people), 1)

    def test_room(self):
        """Test room"""
        self.dojo.create_room(self.args)
        self.dojo.add_person(self.person_args)
        self.assertEqual(self.dojo.all_rooms[0].room_name, 'blue')

    def test_unallocated_people(self):
        """Unallocated people"""
        available_room = []
        result = "\x1b[33mNo Office available\x1b[0m\n"
        self.dojo.selected_room(available_room, 'Office', 'victor', False)
        self.assertGreater(len(self.dojo.unallocated_people), 1)
        self.assertEqual(sys.stdout.getvalue(), result)

    def test_allocate_room(self):
        """Allocate room with no room"""
        result = "\x1b[33mNo office available\x1b[0m\n"
        self.dojo.allocate_random_room("new_person",
                                       "Fellow",
                                       True)
        self.assertEqual(sys.stdout.getvalue(), result)

    def test_available_room(self):
        """Test Available rooms"""
        blue = Office('blue')
        red = Office('red')
        rooms = [blue, red]
        rooms_with_occupants = {blue: ['vic', 'mut', 'sun'],
                                red: ['vic',
                                      'mut', 'sun', 'vic', 'mut', 'sun']}
        res = self.dojo.available_room(rooms, rooms_with_occupants)
        self.assertEqual([blue], res)

    def test_room_name_map(self):
        """List of all rooms and people"""
        self.dojo.create_room(self.args)
        self.dojo.add_person(self.person_args)
        res = len(self.dojo.room_name_map)
        self.assertEqual(res, 1)

    def test_reallocate_person(self):
        self.dojo.create_room(self.args)
        self.dojo.add_person(self.person_args)
        old_room = self.dojo.assigned_room(self.dojo.all_people[0])
        self.assertEqual(old_room.room_name, 'blue')
        self.assertEqual(len(self.dojo.all_people), 1)
        self.dojo.create_room(self.red_args)
        self.assertEqual(len(self.dojo.all_rooms), 2)
        is_room = self.dojo.is_within_room_type('blue', old_room)
        self.assertTrue(is_room)
        # Relocation
        self.dojo.reallocate_person(self.reallocate_args)
        new_room = self.dojo.assigned_room(self.dojo.all_people[0])
        self.assertEqual(new_room.room_name, 'red')

    def test_load_people(self):
        """Load people from file"""
        self.assertListEqual(self.dojo.all_people, [])
        self.dojo.load_people()
        self.assertGreater(30, len(self.dojo.unallocated_people))

    def test_get_person_by_id(self):
        """Get Person by Id"""
        self.dojo.add_person(self.person_args)
        self.assertEqual(len(self.dojo.all_people), 1)
        res = self.dojo.get_person_by_id(1000).name
        current_person = self.dojo.all_people[0].name
        self.assertEqual(res, current_person)

    def test_assign_room(self):
        """Assign room to any un-allocated persons"""
        self.test_load_people()
        self.dojo.create_room(self.args)
        initial_count = len(self.dojo.unallocated_people)
        args = {'<person_identifier>': '1000',
                '-w': False}
        self.dojo.assign_room(args)
        for room in self.dojo.office_with_occupants.values():
            self.assertEqual(len(room), 1)
        count = len(self.dojo.unallocated_people)
        self.assertEqual((initial_count - count), 1)


if __name__ == '__main__':
    unittest.main()
