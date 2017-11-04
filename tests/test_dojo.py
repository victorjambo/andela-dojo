import unittest
from unittest import TestCase
from src.dojo import Dojo


class TestDojo(TestCase):
    args = {'<room_type>': 'office', '<room_name>': ['blue']}
    wrong_args = {'<room_type>': 'offices', '<room_name>': ['blue']}

    def test_create_room_successfully(self):
        result = "An Office called blue has been successfully created!"
        res = Dojo().create_room(self.args)
        self.assertEqual(res, result)

    def test_create_room_error(self):
        res = Dojo().create_room(self.wrong_args)
        result = "offices invalid command!!! try office or livingspace"
        self.assertEqual(result, res)


if __name__ == '__main__':
    unittest.main()
