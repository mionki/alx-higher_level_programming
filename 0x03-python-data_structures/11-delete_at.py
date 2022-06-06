#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """a function that deletes an item a specific position"""
    if my_list:
        if 0 <= idx < len(my_list):
            del my_list[idx]
    return my_list