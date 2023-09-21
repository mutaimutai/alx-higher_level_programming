import unittest
from models.base import Base
from models.rectangle import Rectangle

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

    def test_to_json_string_empty(self):
        """Test to_json_string with an empty list of dictionaries."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_non_empty(self):
        """Test to_json_string with a non-empty list of dictionaries."""
        data = [{"id": 1, "width": 2, "height": 3}, {"id": 4, "width": 5, "height": 6}]
        json_string = Base.to_json_string(data)
        self.assertEqual(json_string, '[{"id": 1, "width": 2, "height": 3}, {"id": 4, "width": 5, "height": 6}]')

    def test_save_to_file_empty_list(self):
        """Test save_to_file with an empty list of objects."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")

    def test_save_to_file_non_empty_list(self):
        """Test save_to_file with a non-empty list of objects."""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual(content, '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}, {"id": 2, "width": 3, "height": 4, "x": 0, "y": 0}]')

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty string."""
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_non_empty(self):
        """Test from_json_string with a non-empty string."""
        json_string = '[{"id": 1, "width": 2, "height": 3}, {"id": 4, "width": 5, "height": 6}]'
        data = Base.from_json_string(json_string)
        self.assertEqual(data, [{"id": 1, "width": 2, "height": 3}, {"id": 4, "width": 5, "height": 6}])

    def test_create_rectangle(self):
        """Test create method for creating a Rectangle object."""
        dictionary = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        r = Rectangle.create(**dictionary)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 4/5 - 2/3")

    def test_create_empty_dictionary(self):
        """Test create method with an empty dictionary."""
        dictionary = {}
        r = Rectangle.create(**dictionary)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 0/0 - 1/1")

    def test_load_from_file_non_existing(self):
        """Test load_from_file with a non-existing file."""
        rectangles = Rectangle.load_from_file()
        self.assertEqual(rectangles, [])

    def test_load_from_file_existing(self):
        """Test load_from_file with an existing file."""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        Rectangle.save_to_file([r1, r2])
        rectangles = Rectangle.load_from_file()
        self.assertEqual(len(rectangles), 2)
        self.assertEqual(rectangles[0].__str__(), "[Rectangle] (1) 0/0 - 1/2")
        self.assertEqual(rectangles[1].__str__(), "[Rectangle] (2) 0/0 - 3/4")



if __name__ == '__main__':
    unittest.main()
