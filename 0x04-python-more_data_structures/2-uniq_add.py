#!/usr/bin/python3
def uniq_add(my_list=[]):

    uniq = set(my_list)
    a = 0

    for i in uniq:
        a += i
    return (a)
