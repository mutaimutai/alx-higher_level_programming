#!/usr/bin/python3
"""Defining the class square"""
from .rectangle import Rectangle


class Square(Rectangle):
    """This is a blueprint of a square object that inherits from class Rectangle"""
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
        return self.height

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updating the instance attributes using args and kwargs
            Args:
                args : non-keyworded arguments
                kwargs : keyworded argumemts
        """
        if args == None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        try:
            args[0] = self.id
            args[1] = self.size
            args[2] = self.x
            args[3] = self.y
        except Exception:
            pass
