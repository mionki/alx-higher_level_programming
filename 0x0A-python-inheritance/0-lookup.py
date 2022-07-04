#!/usr/bin/python3
"""
The lookup function to return attributes and methods of an object
"""
def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    return dir(obj)