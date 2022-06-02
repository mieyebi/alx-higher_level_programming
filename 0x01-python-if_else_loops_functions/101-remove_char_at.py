#!/usr/bin/python3

def remove_char_at(str, n):
    for a in str:
        if a == str[n]:
            a = ""
        print(f"{a}", end="")
