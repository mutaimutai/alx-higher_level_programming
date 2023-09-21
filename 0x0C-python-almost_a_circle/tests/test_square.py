import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """This is a test case for the class squre"""
    def test_update_with_args(self):
        """Testing using args"""
        square = Square(1,2,3,4)
        square.update(5,6,7,8)
        self.assertEqual(square.id, 5)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_update_with_kwargs(self):
        """Testing the update method using kwargs"""
        square = Square(1, 2, 3, 4)
        square.update(id=5, size=6, x=7, y=8)
        self.assertEqual(square.id, 5)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_update_with_args_and_kwargs(self):
        """Testing using mixture of args and kwargs"""
        square = Square(1, 2, 3, 4)
        square.update(id=5, size=6, x=7, y=8)
        self.assertEqual(square.id, 5)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_update_args_skips_kwargs(self):
        """Testing args skipping kwargs"""
        square = Square(1, 2, 3, 4)
        square.update(5, 6, 7, 8, id=9, size=10, x=11, y=12)
        self.assertEqual(square.id, 5)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_to_dictionary(self):
        """Test the to_dictionary method of the Square class"""
        square = Square(10, 2, 1, 1)
        square_dict = square.to_dictionary()
        expected_dict = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(square_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
