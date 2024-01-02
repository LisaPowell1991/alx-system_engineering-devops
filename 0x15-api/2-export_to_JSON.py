#!/usr/bin/python3

"""
Using this REST API(https://jsonplaceholder.typicode.com),
for a given employee ID, returns information about
his/her TODO list progress and exports to JSON.
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

    # Create a dictionary to store the required info
    user_tasks = {str(employee_id): [
        {"task": todo['title'], "completed": todo['completed'],
            "username": user_data['username']} for todo in todos_data]}

    # Write data to a JSON file
    json_file_name = f"{employee_id}.json"
    with open(json_file_name, 'w') as json_file:
        json.dump(user_tasks, json_file, indent=2)
