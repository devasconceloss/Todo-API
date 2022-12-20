from fastapi import APIRouter, Depends, HTTPException
from database_connection import SessionLocal
from sqlalchemy.orm import Session
import crud_functions
from schemas import Response, RequestTodo
from schemas import TodoSchema

router = APIRouter()


def get_data_base():
    data_base = SessionLocal()
    try:
        yield data_base
    finally:
        data_base.close()


@router.get("/", tags=["todos"])
async def get_all_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_data_base)):
    todolist = crud_functions.get_todos(db, skip, limit)
    return Response(
        status="OK",
        code="200",
        message="Fetched all data",
        result=todolist
    )


@router.get("/todos/{todo_id}", tags=["todos"])
async def get_todo_by_id(todo_id: int, db: Session = Depends(get_data_base)):
    selected_todo: TodoSchema = crud_functions.get_todo_by_id(db=db, todo_id=todo_id)
    if selected_todo:
        return Response(
            status="OK",
            code="200",
            message="Fetched the selected data",
            result=selected_todo
        )
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@router.post("/todos", tags=["todos"])
async def create_todo(request: RequestTodo, db: Session = Depends(get_data_base)):
    new_todo = crud_functions.create_todo(db=db, todo=request.parameter)
    return Response(
        status="Created Todo",
        code="200",
        message="Todo created successfully",
        result=new_todo

    )


@router.delete("/todos/{todo_id}", tags=['todos'])
async def delete_todo(todo_id: int,  db: Session = Depends(get_data_base)):
    deleted_todo = crud_functions.deleted_todo(db, todo_id=todo_id)
    if deleted_todo is None:
        raise HTTPException(status_code=404, detail="Item not found")

    else:
        return Response(
            status="OK",
            code="200",
            message="Todo deleted"
        )


@router.patch("/todos/{todo_id}", tags=['todos'])
async def updating_todo(request: RequestTodo, db: Session = Depends(get_data_base)):
    todo_to_be_updated: TodoSchema = crud_functions.get_todo_by_id(db, todo_id=request.parameter.id)

    return todo_to_be_updated


@router.patch("/todos/finish/{todo_id}", tags=['todos'])
async def finishing_todo(todo_id: int, db: Session = Depends(get_data_base)):
    todo_done = crud_functions.finishing_todo(
        db,
        todo_id=todo_id
    )
    if todo_done is None:
        raise HTTPException(status_code=404, detail="Item not found")

    else:
        return Response(
            status="Accepted",
            code="202",
            message='Todo is completed',
            result=todo_done
        )


@router.get("/highest_id", tags=['id'])
async def get_highest_id():
    highest_id = int(crud_functions.get_highest_id())
    return highest_id
