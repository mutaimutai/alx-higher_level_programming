import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """This is where we test the base class"""

    def test_id_increment(self):
        """Test that each instance has  unique ID."""
        base1 = Base()
        base2 = Base()
        self.assertNotEqual(base1.id, base2.id)

    def test_custom_id(self):
        """Test that custom id is corerectly set."""
        custom_id = 42
        base = Base(custom_id)
        self.assertEqual(base.id, custom_id)

    def test_default_id(self):
        """test that instances get assigned sequential ID's"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)


if __name__ == '__main__':
    unittest.main()
