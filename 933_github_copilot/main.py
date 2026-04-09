from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Define request/response models
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class User(BaseModel):
    username: str
    email: str
    age: int
    is_active: bool = True

# In-memory storage
items_db = []
users_db = []

@app.post("/items/")
async def create_item(item: Item):
    """
    Create a new item with JSON payload
    """
    items_db.append(item.dict())
    return {
        "message": "Item created successfully",
        "item": item,
        "total_items": len(items_db)
    }

@app.post("/users/")
async def create_user(user: User):
    """
    Create a new user with JSON payload
    """
    users_db.append(user.dict())
    return {
        "message": "User created successfully",
        "user": user,
        "total_users": len(users_db)
    }

@app.post("/process/")
async def process_data(data: dict):
    """
    Accept arbitrary JSON payload and process it
    """
    return {
        "received": data,
        "processed": True,
        "item_count": len(data)
    }

@app.get("/items/")
async def get_items():
    """Get all items"""
    return items_db

@app.get("/users/")
async def get_users():
    """Get all users"""
    return users_db
