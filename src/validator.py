def validate_subject(subject):
    return bool(subject.strip())


def validate_topic(topic):
    return bool(topic.strip())


def validate_difficulty(difficulty):

    return difficulty.lower() in [
        "easy",
        "medium",
        "hard"
    ]


def validate_study_hours(hours):

    try:
        return float(hours) > 0

    except ValueError:
        return False


def validate_deadline(deadline):
    return bool(deadline.strip())


def validate_task_id(task_id):

    try:
        return int(task_id) > 0

    except ValueError:
        return False