#!/usr/bin/python3
"""A square module that initializes a class"""


class Square:
    """This class defines the object size"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
