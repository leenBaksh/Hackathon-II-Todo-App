# Data Model: Todo Application

## Entities

### User
Represents an authenticated participant in the system.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| id | UUID/Int | Primary Key | Auto-increment/Generated |
| email | String | User's unique email | Unique, Not Null |
| hashed_password | String | Securely stored password | Not Null |
| created_at | DateTime | Account creation time | Not Null, Default: UTC Now |

**Relationships**:
- `tasks`: One-to-Many relationship with `Task` model.

### Task
Represents an individual action item.

| Field | Type | Description | Constraints |
|-------|------|-------------|-------------|
| id | UUID/Int | Primary Key | Auto-increment/Generated |
| title | String | Brief title of the task | Not Null, Max 255 chars |
| description | Text | Full details | Optional |
| is_completed | Boolean | Status of task | Default: False |
| created_at | DateTime | Creation time | Not Null |
| updated_at | DateTime | Last update time | Not Null |
| user_id | Int | Owner of the task | Foreign Key (users.id), Not Null |

**Relationships**:
- `user`: Many-to-One relationship with `User` model.

## Validation Rules
- Email must follow standard email format.
- Task title cannot be empty.
- Timestamps must be handled on the server side to ensure consistency.
