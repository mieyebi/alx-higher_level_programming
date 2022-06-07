#!/usr/bin/python3

def max_integer(my_list=[]):
    a = len(my_list) - 1
    b = my_list[0]
    c = 0
    while c <= a:
        if b < my_list[c]:
            b = my_list[c]
        c += 1
    return b

