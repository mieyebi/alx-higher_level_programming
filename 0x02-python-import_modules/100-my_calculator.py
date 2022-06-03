#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import mul, add, sub, div
    args = sys.argv

    x = 0
    for a in args:
        x = x + 1
    x = x - 1

    if x < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit (1)
    if (args[2] != '+' and args[2] != '-' and args[2] != '*' and args[2] != '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit (1)

    a = int(args[1])
    b = int(args[3])
    if args[2] == '+':
        c = add(a, b)
        print("{} + {} = {}".format(a, b, c))
    elif args[2] == '-':
        c = sub(a, b)
        print("{} - {} = {}".format(a, b, c))
    elif args[2] == '*':
        c = mul(a, b)
        print("{} * {} = {}".format(a, b, c))
    elif args[2] == '/':
        c = div(a, b)
        print("{} / {} = {}".format(a, b, c))
