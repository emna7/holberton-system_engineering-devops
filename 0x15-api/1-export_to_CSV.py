#!/usr/bin/python3
"""Returns information about an employee
Exports data in CSV format
"""


if __name__ == '__main__':
    import csv
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com'

    user_id = sys.argv[1]

    employee = requests.get('{}/users/{}'.format(url, user_id))
    username = employee.json().get('username')

    tasks = requests.get('{}/todos?userId={}'.format(url, user_id))
    task_list = tasks.json()

    row_list = [[user_id,
                 username,
                 task.get('completed'),
                 task.get('title')]
                for task in task_list]

    with open('{}.csv'.format(user_id), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(row_list)
