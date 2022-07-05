#!/usr/bin/python3
''' A function that returns true or false if the object is an instance of class
    that inherited from a specified class'''


def inherits_from(obj, a_class):
    """defines if the object is an instance of the class or is inherited from a specified class"""
    if issubclass (type(obj), a_class):
        if type(obj) == a_class:
            return True
        else:
            return False
    else:
        return False
