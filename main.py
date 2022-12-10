from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
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

database = {
    "todos": [

    ]
}

todo_data = database['todos']


class Todo(BaseModel):
    id: int
    title: str
    category: str
    done: bool


@app.get("/")
async def home():
    return database


@app.get("/todo/{id_todo}", response_model=Todo)
async def get_todos_by_id(id_todo: int):
    for i in range(len(todo_data)):
        if database['todos'][i]['id'] == id_todo:
            return todo_data[i]
    else:
        raise HTTPException(status_code=404, detail="Item not Found")


@app.put("/todo/{id_todo}", response_model=Todo)
async def update_todo_by_id(id_todo: int, new_todo: Todo):
    for i in range(len(todo_data)):
        if todo_data[i]['id'] == id_todo:
            todo_data[i] = new_todo
            return todo_data[i]
    else:
        raise HTTPException(status_code=404, detail="Item not Found")


@app.post("/todo/", response_model=Todo)
async def create_todo(created_todo: Todo):
    try:
        todo_data.append(created_todo)
    except TypeError:
        raise HTTPException(status_code=422, detail="Unprocessable Entity")

    finally:
        return created_todo


@app.patch("/todo/{id_todo}")
async def update_todo_field(id_todo: int, id_field: int, new_value: str):
    todo_to_be_updated: Todo
    keys_map = {
        1: "id",
        2: "title",
        3: "category",
        4: "done"
    }

    for key in keys_map.keys():
        if id_field == key:
            field_to_be_changed = keys_map[id_field]
            for i in range(len(todo_data)):
                if todo_data[i]['id'] == id_todo:
                    todo_to_be_updated = todo_data[i]
                    if id_field == 1:
                        new_value = int(new_value)

                    todo_to_be_updated[field_to_be_changed] = new_value
                    todo_data[i] = todo_to_be_updated
                    return todo_data[i]
            else:
                raise HTTPException(status_code=404, detail="Item not Found")
    else:
        return {'Message': 'Id field out of range'}


@app.delete("/todo/{id_todo}")
async def delete_todo_by_id(id_todo: int):
    for i in range(len(database['todos'])):
        if database['todos'][i]['id'] == id_todo:
            database['todos'].remove(database['todos'][i])
            return {"Message": "Element removed"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
