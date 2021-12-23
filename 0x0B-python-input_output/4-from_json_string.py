#!/usr/bin/python3

"""
This function file that returns 
an object represnted by a json
string
"""

import json

def from_json_string(my_str):
    """
     return object by json string
    
    """
    return (json.loads(my_str))
