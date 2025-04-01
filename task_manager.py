import json
from task import Task

class TaskManager:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                task_data = json.load(f)
                return [Task(**task) for task in task_data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f)

    def add_task(self, title, description, status="pending"):
        task_id = len(self.tasks) + 1
        new_task = Task(task_id, title, description, status)
        self.tasks.append(new_task)

    def edit_task(self, task_id, title=None, description=None, status=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title is not None:
                    task.title = title
                if description is not None:
                    task.description = description
                if status is not None:
                    task.status = status
                break

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def view_tasks(self):
        for task in self.tasks:
            print(f"ID: {task.task_id}, Title: {task.title}, Description: {task.description}, Status: {task.status}")

    def search_tasks(self, keyword):
        found_tasks = [task for task in self.tasks if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]
        for task in found_tasks:
            print(f"ID: {task.task_id}, Title: {task.title}, Description: {task.description}, Status: {task.status}")