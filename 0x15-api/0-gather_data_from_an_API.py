#!/usr/bin/python3
"""
api task
"""
import  urllib, requests
import sys

if __name__ == "__main__":
        url = "https://jsonplaceholder.typicode.com/"
        id = sys.argv[1]

        response_user = requests.get(f"{url}/users/{id}")
        response_todos = requests.get(f"{url}/todos?userId={id}")

        response_user = response_user.json()
        response_todos = response_todos.json()

        user_name = response_user.get("name")

        tasks_name = []


        for task in response_todos:
                if task.get("completed"):
                        tasks_name.append(task.get("title"))

        c_todos = len(response_todos)
        c_done = len(tasks_name)

        print(f"Employee {user_name} is done with tasks({c_done}/{c_todos})")
        for name in tasks_name:
                print(f"\t{name}")


