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

    # CSV file name
    csv_filename = f"{employee_id}.csv"

    # Write data to CSV file
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)

        # Write todo data
        rows = [[str(user_data['id']),
                user_data['name'], str(todo['completed']),
                todo['title']] for todo in todos_data]
        csv_writer.writerows(rows)

    # Display progress info
    print(f"Employee {user_data['name']} tasks exported to {csv_filename}.")
