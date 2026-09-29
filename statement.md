# Project Statement

## Project Title

Smart Study Planner

---

## 1. Problem Statement

Students often have multiple subjects and topics to study within limited time. Different topics have different difficulty levels, estimated study hours, and deadlines. Managing these tasks manually can make it difficult to determine which topics should be studied first.

The Smart Study Planner is a Python-based application designed to help students organize their study tasks and generate a priority-based study plan.

The system allows students to add, view, update, delete, search, and complete study tasks. It also calculates priority scores and generates a recommended study order for pending topics.

---

## 2. Project Scope

The project focuses on developing a command-line Python application for managing academic study tasks.

The system includes:

- Adding study tasks.
- Viewing all study tasks.
- Updating study tasks.
- Deleting study tasks.
- Marking study tasks as completed.
- Searching study tasks.
- Calculating study priority.
- Generating a smart study plan.
- Tracking study progress.
- Generating study reports.
- Storing data using JSON.
- Validating user input.
- Handling invalid input.

Each study task contains:

- Task ID
- Subject
- Topic
- Difficulty
- Estimated study hours
- Deadline
- Completion status

The project is designed for individual student use and runs locally through a command-line interface.

---

## 3. Target Users

The primary target users are:

- College students
- School students
- Students preparing for examinations
- Students managing multiple subjects
- Students who want to organize their study workload

---

## 4. High-Level Features

### Study Task Management

Users can:

- Add a study task.
- View study tasks.
- Update study tasks.
- Delete study tasks.
- Mark tasks as completed.

### Smart Priority Calculation

The application calculates a priority score using:

- Difficulty level.
- Estimated study workload.
- Completion status.

Difficulty is categorized as:

```text
Easy   = 1
Medium = 2
Hard   = 3