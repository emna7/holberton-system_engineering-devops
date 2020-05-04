#!/usr/bin/python3
"""Returns information about an employee
Exports data in JSON format
"""


if __name__ == '__main__':
    import json
    import requests
    import sys

    url = 'https://jsonplaceholder.typicode.com'

    user_id = sys.argv[1]

    employee = requests.get('{}/users/{}'.format(url, user_id))
    username = employee.json().get('username')

    tasks = requests.get('{}/todos?userId={}'.format(url, user_id))
    task_list = tasks.json()

    json_dict = {user_id: [{"task": task.get('title'),
                            "completed": task.get('completed'),
                            "username": username}
                           for task in task_list]}

    with open('{}.json'.format(user_id), 'w') as fp:
        json.dump(json_dict, fp)
