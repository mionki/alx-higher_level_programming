#!/usr/bin/python3
"""a function that returns True if the object is an instance or an object of that has inhereited from specified class"""

def is_kind_of_class(obj, a_class):
    """
   Checks if an object is an object of a class or has inherited instance of a class 
    """
    if isinstance(obj, a_class):
        return True
    return False
