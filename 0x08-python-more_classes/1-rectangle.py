#!/usr/bin/python3
"""Define a Class of a rectangle"""

class Rectangle:
    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height
    """Getter for width attribute"""    
    @property
    def width(self):
        return self.__width
    """setter for the private instance attribute width"""
    @width.setter
    def width(self,value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    """Getter for thePrivate instance attribute height"""
    @property
    def height(self):
        return self.__height
    """Setter for the private instance"""
    @height.setter
    def height(self,value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0") 
        else:
            self.__height =  value  








        


            

