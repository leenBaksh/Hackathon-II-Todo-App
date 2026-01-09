---
description: "Task list for Core Infrastructure & Database Schema implementation"
---

# Tasks: Core Infrastructure & Database Schema

**Input**: Design documents from `/specs/2-infra-db-schema/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, quickstart.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create monorepo project structure with `backend/` and `frontend/` directories
- [X] T002 Initialize `backend/requirements.txt` with required dependencies (FastAPI, SQLModel, Alembic, etc.)
- [X] T003 [P] Create `.env` file in project root with `DATABASE_URL` placeholder

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before user story implementation

- [ ] T004 Setup centralized configuration in `backend/app/core/config.py` using `pydantic-settings`
- [ ] T005 [P] Implement database engine and `SessionDep` in `backend/app/core/db.py`
- [ ] T006 [P] Initialize Alembic migrations in `backend/alembic/` and configure `alembic.ini`
- [ ] T007 Configure `backend/alembic/env.py` to use SQLModel metadata and environmental connection string

**Checkpoint**: Foundation ready - user story implementation can now begin

---

## Phase 3: User Story 1 - Database Initialization (Priority: P1) 🎯 MVP

**Goal**: Initialize the persistent storage layer with automated schema creation

**Independent Test**: Running `backend/scripts/setup_db.py` creates the schema on Neon PostgreSQL

### Implementation for User Story 1

- [ ] T008 [P] [US1] Define `User` SQLModel in `backend/app/models/user.py`
- [ ] T009 [P] [US1] Define `Task` SQLModel in `backend/app/models/task.py` with `user_id` foreign key
- [ ] T010 [US1] Create Pydantic schemas for User in `backend/app/schemas/user.py`
- [ ] T011 [US1] Create Pydantic schemas for Task in `backend/app/schemas/task.py`
- [ ] T012 [US1] Generate initial Alembic migration: `alembic revision --autogenerate -m "initial"`
- [ ] T013 [US1] Implement `backend/scripts/setup_db.py` to automate migration upgrades

**Checkpoint**: User Story 1 functional - database schema is live and versioned

---

## Phase 4: User Story 2 - Data Persistence & Relationships (Priority: P1)

**Goal**: Verify multi-user data integrity and parent-child relationships

**Independent Test**: `backend/scripts/seed_db.py` successfully populates related user and task data

### Implementation for User Story 2

- [ ] T014 [US2] Implement `backend/scripts/seed_db.py` to create sample users and tasks
- [ ] T015 [US2] Verify foreign key constraints and cascade behaviors in the seeded data
- [ ] T016 [US2] Validate `updated_at` triggers or logic for task modifications

**Checkpoint**: User Story 2 functional - data relationships are verified

---

## Phase 5: User Story 3 - Infrastructure Verification (Priority: P2)

**Goal**: Provide health reporting for the database layer

**Independent Test**: `backend/scripts/verify_db.py` returns success status and counts

### Implementation for User Story 3

- [ ] T017 [US3] Implement `backend/scripts/verify_db.py` for connectivity and schema inspection
- [ ] T018 [US3] Add environment validation checks to the verification script

**Checkpoint**: All infrastructure verification tools functional

---

## Phase 6: Polish & Cross-Cutting Concerns

- [ ] T019 Update `README.md` with infrastructure setup instructions
- [ ] T020 [P] Finalize docstrings and type annotations across the backend core
- [ ] T021 Validate implementation against `specs/2-infra-db-schema/quickstart.md`

---

## Dependencies & Execution Order

### Phase Dependencies
- **Setup (Phase 1)**: Start immediately
- **Foundational (Phase 2)**: Depends on Phase 1
- **User Story 1 (Phase 3)**: Depends on Phase 2 (Foundation)
- **User Story 2 (Phase 4)**: Depends on US1 completion
- **User Story 3 (Phase 5)**: Depends on US2 (seeded data needed for full verification)

### Parallel Opportunities
- T003 (Env) can be done with T001/T002
- T005 (DB Engine) and T006 (Alembic init) can run in parallel
- T008 (User model) and T009 (Task model) can run in parallel
