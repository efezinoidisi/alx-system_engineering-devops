#!/usr/bin/python3
"""
This module contains a function that gets data from a REST API:
'https://jsonplaceholder.typicode.com/'
"""
from sys import argv
import requests
_, id = argv

def main():
    """
    get employee name and information about their todo list given the employee id
    """
    url = "https://jsonplaceholder.typicode.com/"
    todos = requests.get("{}users/{}/todos".format(url, id)).json()
    users = requests.get("{}users".format(url)).json()
    user = {}
    for item in users:
        if item['id'] == int(id):
            user.update(item)
    completed = filter(lambda x: x['completed'] == True, todos)
    completed = [item for item in completed]
    text = "Employee {} is done with tasks({}/{}):".format(user.get('name'), len(completed), len(todos))
    print(text)
    for task in completed:
        print("\t {}".format(task.get('title')))

if __name__=="__main__":
    main()
