#!/usr/bin/python3
"""Defining the class square"""
from .rectangle import Rectangle


class Square(Rectangle):
    """This is a blueprint of an object that inherits from class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializing an object of the class square
        Args:
            size (int) : The size of the square
            x (int) : The X-coordinate of the square
            y (int) : The Y-coordinate of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overloading the str method to return string rep of square"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """Get the size of the square"""
        return self.width
        return self.height

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updating the instance attributes using args and kwargs
            Args:
                args : non-keyworded arguments
                kwargs : keyworded argumemts
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except Exception:
            pass

    def to_dictionary(self):
        """Return a dictionary representation of a square instance"""
        return ({'id': getattr(self, 'id'), 'size': getattr(self, 'size'),
                'x': getattr(self, 'x'), 'y': getattr(self, 'y')})
