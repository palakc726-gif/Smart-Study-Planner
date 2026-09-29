# Student Task & Assignment Manager

## 1. Project Overview

Student Task & Assignment Manager is a Python-based command-line application designed to help students organize and manage their academic tasks and assignments.

The application allows students to create, view, update, delete, search, filter, and complete tasks. Task information is stored permanently in a JSON file so that the data is available even after the application is closed.

The project demonstrates important Python programming concepts such as functions, classes, lists, dictionaries, file handling, JSON storage, modular programming, exception handling, input validation, and automated testing.

---

## 2. Problem Statement

Students often have multiple assignments, projects, and academic tasks with different subjects, priorities, and deadlines. Managing these tasks manually can make it difficult to track pending and completed work.

This project provides a simple centralized task management system that allows students to organize their academic work and monitor their progress.

---

## 3. Objectives

The main objectives of this project are:

* To create a simple academic task management system.
* To allow students to add and manage assignments.
* To provide task status tracking.
* To provide search and filtering functionality.
* To generate task completion statistics.
* To store task information permanently.
* To demonstrate modular Python programming.
* To implement input validation and error handling.
* To demonstrate automated testing.

---

## 4. Features

### Task Management

* Add a new task.
* View all tasks.
* Update an existing task.
* Delete a task.
* Mark a task as completed.

### Search and Filtering

* Search tasks using keywords.
* Filter tasks by status.
* Filter tasks by priority.

### Reporting

The application generates a summary containing:

* Total number of tasks.
* Number of completed tasks.
* Number of pending tasks.
* Task completion percentage.

### Data Storage

Task information is stored in a JSON file.

### Validation

The application validates:

* Task description.
* Subject.
* Priority.
* Deadline.
* Task ID.

### Testing

The project contains automated tests for:

* Task functionality.
* Input validation.
* Data storage.

---

## 5. Technologies Used

* Python 3
* JSON
* Pytest
* Git
* GitHub
* Visual Studio Code

---

## 6. Python Concepts Used

This project demonstrates:

* Variables
* Data types
* Conditional statements
* Loops
* Functions
* Lists
* Dictionaries
* Classes and objects
* Modules
* File handling
* JSON
* Exception handling
* Input validation
* List comprehensions
* Automated testing

---

## 7. Project Structure

```text
Student-Task-Assignment-Manager/
│
├── README.md
├── statement.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── main.py
│   ├── task.py
│   ├── task_manager.py
│   ├── storage.py
│   ├── validator.py
│   ├── search.py
│   └── report.py
│
├── data/
│   └── tasks.json
│
├── tests/
│   ├── test_task.py
│   ├── test_validator.py
│   └── test_storage.py
│
├── screenshots/
│
└── docs/
    ├── architecture.png
    ├── workflow.png
    ├── use_case.png
    ├── class_diagram.png
    └── sequence_diagram.png
```

---

## 8. Installation

### Step 1: Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### Step 2: Open the project directory

```bash
cd Student-Task-Assignment-Manager
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

## 9. Running the Application

Run the following command from the project root:

```bash
python src/main.py
```

The application will display the main menu.

---

## 10. Main Menu

The application provides the following options:

```text
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Completed
6. Search Task
7. Filter Tasks
8. Generate Report
9. Exit
```

---

## 11. Data Storage

Task information is stored in:

```text
data/tasks.json
```

The JSON file contains information such as:

* Task ID
* Description
* Subject
* Priority
* Deadline
* Status

---

## 12. Testing

The project uses Pytest for automated testing.

Run:

```bash
pytest
```

The tests verify:

* Task creation.
* Task completion.
* Task conversion to dictionary.
* Input validation.
* Invalid input handling.
* Saving and loading task data.

---

## 13. Screenshots

Screenshots of the application will be added to the `screenshots/` directory.

Recommended screenshots include:

1. Main menu.
2. Adding a task.
3. Viewing tasks.
4. Updating a task.
5. Searching/filtering tasks.
6. Generated task report.
7. Test results.

---

## 14. System Architecture

The application follows a modular architecture.

```text
User
  |
  v
main.py
  |
  v
Task Manager
  |
  +---- Validator
  |
  +---- Search
  |
  +---- Report
  |
  v
Storage
  |
  v
tasks.json
```

---

## 15. Future Enhancements

Possible future improvements include:

* Graphical user interface.
* Automatic deadline reminders.
* Calendar integration.
* Recurring tasks.
* Subject-wise progress charts.
* SQLite database.
* Login and multiple-user support.
* Desktop or web-based version.

---

## 16. Project Status

The project is developed as part of the VITyarthi Python Essentials course evaluation.

---

## 17. Author

**Student Task & Assignment Manager**

Developed as an academic Python project for VITyarthi.
