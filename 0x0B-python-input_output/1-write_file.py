#!/usr/bin/python3
"""Afunction that writes a text to a file"""


def write_file(filename="", text=""):
    """Writes text into a file"""
    with open(filename, 'w', encoding="UTF8") as file:
        texts = file.write(text)
        return texts
