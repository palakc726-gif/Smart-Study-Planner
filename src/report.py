def total_study_hours(tasks):

    return sum(
        task.study_hours
        for task in tasks
    )


def completed_tasks(tasks):

    return sum(
        1
        for task in tasks
        if task.status == "Completed"
    )


def pending_tasks(tasks):

    return sum(
        1
        for task in tasks
        if task.status == "Pending"
    )


def completion_percentage(tasks):

    if not tasks:
        return 0

    completed = completed_tasks(tasks)

    return (completed / len(tasks)) * 100


def generate_report(tasks):

    total = len(tasks)

    completed = completed_tasks(tasks)

    pending = pending_tasks(tasks)

    hours = total_study_hours(tasks)

    percentage = completion_percentage(tasks)

    print("\n========== STUDY REPORT ==========")

    print(f"Total Topics       : {total}")
    print(f"Completed Topics   : {completed}")
    print(f"Pending Topics     : {pending}")
    print(f"Total Study Hours  : {hours:.2f}")
    print(f"Completion Rate    : {percentage:.2f}%")

    print("==================================")