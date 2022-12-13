from typing import Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class TodoSchema(BaseModel):
    id: Optional[int] = None
    title: Optional[str] = None
    category: Optional[str] = None
    done: Optional[bool] = None

    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestTodo(BaseModel):
    parameter: TodoSchema = Field(...)


class Response(GenericModel, Generic[T]):
    status: str
    code: str
    message: str
    result: Optional[T]
    