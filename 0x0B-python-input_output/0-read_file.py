#!/usr/bin/python3
"""Defining a function to read a file"""


def read_file(filename=""):
    """Reading and printing a file"""
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end='')
