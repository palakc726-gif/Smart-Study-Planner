def difficulty_score(difficulty):

    scores = {
        "Easy": 1,
        "Medium": 2,
        "Hard": 3
    }

    return scores.get(difficulty, 1)


def calculate_priority(task):

    difficulty = difficulty_score(
        task.difficulty
    )

    hours = task.study_hours

    if hours >= 4:
        workload = 3

    elif hours >= 2:
        workload = 2

    else:
        workload = 1

    score = difficulty + workload

    if task.status == "Completed":
        score = 0

    return score


def generate_study_plan(tasks):

    pending_tasks = [
        task
        for task in tasks
        if task.status == "Pending"
    ]

    sorted_tasks = sorted(
        pending_tasks,
        key=lambda task: calculate_priority(task),
        reverse=True
    )

    return sorted_tasks