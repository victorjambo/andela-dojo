import unittest
from unittest import TestCase
from src.room import Room, Office, LivingSpace


class TestRoom(TestCase):
    def setUp(self):
        self.sm_room = Room('Steve Muthee')
        self.sm_office = Office('Steve Muthee')
        self.sm_living_space = LivingSpace('Steve Muthee')

    def test_instance(self):
        self.assertIsInstance(self.sm_office, Office)

    def test_inheritance(self):
        self.assertEqual(self.sm_room.get_room_name,
                         self.sm_living_space.get_room_name)

    # def test_create_room_successfully(self):
    #     my_class_instance = Room()
    #     initial_room_count = len(my_class_instance.all_rooms)
    #     blue_office = my_class_instance.create_room("Blue", "office")
    #     self.assertTrue(blue_office)
    #     new_room_count = len(my_class_instance.all_rooms)
    #     self.assertEqual(new_room_count - initial_room_count, 1)


if __name__ == '__main__':
    unittest.main()
