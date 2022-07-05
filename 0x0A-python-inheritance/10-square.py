#!/usr/bin/python3

"""A class Square that inherits from Rectangle (9-rectangle.py)"""

Rectangle = __import__('9-rectangle').Rectangle

class square(Rectangle):
    """A class representation of a square"""

    def __init__(self, size):
        """instantiation of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns the area size of the square"""
        return self.__size ** 2


