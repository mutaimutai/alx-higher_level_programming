#!/usr/bin/python3
"""writing  a function that check if an oject is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """This function takes 2 arguments
    Args:
        obj(any): the object to be checked for
        a_class :the class
    returns:
         returns True if the object is an instanceelse false
    """
    return isinstance(obj, a_class)
