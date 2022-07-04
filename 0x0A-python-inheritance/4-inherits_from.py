#!/usr/bin/python3
""" A function that returns a function if the object is an instance of a class that inherited from the specified class"""

def inherits_from(obj, a_class):
    """
    checks if an object is an inherited instance of a class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False