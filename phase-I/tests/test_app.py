import pytest
from todo_app.services.todo_service import create_task, get_tasks, mark_task_complete, update_task_description, delete_task

def test_add_task():
    task = create_task("Buy milk")
    assert task.description == "Buy milk"
    assert task.id == 1
    assert task.completed is False

def test_add_task_empty():
    with pytest.raises(ValueError):
        create_task("")

def test_list_tasks_empty():
    assert get_tasks() == []

def test_list_tasks_content():
    create_task("One")
    create_task("Two")
    tasks = get_tasks()
    assert len(tasks) == 2
    assert tasks[0].description == "One"
    assert tasks[1].description == "Two"

def test_complete_task():
    create_task("Test")
    assert mark_task_complete(1) is True
    assert get_tasks()[0].completed is True

def test_complete_task_missing():
    assert mark_task_complete(99) is False

def test_update_task():
    create_task("Old")
    assert update_task_description(1, "New") is True
    assert get_tasks()[0].description == "New"

def test_update_task_empty():
    create_task("Old")
    assert update_task_description(1, "") is False

def test_delete_task():
    create_task("Gone")
    assert delete_task(1) is True
    assert len(get_tasks()) == 0

def test_delete_task_missing():
    assert delete_task(99) is False
