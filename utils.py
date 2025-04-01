import json
from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, status="В работе", due_date=None, priority="Средний"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date
        self.priority = priority

    def __str__(self):
        return f"[{self.task_id}] {self.title} - {self.status} (Приоритет: {self.priority}, Срок: {self.due_date})"

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description, due_date=None, priority="Средний"):
        task = Task(self.next_id, title, description, due_date=due_date, priority=priority)
        self.tasks.append(task)
        self.next_id += 1
        print("Задача добавлена:", task)

    def edit_task(self, task_id, title=None, description=None, status=None, due_date=None, priority=None):
        for task in self.tasks:
            if task.task_id == task_id:
                if title is not None:
                    task.title = title
                if description is not None:
                    task.description = description
                if status is not None:
                    task.status = status
                if due_date is not None:
                    task.due_date = due_date
                if priority is not None:
                    task.priority = priority
                print("Задача обновлена:", task)
                return
        print("Задача не найдена.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.task_id != task_id]
        print(f"Задача {task_id} удалена.")

    def view_tasks(self):
        for task in self.tasks:
            print(task)

    def search_tasks(self, keyword):
        results = [task for task in self.tasks if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]
        if results:
            print("Результаты поиска:")
            for task in results:
                print(task)
        else:
            print("Задачи не найдены.")

    def save_tasks(self, filename='tasks.json'):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([task.__dict__ for task in self.tasks], file, ensure_ascii=False, indent=4)
        print("Задачи успешно сохранены.")

    def load_tasks(self, filename='tasks.json'):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.tasks = [Task(**task) for task in data]
                self.next_id = max(task.task_id for task in self.tasks) + 1 if self.tasks else 1
            print("Задачи успешно загружены.")
        except FileNotFoundError:
            print("Файл не найден. Начинаем с пустого списка задач.")

def main():
    manager = TaskManager()
    manager.load_tasks()

    while True:
        print("\nДоступные действия:")
        print("1. Добавить задачу")
        print("2. Редактировать задачу")
        print("3. Удалить задачу")
        print("4. Просмотреть задачи")
        print("5. Искать задачи")
        print("6. Сохранить задачи")
        print("7. Выход")

        choice = input("Выберите действие (число): ")
        if choice == "1":
            title = input("Введите имя задачи: ")
            description = input("Введите описание задачи: ")
            due_date = input("Введите срок выполнения задачи (YYYY-MM-DD или оставьте пустым): ")
            due_date = due_date if due_date else None
            priority = input("Введите приоритет задачи (Высокий/Средний/Низкий): ")
            priority = priority if priority in ["Высокий", "Средний", "Низкий"] else "Средний"
            manager.add_task(title, description, due_date, priority)

        elif choice == "2":
            task_id = int(input("Введите ID задачи для редактирования: "))
            title = input("Введите новое имя (или оставьте пустым для пропуска): ")
            description = input("Введите новое описание (или оставьте пустым для пропуска): ")
            status = input("Введите новый статус (или оставьте пустым для пропуска): ")
            due_date = input("Введите новый срок выполнения (или оставьте пустым для пропуска): ")
            priority = input("Введите новый приоритет (или оставьте пустым для пропуска): ")
            manager.edit_task(
                task_id,
                title or None,
                description or None,
                status or None,
                due_date if due_date else None,
                priority if priority else None
            )

        elif choice == "3":
            task_id = int(input("Введите ID задачи для удаления: "))
            manager.delete_task(task_id)

        elif choice == "4":
            manager.view_tasks()

        elif choice == "5":
            keyword = input("Введите ключевое слово для поиска: ")
            manager.search_tasks(keyword)

        elif choice == "6":
            manager.save_tasks()

        elif choice == "7":
            print("Выход из программы.")
            manager.save_tasks()
            break

        else:
            print("Некорректный ввод. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()