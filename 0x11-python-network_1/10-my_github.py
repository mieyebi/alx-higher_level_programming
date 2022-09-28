#!/usr/bin/python3
""" A script that takes github credentials and uses the Github api to display id"""

if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.get('https://api.github.com/user',
                     auth=(argv[1], argv[2]))
    if r.status_code >= 400:
        print('None')
    else:
        print(r.json().get('id'))
