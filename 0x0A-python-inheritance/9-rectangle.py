#!/usr/bin/python3
"""Defining a class rectangle that inherits from Base Geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a rectangle class that inherits from BaseGeometry"""

    def area(self):
        """Return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        class_name = self.__class__.__name__
        return "[{}] {}/{}".format(class_name, self.__width, self.__height)
