from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

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


@app.get("/todo/{id_todo}", response_model=Todo)
async def get_todos_by_id(id_todo: int):
    for todo in todos:
        id_actual: int = todo.get("id")
        if id_actual == id_todo:
            return todo
        else:
            raise HTTPException(status_code=404, detail="Item not found")

@app.put("/todo/", response_model=Todo)
async def update_todo_by_id(id_todo: int, todo: Todo):
    try:
        updated_todo = jsonable_encoder(todo)
        todos[id_todo] = updated_todo
        return f'Updated todo at {id_todo} position: {updated_todo}'
    except TypeError:
        return 'TypeError found'
    finally:
        return f'All Todos: \n{todos}'


@app.post("/todo/", response_model=Todo)
async def create_todo(todo: Todo):
    try:
        todos.append(todo)
    except TypeError:
        return TypeError
    finally:
        return todo
