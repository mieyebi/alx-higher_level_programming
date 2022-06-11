#!/usr/bin/python3

def best_score(a_dictionary):

    dlist = []
    if a_dictionary:
        for a in a_dictionary.items():
            dlist.append(item[1])
        dlist = sorted(dlsit, reverse=True)
        best = dlist[0]
        for key, best_val in a_dictionary.items():
            if best_val == best:
                return key
