from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = [
    {
        "id": 1,
        "title": "Read a Book",
        "category": "Other",
        "done": False
    },
    {
        "id": 2,
        "title": "Go to the gym",
        "category": "Health",
        "done": True
    },
    {
        "id": 3,
        "title": "Watch Mr Robot",
        "category": "Other",
        "done": False
    }
]


class Todo(BaseModel):
    id: int
    title: str
    category: str
    done: bool


@app.get("/")
async def home():
    return todos


@app.get("/todo/{id_todo}")
async def get_todos(id_todo: int):
    for todo in todos:
        id_actual: int = todo.get("id")
        if id_actual == id_todo:
            return todo
