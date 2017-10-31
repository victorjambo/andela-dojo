import unittest
from unittest import TestCase
from src.person import Person, Fellow, Staff


class TestPerson(TestCase):
    def setUp(self):
        self.vm_person = Person('victor', 'mutai')
        self.vm_fellow = Fellow('victor', 'mutai')
        self.vm_staff = Staff('victor', 'mutai')

    def test_instance(self):
        self.assertIsInstance(self.vm_staff, Staff)

    def test_inheritance(self):
        self.assertEqual(self.vm_person.email, self.vm_fellow.email)


if __name__ == '__main__':
    unittest.main()
