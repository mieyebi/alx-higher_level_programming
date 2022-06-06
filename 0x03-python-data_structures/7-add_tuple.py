#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    a = len(tuple_a) - 1
    b = len(tuple_b) - 1

    if a < 0:
        tuple_a = 0, 0
    elif a == 0:
       tuple_a = tuple_a[0], 0
    elif a >= 1:
        tuple_a = tuple_a[0], tuple_a[1]
    if b < 0:
        tuple_b = 0, 0
    elif b == 0:
        tuple_b = tuple_b[0], 0
    elif b >= 1:
       tuple_b = tuple_b[0], tuple_b[1]

    x = tuple_a[0] + tuple_b[0]
    y = tuple_a[1] + tuple_b[1]
    return (x, y)
