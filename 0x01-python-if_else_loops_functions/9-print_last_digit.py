#!/usr/bin/python3

def print_last_digit(number):
    if number < 10 and number >= 0:
        a = number
        print("{}".format(a), end = "")
    elif (number > 10 or number < -10) and (number < 100 or number > -100):
        a = number % 10
        print("{}".format(a), end = "")
    elif (number >= 100 or number <= -100) and (number < 1000 or nnumber >-1000):
        a = number % 100
        print("{}".format(a), end = "")
    elif (number >= 1000 or number <= -1000) and (number < 10000 or number >= 10000):
         a = number % 1000
         print("{}".format(a), end = "")
    return(a)
