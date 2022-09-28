#!/usr/bin/python3
""" A script that takes a url, sends a request and displays the response"""


if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
