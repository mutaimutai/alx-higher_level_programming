#!/usr/bin/python3
"""Adds all arguments to a python list and save them to a file"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    py_list = load_from_json_file("add_item.json")
except:
    py_list = []

if __name__ == "__main__":
    py_list.extend(sys.argv[1:])
    save_to_json_file(py_list, "add_item.json")
