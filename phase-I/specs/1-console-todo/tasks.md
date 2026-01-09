# Tasks: In-Memory Console-Based Todo App

**Input**: Design documents from `/specs/1-console-todo/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md

**Tests**: Unit tests are required to ensure 80%+ coverage per constitution.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Initialize Python project with UV in repository root
- [x] T002 Create project structure: `src/todo_app/{cli,models,repositories,services,utils}`
- [x] T003 [P] Configure `pyproject.toml` with `todo_app` script entry point
- [x] T004 Create `src/todo_app/__init__.py` and `src/todo_app/__main__.py` entry point

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core data structures and base logic

- [x] T005 [P] Implement `Task` dataclass in `src/todo_app/models/task.py`
- [x] T006 Implement in-memory repository in `src/todo_app/repositories/task_repository.py`
- [x] T007 [P] Create `tests/conftest.py` with repository reset fixtures

**Checkpoint**: Foundation ready - user story implementation can now begin

## Phase 3: User Story 1 - Core Task Management (Priority: P1) 🎯 MVP

**Goal**: Add and list tasks in an in-memory session

**Independent Test**: Run `add "test"`, then `list`, verify output shows "1. [ ] test"

### Tests for User Story 1
- [x] T008 [P] [US1] Unit test for `create_task` and `get_tasks` in `tests/test_app.py`
- [x] T009 [P] [US1] Unit test for listing tasks in `tests/test_app.py`

### Implementation for User Story 1
- [x] T010 [US1] Implement `todo_service.create_task` in `src/todo_app/services/todo_service.py`
- [x] T011 [US1] Implement `todo_service.get_tasks` in `src/todo_app/services/todo_service.py`
- [x] T012 [US1] Implement CLI interface supporting `add` and `list` in `src/todo_app/cli/interface.py`

**Checkpoint**: User Story 1 fully functional and testable

## Phase 4: User Story 2 - Task Lifecycle (Priority: P2)

**Goal**: Complete, update, and delete tasks

**Independent Test**: Add task, 1) `complete 1` -> [x], 2) `update 1 "new"` -> "new", 3) `delete 1` -> empty list

### Tests for User Story 2
- [x] T013 [P] [US2] Unit test for `mark_task_complete` in `tests/test_app.py`
- [x] T014 [P] [US2] Unit test for `update_task_description` in `tests/test_app.py`
- [x] T015 [P] [US2] Unit test for `delete_task` in `tests/test_app.py`

### Implementation for User Story 2
- [x] T016 [US2] Implement `mark_task_complete` logic in `src/todo_app/services/todo_service.py`
- [x] T017 [US2] Implement `update_task_description` logic in `src/todo_app/services/todo_service.py`
- [x] T018 [US2] Implement `delete_task` logic in `src/todo_app/services/todo_service.py`
- [x] T019 [US2] Update CLI interface in `src/todo_app/cli/interface.py` for task lifecycle commands

**Checkpoint**: User Stories 1 & 2 functional

## Phase 5: User Story 3 - Interactive Session (Priority: P3)

**Goal**: Interface wrapper with help and exit support

**Independent Test**: Start app, run `help` -> see commands, run `exit` -> app closes

### Tests for User Story 3
- [x] T020 [P] [US3] Functional test for CLI input parsing in `tests/test_app.py`

### Implementation for User Story 3
- [x] T021 [US3] Implement command parsing with `shlex` in `src/todo_app/cli/interface.py`
- [x] T022 [US3] Implement `help` command display logic in `src/todo_app/cli/interface.py`
- [x] T023 [US3] Implement `exit`/`quit` command and Ctrl+C handling in `src/todo_app/cli/interface.py`

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and documentation

- [x] T024 [P] Create final `README.md` with setup and usage instructions
- [x] T025 Run `quickstart.md` validation against final implementation
- [x] T026 Verify 80%+ test coverage using `pytest`

## Dependencies & Execution Order

- **Setup (Phase 1)** -> **Foundational (Phase 2)** (Blocks all stories)
- **User Story 1 (P1)**: Priority 1 (MVP)
- **User Story 2 (P2)**: Depends on US1 concepts but can be implemented in parallel if needed
- **User Story 3 (P3)**: Final interface polish

## Implementation Strategy
1. Complete Setup & Foundation.
2. Deliver User Story 1 as MVP.
3. Iteratively add Lifecycle (US2) and Session Polish (US3).
