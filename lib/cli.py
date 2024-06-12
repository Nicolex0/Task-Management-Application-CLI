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