# TASK MANAGEMENT APPLICATION CLI

## Introduction

Welcome to the Task Manager Application, a Python-based command-line interface (CLI) tool designed to streamline organizational task management.
This application enables users to add, remove, and assign tasks to various users, while users can view their assigned tasks, find tasks by priority and due date, and list all tasks.
Our goal is to enhance productivity and task organization, making it easier for teams to work efficiently and effectively.

## Minimum Viable Product (MVP)

Our MVP includes the following features:

1. **Task Management**:
   
* Add tasks with details such as task name, description, priority, and due date.
* Remove tasks from the system.
* Assign tasks to specific users.
* List all tasks in the system.

2. **Basic Crud Operations**:
   
* Create, read and delete tasks and users.

3. **Task Filtering**:
   
* Find tasks by priority and due date.

4. **User and Task Management**:
   
* Distinguish between Users and Tasks

## File Structure

**Task-Management-Application**
* `lib/`: Library files for the application.
* `models/`: Data models for tasks and users.
* `cli.py`: Command-line interface for the application.
* `database.py`: Database connection and operations.
* `helpers.py`: Helper functions for the application.
* `initialize_db.py`: Script to initialize the database.
* `requirements.txt`: List of dependencies required by the application.
* `test_db_connection.py`: Script to test the database connection.
* `LICENSE`: License information for the application.
* `Pipfile`: Pipfile for the application.
* `Pipfile.lock`: Lock file for the Pipfile.
* `README.md`: This README file.
* `task_manager.db`: Database file for the application.


## Installation and Setup

* Fork and clone the repository using `git clone https://github.com/your-username/task-management-app.git.`
* Create virtual environment using `pipenv install.`
* Enter the virtual environment using `pipenv shell`
* Initialize the database using python `initialize_db.py.`
* Run the application using `python cli.py.`

## Usage 

Once set up, you can manage users and assign tasks using the CLI.

## Contributors

The Task Management Application is developed and maintained by:
 * Nicole Apono
 * Tony Brian
 * Dennis Githaiga
 * Joy Wanjiru

## License

This project is licensed under the [MIT License](LICENSE).

© 2024 Task Management Application.

   
    
    


