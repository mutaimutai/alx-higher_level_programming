#!/usr/bin/python3
"""Class student with method  that retrieves a dictionary rep of an object"""


class Student:
    """Class students that creates an object"""
    def __init__(self, first_name, last_name, age):
        """Instantiating a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dictionary representation of the Student"""
        return (self.__dict__)
