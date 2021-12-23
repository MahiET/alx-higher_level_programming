#!/usr/bin/python3
import json
"""
This file function that writes
object to text file json rep
"""

def save_to_json_file(my_obj, filename):
    """
     function that writes to text file
    """
    with open(filename, mode="w") as myFile:
        json.dump(my_obj, myFile)
