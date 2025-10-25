from bson import ObjectId
from database import users_collection

# Helper to convert MongoDB document to dict
def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "phone": user["phone"]
    }

def get_all_users():
    try:
        return [user_helper(user) for user in users_collection.find()]
    except Exception as e:
        return []

def get_user_by_id(user_id: str):
    try:
        user = users_collection.find_one({"_id": ObjectId(user_id)})
        return user_helper(user) if user else None
    except Exception as e:
        return None

def create_user(user_data: dict):
    try:
        if users_collection.find_one({"email": user_data["email"]}):
            return None
        result = users_collection.insert_one(user_data)
        return user_helper(users_collection.find_one({"_id": result.inserted_id}))
    except Exception as e:
        return None

def update_user(user_id: str, user_data: dict):
    try:
        result = users_collection.update_one(
            {"_id": ObjectId(user_id)}, {"$set": user_data}
        )
        if result.matched_count == 0:
            return None
        return user_helper(users_collection.find_one({"_id": ObjectId(user_id)}))
    except Exception as e:
        return None

def delete_user(user_id: str):
    try:
        result = users_collection.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count > 0
    except Exception as e:
        return False
