@echo off
cd /d D:\Phase-I-Hackathon-II\phase-II\backend
echo Starting backend server on 127.0.0.1:8000...
python -c "from app.main import app; import uvicorn; uvicorn.run(app, host='127.0.0.1', port=8000, log_level='info')"
pause