#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_list = sys.argv
    x = 0
    for a in arg_list:
        x = x + 1
    x = x - 1
    if x == 0:
        print("{} arguments.".format(x))
    elif x == 1:
        print("{} argument:\n{}: {}".format(x, x, arg_list[x]))
    elif x > 1:
        print("{} arguments:".format(x))
        c = 0
        for b in arg_list:
            if c != 0:
                print("{}: {}".format(c, b))
            c = c +1
