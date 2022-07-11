#!/usr/bin/python3
"""A class Base with a folder named models"""
import json


class Base:
    """A class base with class attributes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the class base"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
