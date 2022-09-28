#!/usr/bin/python3
""" A script that takes a URL, sends a request and displays
    the body of the response
"""

if __name__ == '__main__':
    from urllib.error import HTTPError
    from sys import argv
    from urllib.request import urlopen

    try:
        with urlopen(argv[1]) as response:
            print(response.read().decode("utf-8", "replace"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
