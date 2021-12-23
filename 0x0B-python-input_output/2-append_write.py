#!/usr/bin/python3
"""
This function that appends file
a string at the end of a text file and
returns number of characters 
"""

def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as myFile:
        return (myFile.write(str(text)))
