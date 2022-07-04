#!/usr/bin/python3

"""A function that checks the clas of a function"""

def is_same_class(obj,a_class):
    """checks if an object is an instance of a given class
    return or true
    else false
    """
    if type(obj) == a_class:
        return True
    return False
     
