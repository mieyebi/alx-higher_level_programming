#!/usr/bin/python3
"""This is a BaseGeometry class with a method that
    raises an exception"""



class BaseGeometry:
    """A class with a public instance method that raises an exception"""
    def area(self):
        """this is a method that raises an exception"""
        raise Exception("area() is not implemented")
