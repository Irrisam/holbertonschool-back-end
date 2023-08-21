#!/usr/bin/python3

import json
import requests

base_url = "https://jsonplaceholder.typicode.com"

users_request = requests.get(f"{base_url}/users")
if users_request.status_code == 200:
    users_data = users_request.json()


user_tasks = {}

for user in users_data:
    user_id = user["id"]

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

    user_tasks[user_id] = tasks

with open("todo_all_employees.json", "w") as json_file:
    json.dump(user_tasks, json_file)
