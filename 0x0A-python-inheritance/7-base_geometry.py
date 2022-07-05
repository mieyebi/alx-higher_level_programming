#!/usr/bin/python3
"""This is a BaseGeometry class with a method that
    raises an exception"""


class BaseGeometry:
    """A class with a public instance method that raises an exception"""

    def area(self):
        """this is a method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """this is aa mathod that validates a value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
