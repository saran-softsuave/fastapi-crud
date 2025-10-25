# schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: str  # MongoDB ObjectId will be converted to string
