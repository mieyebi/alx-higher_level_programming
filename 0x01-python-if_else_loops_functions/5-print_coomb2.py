#!/usr/bin/python3
for i in range(1, 100):
    if i < 10:
        print("{0:2d}, ".format(i), end = "")
    elif i == 99:
        print("{:<2}".format(i))
    else:
        print("{:<2}, ".format(i), end="")
