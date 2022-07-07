#!/usr/bin/python3
"""a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """writes to a file and returns len of characters"""
    with open(filename, mode="w", encoding="utf-8") as fw:
        a = fw.write(text)
        return a
