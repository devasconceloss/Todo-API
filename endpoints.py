from fastapi import APIRouter, Depends
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
        status="200",
        code="Ok",
        message="Fetched all data",
        result=todolist
    )


@router.get("/todos/{todo_id}", tags=["todos"])
async def get_todo_by_id(todo_id: int, db: Session = Depends(get_data_base)):
    selected_todo: TodoSchema = crud_functions.get_todo_by_id(db=db, todo_id=todo_id)
    return Response(
        status="200",
        code="OK",
        message="Fetched the selected data",
        result=selected_todo
    )


@router.post("/todos", tags=["todos"])
async def create_todo(request: RequestTodo, db: Session = Depends(get_data_base)):
    crud_functions.create_todo(db=db, todo=request.parameter)
    return Response(
        status="201",
        code="Created",
        message="Todo created successfully"
    )


@router.delete("/", tags=["todos"])
async def deleting_todo(request: RequestTodo, db: Session = Depends(get_data_base)):
    crud_functions.deleted_todo(db=db, todo_id=request.parameter.id)
    return Response(
        status="204",
        code="No content"
    )


@router.put("/todos/{todo_id}")
async def updating_todo(request: RequestTodo, db: Session = Depends(get_data_base)):
    updated_todo = crud_functions.updated_todo(
        db,
        todo_id=request.parameter.id,
        title=request.parameter.title,
        category=request.parameter.category,
        done=request.parameter.done
    )

    return Response(
        status="202",
        code="Accepted",
        result=updated_todo
    )
