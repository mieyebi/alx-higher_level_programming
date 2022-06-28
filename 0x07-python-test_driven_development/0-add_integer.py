#!/usr/bin/python3
"""a function that adds two integers"""


def add_integer(a, b=98):
    """defines the function that adds integers"""

    if a is not isinstance(a,int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if b is not isinstance(a,int) and not isinstance(a, float):
        raise TypeError("b must be an integer")

    sum = (int)a + (int)b
    return sum
