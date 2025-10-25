from fastapi import APIRouter
from models import user_model
from controllers import user_controller

router = APIRouter(prefix="/uers", tags=["Users"])

router.get("/", response_model=list[user_model.UserResponse])(user_controller.get_users_controller)
router.get("/{user_id}", response_model=user_model.UserResponse)(user_controller.get_user_controller)
router.post("/", response_model=user_model.UserResponse)(user_controller.create_user_controller)
router.put("/{user_id}", response_model=user_model.UserResponse)(user_controller.update_user_controller)
router.delete("/{user_id}")(user_controller.delete_user_controller)
