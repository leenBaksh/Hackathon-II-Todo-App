<!--
Sync Impact Report
Version change: 1.0.0 → 1.1.0
Modified principles:
  - [PRINCIPLE_1_NAME] → I. Modularity & Separation of Concerns
  - [PRINCIPLE_2_NAME] → II. Security-First Data Isolation
  - [PRINCIPLE_3_NAME] → III. Developer Ergonomics & Automation
  - [PRINCIPLE_4_NAME] → IV. Modern Framework Leverage
  - [PRINCIPLE_5_NAME] → V. Type Safety & Validation (SQLModel)
Added sections:
  - Technical Constraints
  - Development Standards
Templates updated:
  - .specify/templates/plan-template.md (verification pending)
  - .specify/templates/spec-template.md (verification pending)
  - .specify/templates/tasks-template.md (verification pending)
Follow-up TODOs:
  - None
-->

# Todo Full-Stack Web Application Constitution

## Core Principles

### I. Modularity & Separation of Concerns
The application MUST maintain a clear physical and logical separation between the Data Layer (Neon/SQLModel), API Layer (FastAPI), UI Layer (Next.js), and Auth Layer (Better Auth). Each layer should be independently testable and communicable through well-defined contracts.

### II. Security-First Data Isolation
User data isolation MUST be implemented from the start. All database queries and API endpoints must enforce user-scoped data filtering using JWT claims. No cross-user data access is permitted without explicit, audited authorization.

### III. Developer Ergonomics & Automation
Infrastructure setup, database migrations, and verification MUST be automated. Developers should be able to spin up a fully verified environment using a single command or a series of scripts in the `scripts/` directory.

### IV. Modern Framework Leverage
The project SHOULD leverage the full power of its chosen stack (Next.js App Router, FastAPI, SQLModel). Avoid custom-built alternatives for features natively supported by these frameworks unless architectural trade-offs are documented and approved via ADR.

### V. Type Safety & Validation (SQLModel)
All database schemas MUST use SQLModel to ensure Python type safety and Pydantic validation across the backend. No manual SQL for schema definition is allowed; use SQLModel classes exclusively.

### VI. Centralized Environment Configuration
Environment configuration must be centralized using `pydantic-settings` to ensure all necessary environment variables are present and valid before the application starts.

## Technical Constraints

- **Database**: Neon Serverless PostgreSQL is the authoritative source of truth, accessed via connection URI.
- **ORM**: SQLModel (synchronous driver for Phase II) is mandatory.
- **API Schema**: Pydantic models MUST be used for all request and response bodies.
- **Authentication**: Better Auth with JWT-based session management is the standard. Backend MUST verify JWT signatures and decode claims for user identification.

## Development Standards

- **Code Formatting**: Python code MUST be formatted with Black; TypeScript/JavaScript code MUST be formatted with Prettier.
- **Migrations**: Database setup and evolution MUST be managed via Alembic.
- **Structure**: Multi-project structure (Backend vs Frontend) must be clearly defined and scalable.

## Governance

This constitution serves as the primary governance document for the project. Amendments require a version bump and an update to the Sync Impact Report. All automated development tasks (specs, plans, tasks) must verify adherence to these principles.

**Version**: 1.1.0 | **Ratified**: 2026-01-08 | **Last Amended**: 2026-01-08
