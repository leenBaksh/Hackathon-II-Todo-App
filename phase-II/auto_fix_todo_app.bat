@echo off
echo ========================================
echo Todo Dashboard Auto-Fix Script
echo ========================================

echo Stopping all processes...
taskkill /F /IM python.exe 2>nul
taskkill /F /IM node.exe 2>nul

echo Cleaning up ports...
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :8000') do taskkill /F /PID %%a 2>nul
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :3000') do taskkill /F /PID %%a 2>nul
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :3001') do taskkill /F /PID %%a 2>nul

echo Cleaning frontend cache...
cd /d D:\Phase-I-Hackathon-II\phase-II\frontend
if exist .next rmdir /s /q .next

echo Setting up environment variables...
echo BACKEND_API_URL=http://127.0.0.1:8000 > .env.local

echo Verifying backend database...
cd /d D:\Phase-I-Hackathon-II\phase-II\backend
if not exist todo.db (
    echo Creating database...
    python -c "from app.core.db import create_db_and_tables; create_db_and_tables()"
)

echo Checking CORS configuration...
findstr /m "CORSMiddleware" app/main.py >nul
if errorlevel 1 (
    echo Fixing CORS configuration...
    copy app/main.py app/main.py.backup
    (
        echo from fastapi import FastAPI
        echo from fastapi.middleware.cors import CORSMiddleware
        echo from .core.config import settings
        echo from .api.routers import users, tasks
        echo.
        echo app = FastAPI(title=settings.PROJECT_NAME)
        echo.
        echo ^^^^ Add CORS middleware
        echo app.add_middleware^(
        echo     CORSMiddleware,
        echo     allow_origins=["*"],  ^^ In production, replace with specific origins
        echo     allow_credentials=True,
        echo     allow_methods=["*"],
        echo     allow_headers=["*"],
        echo ^)
        echo.
        echo ^^^^ Include API routers
        echo app.include_router^^(users.router, prefix=settings.API_V1_STR^^)
        echo app.include_router^^(tasks.router, prefix=settings.API_V1_STR^^)
        echo.
        echo @app.get^^(^"/"^)
        echo def read_root^^(^):
        echo     return {"message": "Todo Backend API"}
    ) > temp_main.py
    move /y temp_main.py app/main.py
)

echo Starting backend server in background...
start /min cmd /c "cd /d D:\Phase-I-Hackathon-II\phase-II\backend && uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload --log-level info"

echo Waiting for backend to start...
timeout /t 5 /nobreak >nul

echo Starting frontend server in background...
cd /d D:\Phase-I-Hackathon-II\phase-II\frontend
start /min cmd /c "cd /d D:\Phase-I-Hackathon-II\phase-II\frontend && npm run dev"

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Backend: http://127.0.0.1:8000
echo Frontend: http://localhost:3000 (or 3001 if 3000 is busy)
echo.
echo The Todo Dashboard should now be accessible without errors.
echo.
pause