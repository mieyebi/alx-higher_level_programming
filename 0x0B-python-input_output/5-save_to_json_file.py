#!/usr/bin/python3
""" A function that writes an object to a text file using json"""


import json


def save_to_json_file(my_obj, filename):
    """writes a string to a textfile using json"""
    with open(filename, 'w', encoding="utf-8") as fs:
        json.dump(my_obj, fs)
