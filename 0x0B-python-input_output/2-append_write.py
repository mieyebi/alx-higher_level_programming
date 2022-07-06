#!/usr/bin/python3
"""A function that appends string at the end of a
    textfile and return the number of characters added"""


def append_write(filename="", text=""):
    """appends a string at the end of a textfile"""
    with open(filename, mode="a", encoding="utf-8") as fa:
        a = fa.write(text)
        return a
