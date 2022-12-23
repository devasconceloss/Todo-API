from fastapi import FastAPI
from database_connection import engine
import models
from endpoints import *
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)

origins = ['localhost:4200',
           'localhost:8000',
           'https://thiagovasc.github.io/Todo-App/']

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
