#!/usr/bin/python3
""" A script that tkaes a URL, sends a request
    and displays the value of X-Request-Id
"""

if __name__ == '__main__':
    from urllib.request import urlopen
    from sys import argv

    with urlopen(argv[1]) as response:
        head = response.headers.get('X-Request-Id')
        print(head)
