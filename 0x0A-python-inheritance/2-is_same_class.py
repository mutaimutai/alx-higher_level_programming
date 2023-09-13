#!/usr/bin/python3
"""This is class checking function"""

def is_same_class(obj, a_class):
    """This function checks if an object is of  a certain class
    Args:
        obj (any): the object to check
        a_class (type): the class to match the type of obj to
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False
    """
    return (type(obj) is a_class)
