#!/usr/bin/python3
"""A function that returns an object represented by a JSON string"""


import json


def from json_string(my_str):
    """returns an json object"""
    return json.loads(my_str)
