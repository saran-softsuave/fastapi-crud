from fastapi import HTTPException
from models import user_model
from services import user_service

def get_users_controller():
    return user_service.get_all_users()

def get_user_controller(user_id: str):
    user = user_service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def create_user_controller(user: user_model.UserCreate):
    new_user = user_service.create_user(user.dict())
    if not new_user:
        raise HTTPException(status_code=400, detail="Email already exists")
    return new_user

def update_user_controller(user_id: str, user: user_model.UserCreate):
    updated_user = user_service.update_user(user_id, user.dict())
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

def delete_user_controller(user_id: str):
    success = user_service.delete_user(user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
