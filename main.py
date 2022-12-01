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
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Todos = {
    "todos": [
        {
            "id": 1,
            "title": "Read a book",
            "category": "Other",
            "done": False
        },
        {
            "id": 2,
            "title": "Go to the Doc",
            "category": "Health",
            "done": True
        },
        {
            "id": 3,
            "title": "Learn Angular",
            "category": "Work",
            "done": False
        },
        {
            "id": 4,
            "title": "Learn FastAPI",
            "category": "Work",
            "done": True
        }
    ]
}

todo_data = Todos['todos']


class Todo(BaseModel):
    id: int
    title: str
    category: str
    done: bool


@app.get("/")
async def home():
    return Todos


@app.get("/todo/{id_todo}", response_model=Todo)
async def get_todos_by_id(id_todo: int):
    for todo in todo_data:
        for val in todo.values():
            if val == id_todo:
                return todo
    if id_todo not in todo.values():
        raise HTTPException(status_code=404, detail="Item not Found")


@app.put("/todo/{id_todo}", response_model=Todo)
async def update_todo_by_id(id_todo: int, new_todo: Todo):
    for todo in todo_data:
        for val in todo.values():
            if val == id_todo:
                Todos["todos"][id_todo - 1] = new_todo
                return new_todo
    if id_todo not in todo.values():
        raise HTTPException(status_code=404, detail="Item not Found")


@app.post("/todo/", response_model=Todo)
async def create_todo(created_todo: Todo):
    try:
        todo_data.append(created_todo)
    except TypeError:
        print(TypeError)
        raise HTTPException(status_code=422, detail="Unprocessable Entity")

    finally:
        return created_todo


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
