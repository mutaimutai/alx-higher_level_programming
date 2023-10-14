#!/usr/bin/python3
"""Class student with method  that retrieves a dictionary rep of an object"""


class Student:
    """Class students that creates an object"""
    def __init__(self, first_name, last_name, age):
        """Instantiating a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of the Student"""
        if attrs is None:
            return (self.__dict__)
        else:
            new_dict = {}
            for a in attrs:
                try:
                    new_dict[a] = self.__dict__[a]
                except:
                    pass
            return new_dict

