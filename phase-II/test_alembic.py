import sys
import os
sys.path.insert(0, os.path.abspath('.'))

# Change to the backend directory
os.chdir('D:\\Phase-I-Hackathon-II\\phase-II\\backend')

from alembic.config import Config
from alembic import command

# Create Alembic config
alembic_cfg = Config("alembic.ini")

# Try to generate the revision
try:
    command.revision(alembic_cfg, autogenerate=True, message="initial")
    print("Migration generated successfully!")
except Exception as e:
    print(f"Error generating migration: {e}")
    import traceback
    traceback.print_exc()