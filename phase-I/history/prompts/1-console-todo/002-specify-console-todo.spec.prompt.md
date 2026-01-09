---
id: 2
title: Specify Console Todo Feature
stage: spec
date: 2026-01-08
surface: agent
model: claude-sonnet-4-5-20250929
feature: 1-console-todo
branch: 1-console-todo
user: default
command: /sp.specify In-Memory Console-Based Todo App...
labels: [spec, console-todo, phase-I]
links:
  spec: specs/1-console-todo/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/1-console-todo/spec.md
  - specs/1-console-todo/checklists/requirements.md
tests:
  - null
---

## Prompt

/sp.specify In-Memory Console-Based Todo App (Phase I Basic Level)

Target audience: AI agents (e.g., Claude Code) implementing via Agentic Dev Stack workflow
Focus: Command-line todo application with in-memory storage implementing 5 core features (Add, Delete, Update, View, Mark Complete)

Success criteria:

- Fully implements all 5 basic features with intuitive console commands (e.g., `add "Buy milk"`, `list`, `complete 1`, `delete 1`, `update 1 "Buy milk and eggs"`)
- Supports task details: ID, description, completion status; displays numbered lists with status indicators
- Follows clean code principles: modular functions, error handling, input validation, docstrings
- Uses proper Python project structure: `src/` with `__init__.py`, `pyproject.toml` for UV, entrypoint script (e.g., `todo.py` or `main.py`)
- App runs via `uv run python src/todo.py` or similar; resets on restart (in-memory only)
- Reader (implementer) can generate plan, tasks, and code via Spec-Kit Plus workflow without manual coding

Constraints:

- Technology stack: UV for project init/dependencies/runs, Python 3.13+
- In-memory storage only (list/dict of tasks); no files, databases, or persistence
- Console-based input/output only (no GUI, web, or external libs beyond stdlib)
- No manual coding allowed; output spec → plan → tasks → Claude Code implementation
- Commands: Interactive loop with `help`, `quit/exit`; case-insensitive, handles invalid inputs gracefully
- Project init: `uv init todo-app`, minimal deps (none needed), structured dirs/files

Not building:

- Data persistence (files, DB, cloud sync)
- Advanced features (priorities, due dates, categories, search/filter, undo)
- GUI, web API, or mobile app
- External dependencies beyond Python stdlib (e.g., no Click, Rich, SQLAlchemy)
- Multi-user support or authentication

## Response snapshot

Created the feature specification for the Phase I In-Memory Console-Based Todo App. Initialized branch `1-console-todo` and created `specs/1-console-todo/spec.md` with requirements, user scenarios, and success criteria. Validated requirements via a quality checklist.

## Outcome

- ✅ Impact: Requirements finalized for the MVP phase.
- 🧪 Tests: n/a
- 📁 Files: specs/1-console-todo/spec.md, specs/1-console-todo/checklists/requirements.md
- 🔁 Next prompts: /sp.plan to design the technical architecture.
- 🧠 Reflection: The prompt provides very clear success criteria and constraints which made specification straightforward.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): n/a
- Prompt variant (if applicable): n/a
- Next experiment (smallest change to try): n/a
