from typing import Protocol
from src.domain.entities.task import Task
from src.domain.ports.outbound.db.repositories.task import TaskRepository


class TaskInterface(Protocol):

    def __init__(self, repository: TaskRepository):
        pass

    def create(self, task: Task) -> None:
        pass

