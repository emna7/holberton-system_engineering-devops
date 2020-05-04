#!/usr/bin/python3
"""task 0, extended to export data in the JSON format.
"""


if __name__ == '__main__':
    import json
    import requests

    url = 'https://jsonplaceholder.typicode.com'

    employee = requests.get('{}/users'.format(url))
    user_list = employee.json()

    task_list = []

    for user in user_list:
        tasks = requests.get('{}/todos?userId={}'.format(url, user.get('id')))
        task_list += tasks.json()

    json_dict = {user.get('id'): [{"task": task.get('title'),
                                   "completed": task.get('completed'),
                                   "username": user.get('username')}
                                  for task in task_list
                                  if user.get('id') == task.get('userId')]
                 for user in user_list}

    with open('todo_all_employees.json', 'w') as fp:
        json.dump(json_dict, fp)
