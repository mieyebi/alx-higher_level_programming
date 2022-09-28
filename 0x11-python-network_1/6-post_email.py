#!/usr/bin/python3
""" A script that takes in a url and an email address,
    sends a POST request with the email as parameter
    and displays the body of the response
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
