class StudyTask:

    def __init__(
        self,
        task_id,
        subject,
        topic,
        difficulty,
        study_hours,
        deadline,
        status="Pending"
    ):
        self.task_id = task_id
        self.subject = subject
        self.topic = topic
        self.difficulty = difficulty
        self.study_hours = float(study_hours)
        self.deadline = deadline
        self.status = status

    def mark_completed(self):
        self.status = "Completed"

    def to_dict(self):
        return {
            "id": self.task_id,
            "subject": self.subject,
            "topic": self.topic,
            "difficulty": self.difficulty,
            "study_hours": self.study_hours,
            "deadline": self.deadline,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return StudyTask(
            data["id"],
            data["subject"],
            data["topic"],
            data["difficulty"],
            data["study_hours"],
            data["deadline"],
            data["status"]
        )