from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import uuid

# Domain
class TaskStatus(Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class TaskPriority(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


# Entity

@dataclass
class Task:
    id: str
    title: str
    priority: TaskPriority
    status: TaskStatus
    created_at: datetime
    description: Optional[str] = None
    assignee_id: Optional[str] = None


# Factory

class TaskFactory:

    @staticmethod
    def create(
        title: str,
        priority: str,
        description: Optional[str] = None,
        assignee_id: Optional[str] = None,
    ) -> Task:

        if not title or not title.strip():
            raise ValueError("title cannot be empty")

        try:
            task_priority = TaskPriority(priority.upper())
        except ValueError:
            raise ValueError(
                f"Invalid priority '{priority}'."
                f"Must be one of {[p.value for p in TaskPriority]}"
            )

        return Task(
            id=str(uuid.uuid4()),
            title=title.strip(),
            priority=task_priority,
            status=TaskStatus.OPEN,
            created_at=datetime.utcnow(),
            description=description,
            assignee_id=assignee_id,
        )
