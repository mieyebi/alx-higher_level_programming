#!/usr/bin/python3
"""a function that returns true or false of an object
   is an instance of, or if the object is an instance of
    a class that inherited from a specified class"""


def is_kind_of_class(obj, a_class):
    """defines true or false for an object of instance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
