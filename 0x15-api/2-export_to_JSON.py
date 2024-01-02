#!/usr/bin/python3

"""
Using this REST API(https://jsonplaceholder.typicode.com),
for a given employee ID, returns information about
his/her TODO list progress.
"""
from requests import get
from sys import argv
import json

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_id = int(argv[1])

    # User details
    user_response = get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    # User's todos
    todos_response = get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    # Create a list to store task info
    tasks_info = []

    # Populate the tasks_info list with tasks details
    for todo in todos_data:
        task_info = {
            "task": todo['title'],
            "completed": todo['completed'],
            "username": user_data['name']
        }
        tasks_info.append(task_info)

    # Create a dictionary with the required structure
    result_data = {str(employee_id): tasks_info}

    # Dump the data into a JSON file
    json_file_name = f"{employee_id}.json"
    with open(json_file_name, 'w') as json_file:
        json.dump(result_data, json_file, indent=2)
