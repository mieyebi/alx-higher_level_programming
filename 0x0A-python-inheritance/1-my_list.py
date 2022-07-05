#!/usr/bin/python3
"""describes a class that inherits frm a list"""


class Mylist(list):
    """a Mylist class that inherits from a list class"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints a list in ascending order"""
        print(sorted(self))
