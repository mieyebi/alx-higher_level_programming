#!/usr/bin/python3
""" A function that creates an object from a JSON file """

import json


def load_from_json_file(filename):
    """creates an object from a json file"""
    with open(filename, 'r', encoding="utf-8") as fj:
        return json.load(fj)
