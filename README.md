# Smart Study Planner

## 1. Project Overview

Smart Study Planner is a Python-based command-line application designed to help students organize their study activities and prioritize academic topics.

The application allows students to create study tasks by specifying the subject, topic, difficulty level, estimated study hours, and deadline. The system can then calculate a priority score and generate a recommended study order.

The application also provides task management, search, progress tracking, reporting, input validation, and JSON-based data storage.

The project demonstrates Python programming concepts such as classes, objects, functions, lists, dictionaries, modules, file handling, JSON, sorting, input validation, and automated testing.

---

## 2. Problem Statement

Students often have multiple subjects and topics to study, each with different difficulty levels, estimated study times, and deadlines. Managing these topics manually can make it difficult to determine which topic should be studied first.

Smart Study Planner provides a simple solution by allowing students to organize their study tasks and generate a priority-based study plan.

The system considers factors such as topic difficulty, estimated study hours, and completion status when calculating study priority.

---

## 3. Objectives

The main objectives of the project are:

- To help students organize their study tasks.
- To maintain a list of subjects and topics.
- To record estimated study hours.
- To record study deadlines.
- To classify topics according to difficulty.
- To calculate a priority score for study tasks.
- To generate a recommended study order.
- To track completed and pending topics.
- To calculate overall study progress.
- To store study information permanently.
- To demonstrate modular Python programming.
- To implement input validation and error handling.
- To demonstrate automated testing.

---

## 4. Features

### 4.1 Study Task Management

Users can:

- Add a study task.
- View all study tasks.
- Update an existing study task.
- Delete a study task.
- Mark a study task as completed.

### 4.2 Study Task Information

Each study task contains:

- Task ID.
- Subject.
- Topic.
- Difficulty.
- Estimated study hours.
- Deadline.
- Completion status.

### 4.3 Smart Priority Calculation

The system calculates a priority score based on:

- Difficulty level.
- Estimated study workload.
- Completion status.

Higher-priority pending tasks are placed earlier in the generated study plan.

### 4.4 Smart Study Plan

The application generates a recommended study order by sorting pending study tasks according to their calculated priority.

### 4.5 Search

Users can search for study tasks using:

- Subject name.
- Topic name.

### 4.6 Progress Report

The system generates a report containing:

- Total topics.
- Completed topics.
- Pending topics.
- Total estimated study hours.
- Completion percentage.

### 4.7 Data Storage

Study task information is stored in a JSON file so that data remains available when the application is restarted.

### 4.8 Input Validation

The application validates:

- Subject.
- Topic.
- Difficulty.
- Study hours.
- Deadline.
- Task ID.

---

## 5. Functional Modules

The project contains the following major modules:

### Module 1: Study Task Management

Responsible for:

- Creating study tasks.
- Viewing study tasks.
- Updating study tasks.
- Deleting study tasks.
- Completing study tasks.

### Module 2: Smart Planning

Responsible for:

- Calculating priority scores.
- Identifying pending tasks.
- Sorting tasks according to priority.
- Generating the recommended study plan.

### Module 3: Data Storage

Responsible for:

- Loading study tasks from JSON.
- Saving study tasks to JSON.

### Module 4: Search

Responsible for searching study tasks by subject or topic.

### Module 5: Reporting

Responsible for calculating study statistics and generating the study progress report.

### Module 6: Validation

Responsible for checking user input before processing it.

---

## 6. Technologies Used

- Python 3
- JSON
- Pytest
- Git
- GitHub
- Visual Studio Code

---

## 7. Python Concepts Used

This project demonstrates:

- Variables and data types.
- Conditional statements.
- Loops.
- Functions.
- Lists.
- Dictionaries.
- Classes and objects.
- Modules.
- File handling.
- JSON serialization and deserialization.
- List comprehensions.
- Sorting.
- Lambda functions.
- Input validation.
- Exception handling.
- Automated testing.

---

## 8. Project Structure

```text
Smart-Study-Planner/
│
├── README.md
├── statement.md
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── main.py
│   ├── study_task.py
│   ├── study_manager.py
│   ├── storage.py
│   ├── validator.py
│   ├── planner.py
│   └── report.py
│
├── data/
│   └── study_tasks.json
│
├── tests/
│   ├── test_study_task.py
│   ├── test_validator.py
│   └── test_planner.py
│
├── screenshots/
│
└── docs/