import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


database_url = os.getenv('database_url')
engine = create_engine(database_url)
local_session = sessionmaker(autocommit=False, autoflush=False)
Base = declarative_base()
