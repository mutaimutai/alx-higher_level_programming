#!/usr/bin/python3
"""Defining a function that appends a text to file"""


def append_write(filename="", text=""):
    """Appends a text to a file"""
    with open(filename, 'a', encoding='UTF8') as file:
        texts = file.write(text)
        return texts
