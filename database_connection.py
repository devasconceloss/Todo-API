from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import settings

sqlalchemy_db_url = settings.Database_url

engine = create_engine(sqlalchemy_db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False)
