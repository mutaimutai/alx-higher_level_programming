#!/usr/bin/python3
"""Defining a class rectangle"""


class Rectangle:
    """A blue print of the rectangle"""

    def __init__(self, width=0, height=0):
        """Method to initialiaze an object.
        Args:
            width : width of the rectangle.
            height : height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of the width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """Calculates the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return ((2 * self.width) + (2 * self.height))

    def __str__(self):
        """String representation of a rectangle"""
        if self.width == 0 or self.height == 0:
            return ""

        rectangle_str = ""

        for i in range(self.height):
            rectangle_str += "#" * self.width
            if i < self.height -1:
                rectangle_str += "\n"
        return rectangle_str
