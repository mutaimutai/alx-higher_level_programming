#!/usr/bin/python3
"""appending into a file"""


def append_write(filename="", text=""):
    """This function appends into a file"""
    with open(filename, "a", encoding='UTF-8') as f:
        num = f.write(text)
        return num
