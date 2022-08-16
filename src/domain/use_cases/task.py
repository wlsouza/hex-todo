from src.domain.entities.task import Task
from src.domain.ports.outbound.db.postgres.repositories.task import TaskRepository


class Task:

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def create_task(self, task: Task):
        self.repository.create(task=task)