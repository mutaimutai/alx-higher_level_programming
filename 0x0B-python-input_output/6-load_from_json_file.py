#!/usr/bin/python3
"""Loads from a json file"""
import json


def load_from_json_file(filename):
    """Parse a JSON file into a python data structure"""
    with open(filename, 'r', encoding='UTF8') as file:
        py_object = json.load(file)
        return py_object
    """->load : Data stored in files
       ->loads: In-memory data
    """
