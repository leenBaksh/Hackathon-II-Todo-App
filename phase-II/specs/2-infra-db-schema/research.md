# Research: Core Infrastructure & Database Schema

## Decisions & Rationale

### 1. Project Structure
**Decision**: Monorepo with `backend/` and `frontend/` subdirectories.
**Rationale**: Allows for independent scaling of services while keeping related code in a single repository.
**Alternatives Considered**: Single flat project structure (too cluttered for multi-user web app).

### 2. SQLModel Integration
**Decision**: Use SQLModel as the primary ORM and schema validator.
**Rationale**: Inherits the best parts of SQLAlchemy and Pydantic, ensuring type safety from DB to API.
**Alternatives Considered**: Direct SQLAlchemy (no native Pydantic integration), Pydantic with raw queries (no ORM features).

### 3. Migration Strategy
**Decision**: Alembic with SQLModel metadata.
**Rationale**: Industry standard for Python DB migrations.
**Alternatives Considered**: Manual schema management (error-prone).

### 4. Configuration Management
**Decision**: `pydantic-settings` with `.env` file.
**Rationale**: Clean, validated configuration that prevents application startup if critical variables are missing.
**Alternatives Considered**: `os.environ` directly (no validation).

## Best Practices Found
- Use standard `psycopg2-binary` for synchronous database operations in Phase II.
- Ensure SQLModel models are imported in `alembic/env.py` to allow autogenerate to detect changes.
- Use `Relationship` without internal field leaks in Pydantic schemas.
