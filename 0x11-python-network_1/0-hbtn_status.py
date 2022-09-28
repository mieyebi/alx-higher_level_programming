#!/usr/bin/python3
""" A script that fetches a url"""


if __name__ == '__main__':
    from urllib.request import urlopen


    with urlopen('https://alx_intranet.hbtn.io/status') as response:
        html = response.read()
        utf8 = html.decode('utf-8', "strict")
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html, utf8, end=""))
