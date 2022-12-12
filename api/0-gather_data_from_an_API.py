#!/usr/bin/python3
""" module use urllib or requests api """

from requests import get
from sys import argv


if __name__ == "__main__":

    url_todos = get('https://jsonplaceholder.typicode.com/todos/')
    url_second = get('https://jsonplaceholder.typicode.com/users/')
    response_todos = url_todos.json()
    response_user = url_second.json()
    completed = 0
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = []

    for num in response_todos:
        if num.get('userId') == int(argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1

            if num.get('completed') is True:
                completed += 1
                NUMBER_OF_DONE_TASKS.append(num.get('title'))

    for num in response_user:
        if num.get('id') == int(argv[1]):
            employee = num.get('name')

    print("Employee {} is done with tasks({}/{}):".format(
        employee, completed, TOTAL_NUMBER_OF_TASKS))

    for NUMBER_OF_DONE_TASKS in NUMBER_OF_DONE_TASKS:
        print("\t {}".format(NUMBER_OF_DONE_TASKS))