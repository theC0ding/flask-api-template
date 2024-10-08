from app.models.task_model import Task, TaskStatus
import uuid


class TaskRepository:
    def __init__(self):
        self.tasks = []

    def create_task(self, task_name: str, task_description: str) -> Task:
        task = Task(uuid.uuid4(), task_name, task_description, TaskStatus.PENDING)
        self.tasks.append(task)
        return task

    def get_task(self, task_id: str) -> Task or None:
        for task in self.tasks:
            if task.task_id.hex == task_id:
                return task
        return None

    def get_all_tasks(self) -> list:
        return self.tasks

    def update_task(self, task_id: str, task_name: str, task_description: str, task_status: TaskStatus) -> Task or None:
        for task in self.tasks:
            if task.task_id.hex == task_id:
                task.task_name = task_name
                task.task_description = task_description
                task.task_status = task_status
                return task
        return None

    def delete_task(self, task_id: str) -> Task or None:
        for task in self.tasks:
            if task.task_id.hex == task_id:
                self.tasks.remove(task)
                return task
        return None
