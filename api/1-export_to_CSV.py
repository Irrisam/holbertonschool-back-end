#!/usr/bin/python3
"""program that uses a fake api to retreive data."""

import csv
import requests
import sys

if len(sys.argv) > 1:
    user_id = sys.argv[1]

    url_name = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    name_request = requests.get(url_name)
    todos_request = requests.get(url_todos)

    if name_request.status_code == 200:
        name_response = name_request.json()
        name = name_response["username"]

    if todos_request.status_code == 200:
        todos_response = todos_request.json()
        completed = []
        uncompleted = []
        for task in todos_response:
            if task['completed']:
                completed.append(task)
            else:
                uncompleted.append(task)
        todos_total = (len(completed) + len(uncompleted))

    output = "Employee {} is done with tasks({}/{}):".format(
        name, len(completed), todos_total)
    csv_list = []
    for task in todos_response:
        task_title = str(task["completed"])
        csv_list.append([user_id, name, task_title, task["title"]])

    file_name = f"{user_id}.csv"

    with open(file_name, mode="w", newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)

        writer.writerows(csv_list)

else:
    print("usage: command userid")
