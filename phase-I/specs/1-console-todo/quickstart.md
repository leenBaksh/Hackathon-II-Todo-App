# Quickstart: In-Memory Console Todo App

## Setup
1. Ensure you have `uv` installed.
2. Clone the repository and navigate to the root.
3. Install the project in editable mode:
   ```bash
   uv pip install -e .
   ```

## Running the App
Run the interactive console:
   ```bash
   uv run python -m todo
   ```

## Available Commands
- `add "description"`: Add a new todo.
- `list`: Show all todos with their status.
- `complete <id>`: Mark a todo as finished.
- `update <id> "new description"`: Change the text of an existing todo.
- `delete <id>`: Remove a todo forever.
- `help`: Show this information.
- `exit` or `quit`: Close the application.
