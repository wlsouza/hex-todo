from typing import Protocol
from src.domain.entities.task import Task

class TaskRepositoryInterface(Protocol):

    def create(self, task: Task) -> None:
        pass
