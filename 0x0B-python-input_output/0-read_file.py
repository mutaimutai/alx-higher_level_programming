#!/usr/bin/python3
"""Defining a function that prints a file"""
def read_file(filename=""):
    """A function that reads a textfile and prints it out
    Args:
        filename : the name of the file to be read
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read())

