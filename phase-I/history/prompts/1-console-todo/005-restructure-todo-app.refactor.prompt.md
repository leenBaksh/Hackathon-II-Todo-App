---
id: 5
title: Restructure Todo App Package
stage: refactor
date: 2026-01-08
surface: agent
model: claude-sonnet-4-5-20250929
feature: 1-console-todo
branch: 1-console-todo
user: default
command: Restructure project to src/todo_app/{cli,models,repositories,services,utils}
labels: [refactor, project-structure, python]
links:
  spec: specs/1-console-todo/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - src/todo_app/__init__.py
  - src/todo_app/__main__.py
  - src/todo_app/cli/interface.py
  - src/todo_app/models/task.py
  - src/todo_app/repositories/task_repository.py
  - src/todo_app/services/todo_service.py
  - tests/test_app.py
  - pyproject.toml
tests:
  - tests/test_app.py
---

## Prompt

"But project name is todo_app, while your package folder is likely todo (or something else). dictories would be like src /cli/model/ repositories/service/utils /test"

## Response snapshot

Restructured the project from a single-file module approach to a multi-layered domain-driven structure under the `todo_app` package.
1. `models/`: Defined `Task` entity.
2. `repositories/`: In-memory storage management.
3. `services/`: Business logic orchestration.
4. `cli/`: Interactive REPL interface.
5. Updated `pyproject.toml` and tests to match new structure. Verified with all tests passing.

## Outcome

- ✅ Impact: Improved modularity and alignment with standard Python project layouts.
- 🧪 Tests: 10 tests passed (100% logic coverage).
- 📁 Files: src/todo_app/, tests/, pyproject.toml
- 🔁 Next prompts: Phase II Planning (FastAPI + SQLModel).
- 🧠 Reflection: Separating the repository layer from the service layer will make the transition to Phase II (SQLModel/Neon) much cleaner.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): n/a
- Prompt variant (if applicable): n/a
- Next experiment (smallest change to try): n/a
