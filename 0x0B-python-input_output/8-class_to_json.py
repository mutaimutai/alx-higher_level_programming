#!/usr/bin/python3
"""Function that returns the dict description
for JSON serialization of an object
"""
import json


def class_to_json(obj):
    """Returns the JSON rep of a simple data structure"""
    return (obj.__dict__)
