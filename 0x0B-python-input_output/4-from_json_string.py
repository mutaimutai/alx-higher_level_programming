#!/usr/bin/python3
"""Defining from json to string function"""


def from_json_string(my_str):
    """Decodes a json string to a python Object"""
    import json
    py_object = json.loads(my_str)
    return py_object
