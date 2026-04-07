from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

from domain import Task, TaskFactory

router = APIRouter()


# DTOs

class TaskCreateRequest(BaseModel):
    title: str
    priority: str
    description: Optional[str] = None
    assignee_id: Optional[str] = None


class TaskResponse(BaseModel):
    id: str
    title: str
    priority: str
    status: str
    created_at: datetime


# Service

class TaskService:

    def create_task(self, request: TaskCreateRequest) -> Task:
        return TaskFactory.create(
            title=request.title,
            priority=request.priority,
            description=request.description,
            assignee_id=request.assignee_id,
        )


# Endpoint

@router.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(
    request: TaskCreateRequest,
    service: TaskService = Depends(TaskService),
):
    task = service.create_task(request)

    return TaskResponse(
        id=task.id,
        title=task.title,
        priority=task.priority.value,
        status=task.status.value,
        created_at=task.created_at,
    )
