#!/usr/bin/python3
"""The base class for all classes"""


class Base:
    """Defining the class base"""
    __nb_objects = 0
    def __init__(self, id=None):
        """The class constructor
        Args:
            id (int) : Tracks the number of objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
