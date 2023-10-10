#!/usr/bin/python3
"""Loads from a json file"""
import json


def load_from_json_file(filename):
    """Creates an objectfrom a json file"""
    with open(filename, 'r', encoding='UTF8') as file:
        py_object = json.loads(file)
        return py_object
