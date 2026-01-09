# Implementation Plan: Core Infrastructure & Database Schema

**Branch**: `2-infra-db-schema` | **Date**: 2026-01-08 | **Spec**: [specs/2-infra-db-schema/spec.md](./spec.md)
**Input**: Feature specification from `/specs/2-infra-db-schema/spec.md`

## Summary
Establish the foundational data layer for the multi-user Todo application. This includes setting up a monorepo structure, defining SQLModel data models (User, Task), configuring Neon PostgreSQL with pydantic-settings, and providing automation scripts for database management and verification.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: FastAPI, SQLModel, Alembic, Pydantic-Settings, python-dotenv, psycopg2-binary
**Storage**: Neon Serverless PostgreSQL
**Testing**: verification scripts (`verify_db.py`)
**Target Platform**: Linux/WSL2
**Project Type**: Web application (Frontend + Backend monorepo)
**Performance Goals**: Sub-second DB connection/query latency.
**Constraints**: No manual SQL for schema; synchronous driver for Phase II simplicity; absolute data isolation via User ID.
**Scale/Scope**: Foundations for 10k users, extensible data model.

## Constitution Check

| Rule | Status | Notes |
|------|--------|-------|
| Modularity | ✅ | Backend/Frontend separated; clear core/models/scripts structure. |
| Security-First | ✅ | User-scoped data isolation enforced in schema design. |
| Developer Ergonomics | ✅ | Automated setup/verify scripts included in plan. |
| Framework Leverage | ✅ | Using SQLModel/pydantic-settings/Alembic best practices. |
| Type Safety | ✅ | SQLModel mandatory for all schemas. |

## Project Structure

```text
todo-app/
├── backend/
│   ├── app/
│   │   ├── core/           # Config, security, DB setup
│   │   ├── models/         # SQLModel models (Task, User)
│   │   └── schemas/        # Pydantic request/response schemas
│   ├── alembic/           # Migration files
│   ├── scripts/           # Setup, seed_db, verify_db
│   └── requirements.txt
└── frontend/              # Placeholder for UI
```

## Implementation Steps

1.  **Initialize Project Structure**
    - Create `backend/app/core/`, `backend/app/models/`, `backend/app/schemas/`, `backend/alembic/`, and `backend/scripts/` directories.
    - Create placeholders for `frontend/`.
    - Create `backend/__init__.py` and `backend/app/__init__.py` files for package resolution.

2.  **Set Up Python Environment & Dependencies**
    - Create `backend/requirements.txt` with required packages.
    - Create a `.env` file in the repository root with `DATABASE_URL`.

3.  **Implement Configuration & Database Core**
    - Create `backend/app/core/config.py`: Use `pydantic-settings` to load `DATABASE_URL`.
    - Create `backend/app/core/db.py`: Define SQLModel `engine` and `SessionDep` dependency.

4.  **Define SQLModel Data Models**
    - Create `backend/app/models/user.py`: `User` model with `tasks` relationship.
    - Create `backend/app/models/task.py`: `Task` model with `user` relationship and `user_id` foreign key.

5.  **Create Pydantic Schemas**
    - Create `backend/app/schemas/user.py`: `UserCreate`, `UserPublic`.
    - Create `backend/app/schemas/task.py`: `TaskCreate`, `TaskUpdate`, `TaskPublic`.

6.  **Initialize Alembic & Generate Migration**
    - Run `alembic init backend/alembic`.
    - Update `backend/alembic/env.py` to import `SQLModel` and app models.
    - Configure `alembic.ini` to use environment variables for connection.
    - Generate initial migration: `alembic revision --autogenerate -m "initial"`.

7.  **Build Automation Scripts**
    - Create `backend/scripts/setup_db.py`: Automates `alembic upgrade head`.
    - Create `backend/scripts/seed_db.py`: Injects sample multi-user data.
    - Create `backend/scripts/verify_db.py`: Connectivity and schema integrity check.

8.  **Final Integration Test**
    - Perform end-to-end verification using `verify_db.py`.
