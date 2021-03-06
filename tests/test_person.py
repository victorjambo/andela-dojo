import unittest
from unittest import TestCase
from src.person import Person, Fellow, Staff


class TestPerson(TestCase):
    def setUp(self):
        self.vm_person = Person(1, 'victormutai')
        self.vm_fellow = Fellow(2, 'victormutai')
        self.vm_staff = Staff(3, 'victormutai')

    def test_instance(self):
        self.assertIsInstance(self.vm_staff, Staff)

    def test_inheritance(self):
        self.assertEqual(self.vm_person.email, self.vm_fellow.email)


if __name__ == '__main__':
    unittest.main()
