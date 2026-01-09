from typing import List
from todo_app.models.task import Task
from todo_app.repositories import task_repository

def create_task(description: str) -> Task:
    if not description or not description.strip():
        raise ValueError("Task description cannot be empty.")
    return task_repository.add(description)

def get_tasks() -> List[Task]:
    return task_repository.get_all()

def mark_task_complete(task_id: int) -> bool:
    task = task_repository.find_by_id(task_id)
    if task:
        task.completed = True
        return True
    return False

def update_task_description(task_id: int, description: str) -> bool:
    if not description or not description.strip():
        return False
    task = task_repository.find_by_id(task_id)
    if task:
        task.description = description.strip()
        return True
    return False

def delete_task(task_id: int) -> bool:
    return task_repository.remove(task_id)
