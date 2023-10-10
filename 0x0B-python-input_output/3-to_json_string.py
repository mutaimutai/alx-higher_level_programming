#!/usr/bin/python3
"""JSON representation of an object (string)"""


def to_json_string(my_obj):
    """Returns the JSON representation of a string"""
    import json
    j_string = json.dumps(my_obj)
    return j_string
