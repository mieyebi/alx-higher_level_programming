#!/usr/bin/python3
"""a function that adds two integers"""


def add_integer(a, b=98):
    """defines the function that adds integers"""

    sum = 0
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    sum = int(a) + int(b)
    return sum
