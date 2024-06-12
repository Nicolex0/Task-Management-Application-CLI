#!/usr/bin/env python

import sys
from lib.helpers import *
from lib.models import session

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            user_management_menu()
        elif choice == "2":
            task_management_menu()
        elif choice == "3":
            task_assignment_and_filtering_menu()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. User Management")
    print("2. Task Management")
    print("3. Task Assignment and Filtering")

def user_management_menu():
    while True:
        print("\nUser Management Menu:")
        print("1. Create User")
        print("2. Delete User")
        print("3. View All Users")
        print("4. Back to Main Menu")
        choice = input("> ")
        if choice == "1":
            create_user_menu()
        elif choice == "2":
            delete_user_menu()
        elif choice == "3":
            view_all_users()
        elif choice == "4":
            return
        else:
            print("Invalid choice")

def task_management_menu():
     while True:
        print("\nTask Management Menu:")
        print("1. Create Task")
        print("2. Delete Task")
        print("3. View All Tasks")
        print("4. Back to Main Menu")
        choice = input("> ")
        if choice == "1":
            create_task_menu()
        elif choice == "2":
            delete_task_menu()
        elif choice == "3":
            view_all_tasks()
        elif choice == "4":
            return
        else:
            print("Invalid choice")

def task_assignment_and_filtering_menu():
    while True:
        print("\nTask Assignment and Filtering Menu:")
        print("1. Assign Task to User")
        print("2. Filter Tasks by Priority")
        print("3. Filter Tasks by Due Date")
        print("4. View Tasks Assigned to User")
        print("5. Back to Main Menu")
        choice = input("> ")
        if choice == "1":
            assign_task_to_user()
        elif choice == "2":
            filter_tasks_by_priority()
        elif choice == "3":
            filter_tasks_by_due_date()
        elif choice == "4":
            view_tasks_assigned_to_user()
        elif choice == "5":
            return
        else:
            print("Invalid choice")

def create_user_menu():
    print("\nCreate User:")
    username = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    user = create_user(username, email, password)
    print(f"User created successfully with ID: {user.id}")

def delete_user_menu():
    print("\nDelete User:")
    user_id = input("Enter user ID to delete: ")
    if delete_user(user_id):
        print("User deleted successfully.")
    else:
        print("User not found.")

def view_all_users():
    print("\nAll Users:")
    users = get_all_users()
    if users:
        for user in users:
            print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}")
    else:
        print("No users found.")

def create_task_menu():
    print("\nCreate Task:")
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    priority = int(input("Enter task priority (1-5): "))
    due_date = input("Enter task due date (YYYY-MM-DD): ")
    task = create_task(name, description, priority, due_date)
    print(f"Task created successfully with ID: {task.id}")

def delete_task_menu():
    print("\nDelete Task:")
    task_id = input("Enter task ID to delete: ")
    if delete_task(task_id):
        print("Task deleted successfully.")
    else:
        print("Task not found.")

def view_all_tasks():
    print("\nAll Tasks:")
    tasks = get_all_tasks()
    if tasks:
        for task in tasks:
            print(f"ID: {task.id}, Name: {task.name}, Priority: {task.priority}, Due Date: {task.due_date}")
    else:
        print("No tasks found.")

def assign_task_to_user():
    print("\nAssign Task to User:")
    task_id = input("Enter task ID to assign: ")
    user_id = input("Enter user ID to assign task to: ")
    task = get_task_by_id(task_id)
    user = get_user_by_id(user_id)
    if task and user:
        task.assigned_to = user.id
        session.commit()
        print("Task assigned successfully.")
    else:
        print("Task or user not found.")

def filter_tasks_by_priority():
    print("\nFilter Tasks by Priority:")
    priority = int(input("Enter priority level to filter tasks: "))
    tasks = session.query(Task).filter(Task.priority == priority).all()
    if tasks:
        for task in tasks:
            print(f"ID: {task.id}, Name: {task.name}, Priority: {task.priority}, Due Date: {task.due_date}")
    else:
        print("No tasks found with the specified priority.")

def filter_tasks_by_due_date():
    print("\nFilter Tasks by Due Date:")
    due_date = input("Enter due date (YYYY-MM-DD) to filter tasks: ")
    tasks = session.query(Task).filter(Task.due_date == due_date).all()
    if tasks:
        for task in tasks:
            print(f"ID: {task.id}, Name: {task.name}, Priority: {task.priority}, Due Date: {task.due_date}")
    else:
        print("No tasks found with the specified due date.")




