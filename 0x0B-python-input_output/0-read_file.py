#!/usr/bin/python3
def read_file(filename=""):
    """This is a function that reads content froma file"""
    with open(filename, encoding="UTF-8") as f:
        for line in f:
            print(line, end='')
