import pytest
from todo_app.repositories.task_repository import reset_storage

@pytest.fixture(autouse=True)
def clean_storage():
    """Ensure a clean storage for every test."""
    reset_storage()
    yield
