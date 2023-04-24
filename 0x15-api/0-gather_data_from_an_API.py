#!/usr/bin/python3
"""This module contains a function that gets data from a REST API:
'https://jsonplaceholder.typicode.com/' and displays the details about the employee name and completed tasks


it accepts an integer as a parameter, which is the employee ID
"""
import requests
from sys import argv
_, id = argv


def main():
    """get employee name and information about their todo list given the
    employee id"""
    url = "https://jsonplaceholder.typicode.com/"
    todos = requests.get("{}users/{}/todos".format(url, id)).json()
    users = requests.get("{}users".format(url)).json()
    user = {}
    for item in users:
        if item['id'] == int(id):
            user.update(item)
    completed = filter(lambda x: x.get('completed'), todos)
    completed = [item for item in completed]
    text = "Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(completed), len(todos))
    print(text)
    for task in completed:
        print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    main()
