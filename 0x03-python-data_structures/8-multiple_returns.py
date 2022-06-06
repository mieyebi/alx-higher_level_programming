#!/usr/bin/python3

def multiple_returns(sentence):
    a = len(sentence)
    b = sentence[0]
    if sentence == "":
        b = None
    return (a, b)
