#!/usr/bin/python3
import json
"""
This file contains a function
that creates an object from a "JSON FILE"
"""

def load_from_json_file(filename):
    """
    Loads an object from json file
    Arguments:
        filename (str): The name of the output file
    Return:
        A file with a text in jason format
    """
    with open(filename, encoding='utf-8') as file:
        return (json.loads(file.read()))
