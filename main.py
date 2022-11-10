from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()

todos = {

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
        raise HTTPException(status_code=404, detail="Item not found")


@app.put("/todo/{id_todo}", response_model=Todo)
async def update_todo_by_id(id_todo: int, todo: Todo):
    if id_todo in todos.keys():
        updated_todo = jsonable_encoder(todo)
        todo[id_todo] = updated_todo
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
