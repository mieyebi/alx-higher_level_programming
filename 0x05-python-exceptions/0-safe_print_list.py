#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    idx = 0
    for a in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            idx += 1
        except (ValueError, TypeError):
            pass
        except IndexError:
            break
    print()
    return idx
