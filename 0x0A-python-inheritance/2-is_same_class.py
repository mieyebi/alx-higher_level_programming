#!/usr/bin/python3
"""A function that returns true or false on if an object is
   exactly an instance of specified class or otherwise"""


def is_same_class(obj, a_class):
    """checks if objects are exact instance of the specified class"""
    if type(obj) == a_class:
        return True
    else:
        return False
