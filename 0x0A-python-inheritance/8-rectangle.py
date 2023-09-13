#!/usr/bin/python3
"""Defining a class named BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a class rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """This is condtactor that belongs to rectangle
        Args:
            width: Width of he rectangle
            height: Height f the rctangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
