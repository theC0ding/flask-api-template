from app.models.task_model import Task, TaskStatus
from app.repositories.task_repository import TaskRepository


class TaskService:
    def __init__(self):
        self.task_repository = TaskRepository()

    def create_task(self, task_name: str, task_description: str) -> Task:
        return self.task_repository.create_task(task_name, task_description)

    def get_task(self, task_id: str) -> Task or None:
        return self.task_repository.get_task(task_id)

    def get_all_tasks(self) -> list:
        return self.task_repository.get_all_tasks()

    def update_task(self, task_id: str, task_name: str, task_description: str, task_status: TaskStatus) -> Task or None:
        return self.task_repository.update_task(task_id, task_name, task_description, task_status)

    def delete_task(self, task_id: str) -> Task or None:
        return self.task_repository.delete_task(task_id)
