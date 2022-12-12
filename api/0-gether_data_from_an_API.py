#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':
    url_todos = get('https://jsonplaceholder.typicode.com/todos/')
    url_users = get('https://jsonplaceholder.typicode.com/users/')
    response_todos = url_todos.json()
    response_users = url_users.json()
    completed = 0
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = []

    for num in response_todos:
        if num.get('userId') == int(argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1

            if num.get('completed') is True:
                completed += 1
                NUMBER_OF_DONE_TASKS.append(num.get('title'))
    
    for num in url_users:
        if num.get('id') == int(argv[1]):
            empoyee = num.get('name')
    
    print("Employee {} is done with tasks({}/{}):".format(
        empoyee, completed, TOTAL_NUMBER_OF_TASKS))
    
    for NUMBER_OF_DONE_TASKS in NUMBER_OF_DONE_TASKS:
        print("\t {}".format(NUMBER_OF_DONE_TASKS))