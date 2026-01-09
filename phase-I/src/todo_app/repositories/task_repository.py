from typing import List, Optional
from todo_app.models.task import Task

# In-memory storage
_tasks: List[Task] = []
_next_id: int = 1

def reset_storage():
    """Reset the in-memory storage."""
    global _tasks, _next_id
    _tasks = []
    _next_id = 1

def add(description: str) -> Task:
    global _next_id
    task = Task(id=_next_id, description=description.strip())
    _tasks.append(task)
    _next_id += 1
    return task

def get_all() -> List[Task]:
    return _tasks

def find_by_id(task_id: int) -> Optional[Task]:
    for task in _tasks:
        if task.id == task_id:
            return task
    return None

def remove(task_id: int) -> bool:
    global _tasks
    for i, task in enumerate(_tasks):
        if task.id == task_id:
            _tasks.pop(i)
            return True
    return False
