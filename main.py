from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

todos = {
    0: {
        "id": 1,
        "title": "Read a book",
        "category": "Other",
        "done": False
    },
    1: {
        "id": 2,
        "title": "Go to the Doc",
        "category": "Health",
        "done": True
    },
    2: {
        "id": 3,
        "title": "Learn Angular",
        "category": "Work",
        "done": False
    },
    3: {
        "id": 4,
        "title": "Learn FastAPI",
        "category": "Work",
        "done": True
    }
}


class Todo(BaseModel):
    id: int
    title: str
    category: str
    done: bool


@app.get("/")
async def home():
    return todos


@app.get("/todo/{id_todo}", response_model=Todo)
async def get_todos_by_id(id_todo: int):
    if id_todo in todos.keys():
        return todos[id_todo]
    else:
        raise HTTPException(status_code=404, detail="Item not Found")


@app.put("/todo/{id_todo}", response_model=Todo)
async def update_todo_by_id(id_todo: int, todo: Todo):
    if id_todo in todos.keys():
        updated_todo = jsonable_encoder(todo)
        todos[id_todo] = updated_todo
        return updated_todo
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@app.post("/todo/", response_model=Todo)
async def create_todo(todo: Todo):
    try:
        todos[len(todos)] = todo
    except TypeError:
        return TypeError
    finally:
        return todo


@app.patch("/todo/{id_todo}")
async def update_todo_field(id_todo: int, id_field: int, new_value: str):
    keys_map = {
        1: "id",
        2: "title",
        3: "category",
        4: "done"
    }

    field_to_be_changed = keys_map[id_field]

    if id_todo in todos.keys():
        todo_to_be_updated = todos[id_todo]
        if id_field == 1:
            new_value = int(new_value)
    todo_to_be_updated[field_to_be_changed] = new_value
    return todo_to_be_updated




@app.delete("/todo/{id_todo}")
async def delete_todo_by_id(id_todo: int):
    if id_todo in todos.keys():
        del todos[id_todo]
        return todos
    else:
        raise HTTPException(status_code=404, detail="Item not found")
