from study_task import StudyTask
from storage import load_tasks, save_tasks


class StudyManager:

    def __init__(self):

        self.tasks = [
            StudyTask.from_dict(task)
            for task in load_tasks()
        ]

    def get_next_id(self):

        if not self.tasks:
            return 1

        return max(
            task.task_id
            for task in self.tasks
        ) + 1

    def add_task(
        self,
        subject,
        topic,
        difficulty,
        study_hours,
        deadline
    ):

        task = StudyTask(
            self.get_next_id(),
            subject,
            topic,
            difficulty,
            study_hours,
            deadline
        )

        self.tasks.append(task)

        self.save()

        return task

    def get_all_tasks(self):
        return self.tasks

    def find_task(self, task_id):

        for task in self.tasks:

            if task.task_id == task_id:
                return task

        return None

    def update_task(
        self,
        task_id,
        subject,
        topic,
        difficulty,
        study_hours,
        deadline
    ):

        task = self.find_task(task_id)

        if task is None:
            return False

        task.subject = subject
        task.topic = topic
        task.difficulty = difficulty
        task.study_hours = float(study_hours)
        task.deadline = deadline

        self.save()

        return True

    def delete_task(self, task_id):

        task = self.find_task(task_id)

        if task is None:
            return False

        self.tasks.remove(task)

        self.save()

        return True

    def complete_task(self, task_id):

        task = self.find_task(task_id)

        if task is None:
            return False

        task.mark_completed()

        self.save()

        return True

    def save(self):

        data = [
            task.to_dict()
            for task in self.tasks
        ]

        return save_tasks(data)