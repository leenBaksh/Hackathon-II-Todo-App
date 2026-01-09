from fastapi import APIRouter, HTTPException
from typing import List
from ...core.db import SessionDep
from ...models.task import Task, TaskCreate, TaskUpdate
from ...schemas.task import TaskPublic as TaskSchema
import uuid
from datetime import datetime

router = APIRouter()

@router.get("/tasks", response_model=List[TaskSchema])
def read_tasks(db: SessionDep, skip: int = 0, limit: int = 100):
    tasks = db.query(Task).offset(skip).limit(limit).all()
    return tasks

@router.get("/tasks/{task_id}", response_model=TaskSchema)
def read_task(task_id: str, db: SessionDep):
    from uuid import UUID
    try:
        uuid_obj = UUID(task_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid task ID format")

    task = db.get(Task, uuid_obj)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/tasks", response_model=TaskSchema)
def create_task(task: TaskCreate, db: SessionDep):
    db_task = Task(
        id=uuid.uuid4(),
        title=task.title,
        description=task.description,
        is_completed=task.is_completed,
        user_id=task.user_id,  # This should come from authenticated user in real app
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.put("/tasks/{task_id}", response_model=TaskSchema)
def update_task(task_id: str, task: TaskUpdate, db: SessionDep):
    from uuid import UUID
    try:
        uuid_obj = UUID(task_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid task ID format")

    db_task = db.get(Task, uuid_obj)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    task_data = task.model_dump(exclude_unset=True)
    for key, value in task_data.items():
        setattr(db_task, key, value)

    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.delete("/tasks/{task_id}")
def delete_task(task_id: str, db: SessionDep):
    from uuid import UUID
    try:
        uuid_obj = UUID(task_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid task ID format")

    task = db.get(Task, uuid_obj)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}