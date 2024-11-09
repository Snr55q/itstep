class Task:
    def __init__(self, name, description, deadline):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        status = "Виконано" if self.completed else "Не виконано"
        return f"{self.name}: {self.description} (Дедлайн: {self.deadline}) - {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, task):
        self.tasks.remove(task)

    def task_completed(self, task):
        task.complete()

    def list_tasks(self):
        for task in self.tasks:
            print(task)


task1 = Task("Завдання 1", "Опис завдання 1", "09.11.2024")
task2 = Task("Завдання 2", "Опис завдання 2", "09.11.2025")

manager = TaskManager()
manager.add_task(task1)
manager.add_task(task2)

print("Список завдань:")
manager.list_tasks()

print("Відмічаємо перше завдання як виконане:")
manager.task_completed(task1)
manager.list_tasks()
