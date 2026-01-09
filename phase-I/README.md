# Scalable Todo App (Phase I: In-Memory Console)

A simple, robust command-line todo application built with Python 3.13 and UV. This project follows the Spec-Kit Plus agentic workflow.

## Phase I Features
- **In-Memory Storage**: Fast execution without disk I/O.
- **Full CRUD**: Add, list, update, mark as complete, and delete tasks.
- **Interactive REPL**: User-friendly command loop with input validation.
- **Robustness**: Graceful error handling and input parsing via `shlex`.

## Prerequisites
- [Python 3.13+](https://www.python.org/downloads/)
- [UV Package Manager](https://github.com/astral-sh/uv)

## Installation
Install in editable mode:
```bash
uv pip install -e . --system
```

## Usage
Running the application:
```bash
uv run python -m todo
```

### Available Commands
- `add <description>` - Create a new task.
- `list` - View all tasks and their status.
- `complete <id>` - Mark a task as done.
- `update <id> <new description>` - Edit task text.
- `delete <id>` - Remove a task.
- `help` - Show command reference.
- `exit` or `quit` - Close the app.

## Development & Testing
Run the test suite:
```bash
PYTHONPATH=src python -m pytest tests/
```

## Project Structure
- `src/todo/`: Core application logic and data models.
- `tests/`: Comprehensive unit tests.
- `specs/1-console-todo/`: Design artifacts (Spec, Plan, Tasks, Research).
