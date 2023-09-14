#!/usr/bin/python3
"""Writing into a file"""


def write_file(filename="", text=""):
    """This function writes into a file"""
    with open(filename, "w", encoding='UTF-8') as f:
        num = f.write(text)
    return num
