#!/usr/bin/python3
"""a function that returns a list of available attributes and methods of an object"""


def lookup(obj):
    """returns an obj list"""
    return dir(obj)
