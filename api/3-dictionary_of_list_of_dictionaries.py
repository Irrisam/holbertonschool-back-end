#!/usr/bin/python3
"""stores every task of every person in a json file"""

import json
import requests

base_url = "https://jsonplaceholder.typicode.com"

users_request = requests.get(f"{base_url}/users")
if users_request.status_code == 200:
    users_data = users_request.json()

user_tasks = {}

for user in users_data:
    user_id = user["id"]
    username = user["username"]

    todos_request = requests.get(f"{base_url}/todos?userId={user_id}")
    if todos_request.status_code == 200:
        todos_data = todos_request.json()

    tasks = []

    for task in todos_data:
        task_data = {
            "task": task["title"],
            "completed": task["completed"],
        }
        tasks.append(task_data)

    user_tasks[username] = tasks

with open("user_tasks.json", "w") as json_file:
    json.dump(user_tasks, json_file)
