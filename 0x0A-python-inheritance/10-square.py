#!/usr/bin/python3
"""a subclass that inherits frm a class BaseGeometry"""



BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a subclass Rectangle from a base class"""
    def __init__(self, width, height):
        """instantiation with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """A subclass square of class rectangle"""
    def __init__(self, size):
        """instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size

     def area(self):
        """returns the area of the square"""
        return self.__size * self.__size
