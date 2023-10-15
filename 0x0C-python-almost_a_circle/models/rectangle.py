#!/usr/bin/python3
"""Class rectangle that inherits from Base"""

from .base import Base

class Rectangle(Base):
    """Defining the class Rectangle which inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing an instance of the rectangle class
        Args:
            width (int): Width of the rectangle
            height (int) : Height of the rectangle
            x (int) : The X-coordinate of the rectangle
            y (int) : The Y-coordinate of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of width
        Args:
            value (int) : value of width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of height
        Args:
            value (int) : value of height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the X-coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of X-coordinate
        Args:
            value (int) : value of X-coordinate
        """
        if type(value) != int:
            raise TypeError("x  must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the Y-coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the value of the Y-coordinate
        Args:
            value (int) : value of the Y-coordinate
        """
        if type(value) != int:
            raise TypeError("y  must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height
