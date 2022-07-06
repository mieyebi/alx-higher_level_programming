#!/usr/bin/python3
"""A function that returns the dictionary description with simple data structure
    for JSON serialization of object"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    return obj.__dict__
