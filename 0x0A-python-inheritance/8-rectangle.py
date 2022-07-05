#!/usr/bin/python3
"""a subclass that inherits frm a class BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """a subclass Rectangle from a base class"""
    def __init__(self, width = "", height = ""):
        """instantiation with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
