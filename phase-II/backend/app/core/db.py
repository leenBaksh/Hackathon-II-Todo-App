from typing import Annotated, Generator
from fastapi import Depends
from sqlmodel import Session, create_engine, SQLModel
from .config import settings

# Import models to register them with SQLModel metadata
from ..models.user import User
from ..models.task import Task

# Register all models with SQLModel for metadata
def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)

engine = create_engine(settings.DATABASE_URL)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
