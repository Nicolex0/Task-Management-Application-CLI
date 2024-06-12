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
    pass
