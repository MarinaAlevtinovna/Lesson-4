#Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач
# и вывода списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, due_date, status="не выполнено"):
        self.description = description
        self.due_date = due_date
        self.status = status
        self.tasks = []

    def add_task(self, description, due_date):
        task = {
            "description": description,
            "due_date": due_date,
            "status": "не выполнено"
        }
        self.tasks.append(task)
        print(f'Добавлена задача: {description}, выполнить до: {due_date}')

    def mark_task_as_completed(self, description):
        for task in self.tasks:
            if task["description"] == description:
                task["status"] = "выполнено"
                print(f'Задача "{description}" отмечена как выполненная')
                return
        print(f'Задача "{description}" не найдена')

    def list_current_tasks(self):
        current_tasks = [task for task in self.tasks if task["status"] == "не выполнено"]
        if not current_tasks:
            print('Нет текущих (не выполненных) задач')
        else:
            for task in current_tasks:
                print(f'{task["description"]}, выполнить до: {task["due_date"]}, {task["status"]}')

task_manager = Task(description='', due_date='')
task_manager.add_task("Сдать отчет", "12.01.2026")
task_manager.add_task("Завершить проект", "20.07.2024")
task_manager.list_current_tasks()
task_manager.mark_task_as_completed("Сдать отчет")
task_manager.list_current_tasks()