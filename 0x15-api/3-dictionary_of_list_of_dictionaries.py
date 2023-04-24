#!/usr/bin/python3
"""fetch data from a REST API"""

from json import dump
import requests


def main():
    """get and display information about all employee's todo list"""
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("{}users".format(url)).json()
    data = {}
    for user in users:
        name = user.get('username')
        id = user.get('id')
        todos = requests.get("{}users/{}/todos".format(url, id)).json()
        li = [{'username': name, 'task':
               x.get('title'), 'completed':
               x.get('completed')} for x in todos]
        data.update({id: li})
    filename = "todo_all_employees.json"
    with open(filename, 'w') as f:
        dump(data, f)


if __name__ == "__main__":
    main()
