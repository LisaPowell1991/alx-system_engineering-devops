#!/usr/bin/python3

"""
Using this REST API(https://jsonplaceholder.typicode.com),
for a given employee ID, returns information about
his/her TODO list progress and exports it to a CSV file.
"""
from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_id = int(argv[1])

    # User details
    user_response = get(f"{base_url}/users/{employee_id}")
    user_data = user_response.json()

    # User's todos
    todos_response = get(f"{base_url}/todos?userId={employee_id}")
    todos_data = todos_response.json()

    # Create CSV file
    csv_file_name = f"{employee_id}.csv"
    with open(csv_file_name, mode='w', newline='') as csv_file:
        header = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(
                csv_file, fieldnames=header, quoting=csv.QUOTE_ALL)

        # Write todo data to CSV
        todo_list = []
        for todo in todos_data:
            todo_dict = {}
            todo_dict.update({
                "USER_ID": employee_id,
                "USERNAME": user_data['username'],
                "TASK_COMPLETED_STATUS": str(todo['completed']),
                "TASK_TITLE": todo['title']
            })
            todo_list.append(todo_dict)
        writer.writerows(todo_list)
