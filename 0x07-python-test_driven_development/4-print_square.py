#!/usr/bin/python3
""" a function that prints a square with the character #"""

def print_square(size):
    """defines the square by its attributes"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    elif size < 0 and type(size) is float:
        raise TypeError("size must be an integer")
    else:
        print(("#" * size + "\n") * size, end="")
