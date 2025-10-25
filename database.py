from pymongo import MongoClient

client = MongoClient("mongodb://locallhost:27017")
db = client["fastapi_crud"]
users_collection = db["users"]
