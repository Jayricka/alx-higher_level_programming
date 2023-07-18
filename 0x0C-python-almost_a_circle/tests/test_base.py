"""
Unit tests for the Base class.
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_base_creation_with_id(self):
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_base_creation_without_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_base_creation_with_mixed_ids(self):
        b1 = Base()
        self.assertEqual(b1.id, 3)

        b2 = Base(20)
        self.assertEqual(b2.id, 20)

        b3 = Base()
        self.assertEqual(b3.id, 4)

if __name__ == '__main__':
    unittest.main()
