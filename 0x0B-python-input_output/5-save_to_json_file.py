#!/usr/bin/python3
"""writes an Object to a text file using json format"""
import json


def save_to_json_file(my_obj, filename):
    """writes json  to a text filestr from py_object using json format"""
    with open(filename, 'w', encoding="UTF8") as file:
        json.dump(my_obj, file)
