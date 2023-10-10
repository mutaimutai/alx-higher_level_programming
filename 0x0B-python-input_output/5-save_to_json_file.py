#!/usr/bin/python3
"""writes an Object to a text file"""


def save_to_json_file(my_obj, filename):
    """This function writes an object to 
    a text file using JSON representation
    """
    import json
    with open(filename, 'w', encoding="UTF8") as file:
        filename = json.dumps(my_obj)
