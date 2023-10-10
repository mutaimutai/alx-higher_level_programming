#!/usr/bin/python3
def read_file(filename=""):
    """A function that reads a textfile and prints it out"""
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end='')

