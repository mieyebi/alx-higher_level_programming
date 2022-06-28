#!/usr/bin/python3
""" a function that prints a text with 2 lines after .?:"""


def text_indentation(text):
    """defines the attributes of the texts"""

    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(text):
        if i == '.':
            print(i)
            print("\n")
        elif i == '?':
            print(i)
            print("\n")
        elif i == ':':
            print(i)
            print("\n")
        else:
            print(i, end="")
