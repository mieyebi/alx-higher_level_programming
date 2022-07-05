#!/usr/bin/python3
"""a subclass that inherits frm a class BaseGeometry"""


class BaseGeometry:
    """A class with a public instance method that raises an exception"""

    def area(self):
        """this is a method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this is a mathod that validates a value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """a subclass Rectangle from a base class"""
    def __init__(self, width, height):
        """instantiation with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
