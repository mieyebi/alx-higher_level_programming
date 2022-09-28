#!/usr/bin/python3
""" A script that takes a letter and sends a POST request to a url"""


if __name__ == '__main__':
    import requests
    from sys import argv

    q = argv[1] if len(argv) > 1 else ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        dic = r.json()
        if dic == {}:
            print('No result')
        else:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
    except ValueError:
        print('Not a valid JSON')
