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
            list_dictionaries : The dictionary to be
            serialized to a json string
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
        dict_list = []
        with open(filename, 'w', encoding='UTF8') as js:
            if list_objs is None:
                js.write("[]")
            else:
                for i in list_objs:
                    dict_list.append(i.to_dictionary())
                js_lists = Base.to_json_string(dict_list)
                js.write(js_lists)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
