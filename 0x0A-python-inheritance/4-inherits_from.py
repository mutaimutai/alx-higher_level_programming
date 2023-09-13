#!/usr/bin/python3
"""writng a function that checks if the object is an instance of a class"""

def inherits_from(obj, a_class):
    """Function that checks of it was inherited
    Args:
        obj:the object to be checked
        a_class:the class itself
    Returns:
        True if it was inherited else false
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
