import psycopg2
from sqlalchemy.orm import Session
from models import Todo
from schemas import TodoSchema
from settings import settings


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Todo).offset(skip).limit(limit).all()


def get_todo_by_id(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()


def create_todo(db: Session, todo: TodoSchema):
    new_todo = Todo(
        id=todo.id,
        title=todo.title,
        category=todo.category,
        done=todo.done
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def deleted_todo(db: Session, todo_id: int):
    todo_to_be_deleted = get_todo_by_id(db=db, todo_id=todo_id)
    if todo_to_be_deleted is None:
        return None
    else:
        db.delete(todo_to_be_deleted)
        db.commit()
        return True


def update_todo(db: Session, todo_id: int, title: str, category: str, done: bool):
    todo_to_be_updated = get_todo_by_id(db=db, todo_id=todo_id)

    todo_to_be_updated.title = title
    todo_to_be_updated.category = category
    todo_to_be_updated.done = done

    db.commit()
    db.refresh(todo_to_be_updated)
    return todo_to_be_updated


def finishing_todo(db: Session, todo_id: int):
    todo_finished = get_todo_by_id(db=db, todo_id=todo_id)

    if todo_finished is None:
        return None

    todo_finished.done = True

    db.commit()
    db.refresh(todo_finished)
    return todo_finished


def get_highest_id():
    sqlalchemy_db_url = settings.Database_url
    connection = psycopg2.connect(sqlalchemy_db_url)
    cursor = connection.cursor()

    cursor.execute('SELECT MAX(id) FROM todo')
    highest_id: int = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return highest_id
