import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """This is the rectangle testcase which imports from unittest.TestCase"""

    def test_constructor(self):
        """Here we  test the attributes in the init method"""
        rectangle = Rectangle(5 ,10, 1, 2, 42)

        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 2)
        self.assertEqual(rectangle.id, 42)

    def test_setters(self):
        """We test the setter methods for the rectangle objects"""
        rectangle = Rectangle(5, 10)

        rectangle.width = 7
        self.assertEqual(rectangle.width, 7)
        rectangle.height = 12
        self.assertEqual(rectangle.height, 12)
        rectangle.x = 3
        rectangle.y = 4
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)

    def test_area_calculation(self):
        """Testing if the area will give us correct area"""
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

    def test_area_large_value(self):
        """Testing for large valuea"""
        rectangle = Rectangle(1000,1000)
        self.assertEqual(rectangle.area(), 1000000)

    def test_area_with_small_values(self):
        """Testing the area with small values"""
        rectangle = Rectangle(1, 1)
        self.assertEqual(rectangle.area(), 1)

    def test_single_argument(self):
        """Test when a single argument is given for a rectangle creation"""
        with self.assertRaises(TypeError):
            rectangle = Rectangle(7)
    def test_str_represention(self):
        """checking if the string reprsentation matches the expected format"""
        rectangle = Rectangle(4, 5, 2, 3, 1)
        expected = "[Rectangle] (1) 2/3 - 4/5"
        self.assertEqual(str(rectangle), expected)
    def test_update_with_args(self):
        """Testing the update method with positional arguments (*args)"""
        rectangle = Rectangle(1,1,1,1,1)
        rectangle.update(2,3,4,5,6)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 6)
    def test_update_with_kwargs(self):
        """Testing the update method with keyword arguments (**kwargs)"""
        rectangle = Rectangle(1,1,1,1,1)
        rectangle.update(id=2, width=3, height=4, x=5, y=6)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 6)

    def test_to_dictionary(self):
        """Test the function to dictionary for correct output"""
        rectangle = Rectangle(1, 2, 3, 4, 5)
        rect_dict = rectangle.to_dictionary()
        expected_dict = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(rect_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
