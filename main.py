from task_manager import TaskManager

def main():
    manager = TaskManager('tasks.json')

    while True:
        print("\nТрекер задач:")
        print("1. Добавить задачу")
        print("2. Редактировать задачу")
        print("3. Удалить задачу")
        print("4. Просмотреть все задачи")
        print("5. Поиск задач")
        print("6. Сохранить задачи")
        print("7. Выход")

        choice = input("Выберите действие (1-7): ")

        if choice == "1":
            title = input("Введите имя задачи: ")
            description = input("Введите описание задачи: ")
            manager.add_task(title, description)
            print("Задача добавлена.")

        elif choice == "2":
            task_id = int(input("Введите ID задачи для редактирования: "))
            title = input("Введите новое имя (или оставьте пустым для пропуска): ")
            description = input("Введите новое описание (или оставьте пустым для пропуска): ")
            status = input("Введите новый статус (или оставьте пустым для пропуска): ")
            manager.edit_task(task_id, title or None, description or None, status or None)

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
            print("Задачи успешно сохранены.")

        elif choice == "7":
            print("Выход из программы.")
            manager.save_tasks()  # Сохранить перед выходом
            break

        else:
            print("Некорректный ввод. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()