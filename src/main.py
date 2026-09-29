from study_manager import StudyManager

from planner import (
    calculate_priority,
    generate_study_plan
)

from report import generate_report

from validator import (
    validate_subject,
    validate_topic,
    validate_difficulty,
    validate_study_hours,
    validate_deadline,
    validate_task_id
)


manager = StudyManager()


def display_task(task):

    priority = calculate_priority(task)

    print(
        f"ID: {task.task_id} | "
        f"Subject: {task.subject} | "
        f"Topic: {task.topic} | "
        f"Difficulty: {task.difficulty} | "
        f"Hours: {task.study_hours} | "
        f"Deadline: {task.deadline} | "
        f"Status: {task.status} | "
        f"Priority: {priority}"
    )


def add_task():

    print("\n========== ADD STUDY TASK ==========")

    subject = input("Enter subject: ")

    if not validate_subject(subject):
        print("Subject cannot be empty.")
        return

    topic = input("Enter topic: ")

    if not validate_topic(topic):
        print("Topic cannot be empty.")
        return

    difficulty = input(
        "Enter difficulty (Easy/Medium/Hard): "
    )

    if not validate_difficulty(difficulty):
        print("Invalid difficulty.")
        return

    study_hours = input(
        "Enter estimated study hours: "
    )

    if not validate_study_hours(study_hours):
        print("Invalid study hours.")
        return

    deadline = input(
        "Enter deadline (DD-MM-YYYY): "
    )

    if not validate_deadline(deadline):
        print("Deadline cannot be empty.")
        return

    task = manager.add_task(
        subject,
        topic,
        difficulty.capitalize(),
        study_hours,
        deadline
    )

    print(
        f"Study task added successfully! "
        f"Task ID: {task.task_id}"
    )


def view_tasks():

    print("\n========== ALL STUDY TASKS ==========")

    tasks = manager.get_all_tasks()

    if not tasks:
        print("No study tasks available.")
        return

    for task in tasks:
        display_task(task)


def update_task():

    print("\n========== UPDATE STUDY TASK ==========")

    task_id = input("Enter task ID: ")

    if not validate_task_id(task_id):
        print("Invalid task ID.")
        return

    task_id = int(task_id)

    task = manager.find_task(task_id)

    if task is None:
        print("Task not found.")
        return

    subject = input("Enter new subject: ")
    topic = input("Enter new topic: ")

    difficulty = input(
        "Enter new difficulty (Easy/Medium/Hard): "
    )

    study_hours = input(
        "Enter new study hours: "
    )

    deadline = input(
        "Enter new deadline: "
    )

    if not validate_subject(subject):
        print("Invalid subject.")
        return

    if not validate_topic(topic):
        print("Invalid topic.")
        return

    if not validate_difficulty(difficulty):
        print("Invalid difficulty.")
        return

    if not validate_study_hours(study_hours):
        print("Invalid study hours.")
        return

    if not validate_deadline(deadline):
        print("Invalid deadline.")
        return

    manager.update_task(
        task_id,
        subject,
        topic,
        difficulty.capitalize(),
        study_hours,
        deadline
    )

    print("Study task updated successfully.")


def delete_task():

    print("\n========== DELETE STUDY TASK ==========")

    task_id = input("Enter task ID: ")

    if not validate_task_id(task_id):
        print("Invalid task ID.")
        return

    if manager.delete_task(int(task_id)):
        print("Study task deleted successfully.")
    else:
        print("Study task not found.")


def complete_task():

    print("\n========== COMPLETE STUDY TASK ==========")

    task_id = input("Enter task ID: ")

    if not validate_task_id(task_id):
        print("Invalid task ID.")
        return

    if manager.complete_task(int(task_id)):
        print("Study task marked as completed.")
    else:
        print("Study task not found.")


def create_study_plan():

    print("\n========== SMART STUDY PLAN ==========")

    tasks = manager.get_all_tasks()

    plan = generate_study_plan(tasks)

    if not plan:
        print("No pending study tasks.")
        return

    print("\nRecommended Study Order:\n")

    for index, task in enumerate(plan, start=1):

        print(
            f"{index}. "
            f"{task.subject} - "
            f"{task.topic} | "
            f"Difficulty: {task.difficulty} | "
            f"Hours: {task.study_hours} | "
            f"Deadline: {task.deadline} | "
            f"Priority: {calculate_priority(task)}"
        )


def search_tasks():

    print("\n========== SEARCH STUDY TASKS ==========")

    keyword = input(
        "Enter subject or topic keyword: "
    ).lower()

    results = []

    for task in manager.get_all_tasks():

        if (
            keyword in task.subject.lower()
            or keyword in task.topic.lower()
        ):
            results.append(task)

    if not results:
        print("No matching tasks found.")
        return

    for task in results:
        display_task(task)


def main():

    while True:

        print("\n")
        print("==========================================")
        print("          SMART STUDY PLANNER")
        print("==========================================")

        print("1. Add Study Task")
        print("2. View All Study Tasks")
        print("3. Update Study Task")
        print("4. Delete Study Task")
        print("5. Mark Task Completed")
        print("6. Search Study Tasks")
        print("7. Generate Smart Study Plan")
        print("8. Generate Study Report")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            update_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            complete_task()

        elif choice == "6":
            search_tasks()

        elif choice == "7":
            create_study_plan()

        elif choice == "8":
            generate_report(
                manager.get_all_tasks()
            )

        elif choice == "9":
            print(
                "Thank you for using Smart Study Planner!"
            )
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()