#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_list = sys.argv

    sum = 0
    for a in arg_list:
        if a != arg_list[0]:
            sum = sum+int(a)
    print("{}".format(sum))
