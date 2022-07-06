#!/usr/bin/python3
"""A function that reads a file """

def read_file(filename=""):
    """opens the file, reads the file and returns to the stdout"""
    with open(filename, mode="r", encoding="utf-8") as rf:
        print(rf.read(), end="")
