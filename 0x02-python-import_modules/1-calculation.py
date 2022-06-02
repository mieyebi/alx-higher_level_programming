#!/usr/bin/python3
from calculator_1 import sub, add, mul, div

a = 10
b = 5
su = sub(a, b)
ad = add(a, b)
mu = mul(a, b)
di = div(a, b)

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, ad))
    print("{} - {} = {}".format(a, b, su))
    print("{} * {} = {}".format(a, b, mu))
    print("{} / {} = {}".format(a, b, di))
