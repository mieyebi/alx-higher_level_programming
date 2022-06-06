#!/usr/bin/python3

def max_integer(my_list=[]):
    a = len(my_list) - 1
    b = 0
    for c in my_list:
        if my_list[b] > c:
            d = my_list[b]
            my_list[0] = my_list[b]
            b += 1
    return d

