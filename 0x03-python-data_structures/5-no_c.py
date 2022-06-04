#!/usr/bin/python3

def no_c(my_string):
    a = ""
    for b in my_string:
        if b != 'c' and b != 'C':
            a += b
    return (a)
