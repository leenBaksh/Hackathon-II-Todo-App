from fastapi import APIRouter, HTTPException
from typing import List
from ...core.db import SessionDep
from ...models.user import User, UserCreate, UserUpdate
from ...schemas.user import UserPublic as UserSchema
import uuid
from datetime import datetime

router = APIRouter()

@router.get("/users", response_model=List[UserSchema])
def read_users(db: SessionDep, skip: int = 0, limit: int = 100):
    users = db.query(User).offset(skip).limit(limit).all()
    return users

@router.get("/users/{user_id}", response_model=UserSchema)
def read_user(user_id: str, db: SessionDep):
    from uuid import UUID
    try:
        uuid_obj = UUID(user_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    user = db.get(User, uuid_obj)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users", response_model=UserSchema)
def create_user(user: UserCreate, db: SessionDep):
    # In a real app, you would hash the password here
    # For now, we'll just store it directly (not secure)
    db_user = User(
        id=uuid.uuid4(),
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        hashed_password=user.password,  # In real app, hash this properly
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.put("/users/{user_id}", response_model=UserSchema)
def update_user(user_id: str, user: UserUpdate, db: SessionDep):
    from uuid import UUID
    try:
        uuid_obj = UUID(user_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    db_user = db.get(User, uuid_obj)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    user_data = user.model_dump(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/users/{user_id}")
def delete_user(user_id: str, db: SessionDep):
    from uuid import UUID
    try:
        uuid_obj = UUID(user_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    user = db.get(User, uuid_obj)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}