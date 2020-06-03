#!/usr/bin/python3
import requests
import json
import sys
users='https://jsonplaceholder.typicode.com/users'
usr=requests.get(users)
for i in usr.json():
    for key,value in i.items():
        if key=='id' and value==int(sys.argv[1]):
            name=i['name']
            print('Employee {} is done with tasks'.format(name), end="")
j=0
k=0
todos='https://jsonplaceholder.typicode.com/todos'
todo=requests.get(todos)
for i in todo.json():
    for key,value in i.items():
        if key=='userId' and value==int(sys.argv[1]):
            if i['title'] is not None:
                k+=1
            if i['completed']==True:
                j+=1
print ('({}/{}):'.format(j,k))
for i in todo.json():
    for key,value in i.items():
        if key=='userId' and value==int(sys.argv[1]):
            if i['completed']==True:
                print('\t{}'.format(i['title']))
