#!/usr/bin/python3
"""a function that adds two integers"""


import math
def add_integer(a, b=98):
    """defines the function that adds integers"""

    while a and b:
        if a != int:
            if a == float:
                a = (int)a
            else:
                raise TypeError("a must be an integer")
        if b != int:
            if b == float:
                b = (int)b
            else:
                raise TypeError("b must be an integer")

        sum = a + b
    return sum
