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

    # Calculate todo list progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Display progress info
    print(f"Employee {user_data['name']} is done with tasks"
          f"({completed_tasks}/{total_tasks}):")

    # Display and export completed tasks to CSV
    csv_file_name = f"{employee_id}.csv"
    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        for todo in todos_data:
            if todo['completed']:
                csv_writer.writerow([
                    user_data['id'], user_data['username'],
                    str(todo['completed']), todo['title']])
                print(f"\t {todo['title']}")

    print(f"\nData exported to {csv_file_name}")
