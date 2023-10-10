#!/usr/bin/python3
"""writes an Object to a text file"""


def save_to_json_file(my_obj, filename):
    """writes json str from py_object""" 
    import json
    json_string = json.dumps(my_obj)
    with open(filename, 'w', encoding="UTF8") as file:
        file.write(json_string)
