#!/usr/bin/python3

"""
This file contains a function that
writes an obj to a text file using
JSON rep
"""

def save_to_json_file(my_obj, filename):
    from json import dumps
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(dumps(my_obj))
        f.close()

