#!/usr/bin/python3

"""
Using this REST API(https://jsonplaceholder.typicode.com),
for a given employee ID, returns information about
his/her TODO list progress.
"""
import json
from requests import get
from sys import argv

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_id = int(argv[1])

    # Create a dictionary to store tasks for each user
    all_tasks = {}

    # User details
    user_response = get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    # User's todos
    todos_response = get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    # Calculate todo list progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Create a list to store tasks for the current user
    user_tasks = []

    # Populate user_tasks list with task details
    for todo in todos_data:
        task_details = {
            "username": user_data['username'],
            "task": todo['title'],
            "completed": todo['completed']
        }
        user_tasks.append(task_details)

    # Add user_tasks list to the all_tasks dictionary with the key as USER_ID
    all_tasks[str(employee_id)] = user_tasks

    # Write the all_tasks dictionary to a JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file, indent=2)

    # Display progress info
    print(f"Employee {user_data['name']} is done with tasks"
          f"({completed_tasks}/{total_tasks}):")

    # Display completed tasks titles
    for todo in todos_data:
        if todo['completed']:
            print(f"\t {todo['title']}")
