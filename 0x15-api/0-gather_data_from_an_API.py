#!/usr/bin/python3

"""
Using this REST API(https://jsonplaceholder.typicode.com),
for a given employee ID, returns information about
his/her TODO list progress.
"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Get and display info about an employee's
    TODO list progress.

    Parameters:
    - employee_id (int): The ID of the employee
    whose progress needs to be checked.
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # User details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    # User todo
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    # Calculate todo list progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Display progress info
    print(f"Employee {user_data['name']} is done with tasks "
          f"({completed_tasks}/{total_tasks}):")
    print(f"{user_data['name']}:", end=" ")

    if total_tasks > 0:
        print(f"{completed_tasks}/{total_tasks}")
    else:
        print("No tasks found.")

    # Display completed tasks titles
    for todo in todos_data:
        if todo['completed']:
            print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
