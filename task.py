class Task:
    def __init__(self, task_id, title, description, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status

    def __repr__(self):
        return f"Task({self.task_id}, {self.title}, {self.description}, {self.status})"