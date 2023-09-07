#!/usr/bin/python3
"""Creating  rectangle"""


class Rectangle:
    """Defines a cless rectangle"""

    def __init__(self, width=0, height=0):
        """We initialize a blueprint representing a triangle.
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets and sets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError(" width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets and sets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Finds the area f the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculate the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Prints a string in a more redable form
        in our case its going to print a rectangle with "#"
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append("#")
            if i < self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """Returns the spring representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deleting an instance of the rectangle"""
        print("Bye rectangle...")
