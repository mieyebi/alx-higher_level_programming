#!/usr/bin/python3

def magic_calculation(a, b):
    mag = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception("Too far")
            mag += (a ** b) / x
        except Exception:
            mag = b + a
            break
    return mag
