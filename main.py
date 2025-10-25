from fastapi import FastAPI
from routers import user_router

app = FastAPI(title="FastAPI MongoDB CRUD with MVC Structure")
app.include_router(user_router.router)

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI CRUD with Service and Controller Layers"}
