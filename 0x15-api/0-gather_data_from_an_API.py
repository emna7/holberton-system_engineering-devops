#!/usr/bin/python3
"""a script that returns information about an employee
"""


if __name__ == '__main__':
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com'

    employee = requests.get('{}/users/{}'.format(url, sys.argv[1]))
    employee_name = employee.json().get('name')

    tasks = requests.get('{}/todos?userId={}'.format(url, sys.argv[1]))
    task_list = tasks.json()
    total_tasks = len(task_list)
    completed_tasks = sum(1 for task in task_list if task.get('completed'))

    print('Employee {} is done with tasks({}/{}):'.format(employee_name,
                                                          completed_tasks,
                                                          total_tasks))
    for task in task_list:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))
