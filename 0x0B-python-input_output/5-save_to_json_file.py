#!/usr/bin/python3
"""writes an Object to a text file using json format"""
import json


def save_to_json_file(my_obj, filename):
    """Changes a python object into a json file(serialize a python data structure)"""
    with open(filename, 'w', encoding="UTF8") as file:
        json.dump(my_obj, file)
    """We use dump for data stored in files
    and use dumps when dealing with in-memory data
    """
