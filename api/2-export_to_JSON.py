#!/usr/bin/python3
"""Script to export user tasks to JSON file"""
from api_request import api_request
import json
import sys


if __name__ == '__main__':
    """script to get all done task of the user"""
    if len(sys.argv) > 1:
        id = sys.argv[1]

        # User Recovery
        user = api_request(f"users/{id}")
        if len(user) > 0:

            # User task retrievals
            todos = api_request(f"todos", {"userId": id})
            if len(todos) > 0:

                # Create from requested userId: []
                callback = {}
                callback[id] = []

                # We browse data by data to add in the table
                for todo in todos:
                    callback[id].append({
                        "task": todo['title'],
                        "completed": todo['completed'],
                        "username": user['username']
                    })

                # Sending data to a .json file
                with open("{}.json".format(id), 'w') as csvfile:
                    csvfile.write(json.dumps(callback))
                    csvfile.close()
