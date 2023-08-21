#!/usr/bin/python3
"""program that copeis all tasks in a json file"""
import json
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
        username = name_response["username"]

    if todos_request.status_code == 200:
        todos_response = todos_request.json()
        user_data = {}
        for task in todos_response:
            task_data = {
                "task": task["title"],
                "completed": task["completed"],
                "username": username
            }
            if user_id in user_data:
                user_data[user_id].append(task_data)
            else:
                user_data[user_id] = [task_data]
    json_data = json.dumps(user_data)
    json_filename = f"{user_id}.json"

    with open(json_filename, "w") as json_file:
        json.dump(user_data, json_file)
