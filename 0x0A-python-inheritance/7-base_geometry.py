#!/usr/bin/python3
"""Defining a class named BaseGeometry"""


class BaseGeometry:
    """This is the class that i have implemented"""

    def area(self):
        """This method is not impemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates if a value is an integer
        Args:
            name: This is a string
            value: Ths is the value to validate
        Returns:
            returns true if the value is an integer
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        
