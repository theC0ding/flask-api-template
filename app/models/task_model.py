from enum import Enum
# uuid is a module that helps generate random unique identifiers
import uuid


class TaskStatus(Enum):
    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'


class Task:
    def __init__(self, task_id: uuid.UUID, task_name: str, task_description: str, task_status: TaskStatus):
        self.task_id = task_id
        self.task_name = task_name
        self.task_description = task_description
        self.task_status = task_status

    def serialize(self) -> dict:
        return {
            'task_id': self.task_id.hex,
            'task_name': self.task_name,
            'task_description': self.task_description,
            'task_status': self.task_status
        }
