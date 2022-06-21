#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    dlist = 0
    for a in range(0, x):
        try:
            print("{:d}".format(my_list[a]), end="")
            dlist += 1
        except TypeError:
            pass
        except ValueError:
            pass
    print()
    return dlist
