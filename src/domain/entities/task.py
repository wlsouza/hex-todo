import enum
from datetime import datetime
from pydantic import BaseModel, UUID4


class TaskStatus(str, enum.Enum):
    PENDING = "pending"
    RUNNING = "running"
    FINISHED = "finished"
    CANCELED = "canceled"
    PAUSED = "paused"


class Task(BaseModel):
    id: int|None
    title: str
    description: str|None = None
    status: TaskStatus = TaskStatus.PENDING
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()