#!/usr/bin/python3
""" A script that takes in a URL and an email
    sends a post request and displays the body of the response
"""
from sys import argv
from urllib.request import urlopen, Request
from urllib.parse import urlencode


def post_email():
    """ defines the function of the script """
    url = argv[1]
    email = {'email': argv[2]}

    data = urlencode(email).encode('utf-8')
    req = Request(url, data)
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == '__main__':
    post_email()
