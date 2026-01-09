import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'backend'))

print("Current working directory:", os.getcwd())
print("Python path:", sys.path[:3])  # Print first 3 entries

try:
    from backend.app.models.user import User
    from backend.app.models.task import Task
    print("Models imported successfully")
except ImportError as e:
    print(f"Import error: {e}")

try:
    from alembic.config import Config
    print("Alembic config imported successfully")
except ImportError as e:
    print(f"Alembic import error: {e}")

try:
    from backend.app.core.config import settings
    print("Settings imported successfully")
except ImportError as e:
    print(f"Settings import error: {e}")