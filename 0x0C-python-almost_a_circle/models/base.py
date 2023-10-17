#!/usr/bin/python3
"""The base class for all classes"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Serialize an object to json string representation
        Args:
            list_dictionaries : The dictionary to be serialized to a json string
        """
        if list_dictionaries is None:
            return "[]"
        js_string = json.dumps(list_dictionaries)
        return js_string

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the json string representation of list_objs to a file
            Args:
                list_objs : Are list of instances who inherits from Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
