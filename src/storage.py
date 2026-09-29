import json
import os


DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "study_tasks.json"
)


def load_tasks():

    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):

    try:
        with open(DATA_FILE, "w") as file:
            json.dump(tasks, file, indent=4)

        return True

    except OSError:
        return False