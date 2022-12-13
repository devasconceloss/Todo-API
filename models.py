from sqlalchemy import Column, Integer, String, Boolean
from database_connection import Base


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    category = Column(String)
    done = Column(Boolean)
