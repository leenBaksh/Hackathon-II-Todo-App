# Quickstart: Core Infrastructure

## Prerequisites

- Python 3.11+
- A Neon Serverless PostgreSQL instances
- `.env` file with `DATABASE_URL`

## Setup Steps

1. **Install Dependencies**:

   ```bash
   pip install -r backend/requirements.txt
   ```

2. **Initialize Database**:

   ```bash
   python backend/scripts/setup_db.py
   ```

3. **Verify Connection**:

   ```bash
   python backend/scripts/verify_db.py
   ```

## Development Workflow

- Model changes: Modify `backend/app/models/*.py`
- Migrations: `alembic revision --autogenerate -m "description"`
- Database sync: `alembic upgrade head`
