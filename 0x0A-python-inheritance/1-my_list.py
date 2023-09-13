#!/usr/bin/python3
"""class that inherits from a list class"""


class MyList(list):
    """Imlement sorted printing for the builtin list class"""

    def print_sorted(self):
        """returns a list in sorted order"""
        print(sorted(self))
