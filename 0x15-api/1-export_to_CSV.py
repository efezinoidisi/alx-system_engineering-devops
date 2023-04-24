#!/usr/bin/python3
"""fetch data from a REST API"""

import csv
import requests
from sys import argv


def main():
    """get and display information about an employee's todo list"""
    _, id = argv
    url = "https://jsonplaceholder.typicode.com/"
    todos = requests.get("{}users/{}/todos".format(url, id)).json()
    user = requests.get("{}users/{}".format(url, id)).json()
    name = user.get('username')
    for task in todos:
        status = task.get('completed')
        title = task.get('title')
        filename = "{}.csv".format(id)
        text = "{},{},{},{}".format(id, name, status, title)
        with open(filename, 'a') as f:
            textwriter = csv.writer(f, delimiter=",",quotechar='"', quoting=csv.QUOTE_ALL)
            textwriter.writerow([id,name,status,title])


if __name__ == "__main__":
    main()
