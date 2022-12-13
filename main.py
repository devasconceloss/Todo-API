from fastapi import FastAPI
from database_connection import engine
import models
from endpoints import *


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router, tags=["todo"])
