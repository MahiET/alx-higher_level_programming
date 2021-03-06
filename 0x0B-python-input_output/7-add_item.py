#!/usr/bin/python3

"""
This file contains a function that adds
all arguments to a python list and saves
to a file
"""
import json
from sys import argv

save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        lst = load_from_json("add_item.json")
    except:
        pass
        lst = []
    for av in argv[1:]:
        lst.append(av)
    save_to_json(lst, "add_item.json")
