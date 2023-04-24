#!/usr/bin/python3
"""fetch data from a REST API"""

from json import dump
import requests
from sys import argv


def main():
    """get and display information about an employee's todo list"""
    _, id = argv
    url = "https://jsonplaceholder.typicode.com/"
    todos = requests.get("{}users/{}/todos".format(url, id)).json()
    user = requests.get("{}users/{}".format(url, id)).json()
    name = user.get('username')
    li = [{'task': x.get('title'), 'completed':
           x.get('completed'), 'username':
           name} for x in todos]
    data = {id: li}
    filename = "{}.json".format(id)
    with open(filename, 'w') as f:
        dump(data, f)


if __name__ == "__main__":
    main()
