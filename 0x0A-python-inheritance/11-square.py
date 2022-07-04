#!/usr/bin/python3
"""A class square that inherits from Rectangle ("10-square.py"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """A representation of a sqaure"""
    def __init__(self,size):
        """instantiation of square"""
        self.integer_validator("size",size)
        self.__size = size
        super().__init__(size,size)

    def area(self):
        """returns area of a square"""
        return self.__size ** 2

    def __str__(self):
        """string representation of a square"""
        return "[Square] {:d}/{:d}".format(self.__size,self.size)
