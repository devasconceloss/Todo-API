from fastapi import APIRouter, Path, Depends
from database_connection import SessionLocal
from sqlalchemy.orm import Session


def get_data_base():
    data_base = SessionLocal()
    try:
        yield data_base
    finally:
        data_base.close()