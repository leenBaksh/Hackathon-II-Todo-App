import shlex
from todo_app.services import todo_service
from todo_app.repositories import task_repository

def print_help():
    help_text = """
Scalable Todo App - Phase I Commands:
  add <description>             - Add a new todo item
  list                          - List all todos with status
  complete <id>                 - Mark a todo as completed
  update <id> <new description> - Update a todo's description
  delete <id>                 - Remove a todo item
  help                          - Show this help menu
  exit | quit                   - Close the application
"""
    print(help_text)

def start_repl():
    print("Scalable Todo App - Phase I")
    print("Type 'help' for usage instructions.")

    while True:
        try:
            line = input("> ").strip()
            if not line:
                continue

            parts = shlex.split(line)
            command = parts[0].lower()
            args = parts[1:]

            if command in ("exit", "quit"):
                print("Goodbye!")
                break

            elif command == "help":
                print_help()

            elif command == "add":
                if not args:
                    print("Error: 'add' requires a task description.")
                    continue
                try:
                    task = todo_service.create_task(" ".join(args))
                    print(f"Success: Added task {task.id}")
                except ValueError as e:
                    print(f"Error: {e}")

            elif command == "list":
                tasks = todo_service.get_tasks()
                if not tasks:
                    print("Info: No tasks in the list.")
                    continue
                for t in tasks:
                    status = "[x]" if t.completed else "[ ]"
                    print(f"{t.id}. {status} {t.description}")

            elif command == "complete":
                if not args or not args[0].isdigit():
                    print("Error: 'complete' requires a valid task ID.")
                    continue
                if todo_service.mark_task_complete(int(args[0])):
                    print(f"Success: Task {args[0]} marked as complete.")
                else:
                    print(f"Error: Task {args[0]} not found.")

            elif command == "update":
                if len(args) < 2 or not args[0].isdigit():
                    print("Error: 'update' requires <id> and <new description>.")
                    continue
                if todo_service.update_task_description(int(args[0]), " ".join(args[1:])):
                    print(f"Success: Task {args[0]} updated.")
                else:
                    print(f"Error: Task {args[0]} not found or invalid description.")

            elif command == "delete":
                if not args or not args[0].isdigit():
                    print("Error: 'delete' requires a valid task ID.")
                    continue
                if todo_service.delete_task(int(args[0])):
                    print(f"Success: Task {args[0]} deleted.")
                else:
                    print(f"Error: Task {args[0]} not found.")

            else:
                print(f"Error: Unknown command '{command}'. Type 'help' for usage.")

        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"System Error: {e}")
