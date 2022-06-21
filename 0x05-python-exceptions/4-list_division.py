#!/usr/bin/python3

def safe_division(a, b):
    div = 0
    try:
        div = a / b
    except ZeroDivisionError:
        print("division by 0")
    except TypeError:
        print("wrong type")
    finally:
        return div


def list_division(my_list_1, my_list_2, list_length):
    divresult = []
    for i in range(list_length):
        try:
            divresult.append(safe_division(my_list_1[i], my_list_2[i]))
        except IndexError:
            print("out of range")
            divresult.append(0)

    return divresult
