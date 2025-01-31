from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    username: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None
    is_active: Optional[bool] = None


class User(UserBase):
    id: int
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime
