#!/usr/bin/python3
""" A script that fetches a url"""
from urllib.request import urlopen

def hbtn_status_0():
    """ A function that shows """
    with urlopen('https://alx_intranet.hbtn.io/status') as response:
        html = response.read()
        utf8 = html.decode('utf-8')
        print("Body response:\n\t- type: {}".format(type(html)))
        print("\t- content: {}\n\t- utf8 content: {}".
            format(html, ytf8, end=""))


if __name__ == '__main__':
    hbtn_status_0()

