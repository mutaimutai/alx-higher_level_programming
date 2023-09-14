#!/usr/bin/python3
import json
"""Returning the JSON representationof an object(string)"""



def to_json_string(my_obj):
    """This function returns the json representation of a string"""
    json_string = json.dumps(my_obj)
    with open('mydata.json', 'w') as f:
        f.write(json_string)
