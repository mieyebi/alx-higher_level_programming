#!/usr/bin/python3
if __name__ =="__main__":
    import hidden_4
    for a in dir(hidden_4):
        if (a[0] and a[1]) != '_':
            print("{}".format(ord(a)))
