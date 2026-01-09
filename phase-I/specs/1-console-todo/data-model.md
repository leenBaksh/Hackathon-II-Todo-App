# Data Model: In-Memory Console Todo App

## Entities

### Task
Represents a single todo item in the system.

- **id**: `int` (Unique, auto-incrementing)
- **description**: `str` (Required, non-empty)
- **completed**: `bool` (Default: `False`)
- **created_at**: `datetime` (Isoformat timestamp)

## Validation Rules
- **Description**: Must be a string with 1-255 characters. Cannot be whitespace only.
- **Task ID**: Must be a positive integer that exists in the current session.

## State Transitions
- **Pending** ([ ]) → **Completed** ([x]): Via `complete <id>` command.
- **Any State** → **Updated**: Via `update <id> <new_desc>` command.
- **Any State** → **Deleted**: Via `delete <id>` command.
