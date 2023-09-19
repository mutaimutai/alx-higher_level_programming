#!/usr/bin/python3
"""Defining a base class named Base"""


class Base:
    """This is the blueprint of the base class"""

    __nb_object = 0

    def __init__(self, id=None):
        """Object instatiation
        Args:
            id(int): you input the id here
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object
