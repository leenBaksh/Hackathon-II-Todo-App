from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Task:
    """Represents a single todo item in the system."""
    id: int
    description: str
    completed: bool = False
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
